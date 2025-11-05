from datetime import datetime, timedelta
from typing import Optional, Any
from jose import JWTError, jwt
from app.models.user import UserInDb
from app.utils.encrypt import Encrypt
from app.core.config import config
from fastapi import HTTPException, status


class AuthService:
    """认证业务逻辑处理类"""

    # JWT配置
    SECRET_KEY = config.SECRET_KEY
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = config.ACCESS_TOKEN_EXPIRE_MINUTES

    @classmethod
    async def authenticate_user(cls, email: str, password: str) -> UserInDb | bool:
        """验证用户"""
        user = await UserInDb.filter(email=email).get_or_none()
        if not user:
            return False
        if not Encrypt.verify_password_hash(password, user.password_hash):
            return False
        return user

    @classmethod
    def create_access_token(cls, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """创建访问令牌"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM)
        return encoded_jwt

    @classmethod
    async def get_current_user(cls, token: str) -> UserInDb:
        """获取当前用户"""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload: dict[str, Any] = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            email = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        except Exception:
            raise credentials_exception
            
        # 确保email是字符串类型
        if not isinstance(email, str):
            raise credentials_exception
            
        user: UserInDb | None = await UserInDb.filter(email=email).get_or_none()
        if user is None:
            raise credentials_exception
        return user