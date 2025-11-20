from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.models.user import UserInDb
from app.utils.encrypt import Encrypt
from app.core.config import config
from fastapi import HTTPException, status
from app.services.token_cache_service import TokenCacheService
from app.core.logger import logger

class AuthService:
    """认证业务逻辑处理类"""

    # JWT配置
    SECRET_KEY = config.SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = config.ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    async def authenticate_user(cls, email: str, password: str) -> UserInDb | dict:
        """验证用户"""
        user = await UserInDb.filter(email=email).get_or_none()
        if not user:
            return {"status":False, "detail": "用户不存在"}
        if not Encrypt.verify_password_hash(password, user.password_hash):
            return {"status":False, "detail": "用户名或密码错误"}
        
        if not user.is_active:
            return {"status":False, "detail": "用户已禁用"}
        
        # 创建访问令牌
        access_token_expires = timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = cls.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        
        # 缓存用户信息
        await TokenCacheService.cache_token(access_token, user)
        return user

    @classmethod
    def create_access_token(cls, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """创建访问令牌"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        
        return encoded_jwt

    @classmethod
    async def get_current_user(cls, token: str) -> UserInDb:
        """获取当前用户,优先从缓存中获取"""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            # 优先从缓存中获取用户
            user_info = await TokenCacheService.get_cached_user(token)
            
            # 如果缓存中没有用户信息，直接抛出认证异常
            if not user_info:
                raise credentials_exception
                
            # 确保必要的字段存在
            required_fields = ['id', 'name', 'email', 'is_active']
            if not all(field in user_info for field in required_fields):
                raise credentials_exception
                
            # 禁用的用户禁止登录
            user = UserInDb(**user_info)
            logger.info(f"当前用户状态: {user.is_active}")
            if not user.is_active:
                raise credentials_exception
                
            return user
        except JWTError:
            raise credentials_exception
        except Exception as e:
            # 记录具体异常信息，便于调试
            logger.error(f"获取当前用户时发生错误: {str(e)}")
            raise credentials_exception          

    @classmethod
    async def remove_token(cls, token: str) -> bool:
        """移除token"""
        return await TokenCacheService.remove_token(token)

    