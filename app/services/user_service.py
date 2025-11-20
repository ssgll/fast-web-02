import uuid
from typing import List, Optional

from fastapi import UploadFile
from pydantic import EmailStr

from app.core import logger
from app.models.user import UserInDb
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.utils.encrypt import Encrypt
from datetime import datetime

from app.utils.minio_client import upload_file,delete_file
from app.services.cache_service import cache_result, CacheService



class UserService:
    """用户业务逻辑处理类"""
    
    @staticmethod
    @cache_result("users", expire=300)  # 缓存5分钟
    async def get_users_page(page: int = 1, page_size: int = 10) -> tuple[List[UserOut], int]:
        """分页获取用户列表"""
        # 查询总用户数
        total_users = await UserInDb.all().count()
        # 查询分页数据
        users: List[UserInDb] = await UserInDb.all().limit(page_size).offset((page - 1) * page_size)
        
        user_list: List[UserOut] = [
            UserOut(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                create_at=user.create_at,
                avatar_url=user.avatar_url
            ) for user in users
        ]
        
        return user_list, total_users
    
    @staticmethod
    @cache_result("users", expire=300)  # 缓存5分钟
    async def get_all_users() -> List[UserOut]:
        """获取所有用户列表"""
        users: List[UserInDb] = await UserInDb.all()
        
        user_out_list: List[UserOut] = [
            UserOut(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                create_at=user.create_at,
                avatar_url=user.avatar_url
            ) for user in users
        ]
        
        return user_out_list
    
    @staticmethod
    @cache_result("user", expire=300)  # 缓存5分钟
    async def get_user_by_email(email: EmailStr) -> Optional[UserOut]:
        """根据邮箱查询用户"""
        user: UserInDb | None = await UserInDb.filter(is_active=True, email=email).get_or_none()
        if user:
            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                create_at=user.create_at,
                avatar_url=user.avatar_url
            )
        return None
    
    @staticmethod
    async def create_user(user_create: UserCreate) -> Optional[UserOut]:
        """创建用户"""
        # 检查用户是否已存在
        existing_user = await UserInDb.filter(email=user_create.email).get_or_none()
        if existing_user:
            return None
        
        # 对密码进行加密
        password_hash: str = Encrypt.get_password_hash(user_create.password)
        
        # 创建新用户
        user: UserInDb = await UserInDb.create(
            name=user_create.name,
            email=user_create.email,
            password_hash=password_hash,
            is_active=user_create.is_active,
            avatar_url=user_create.avatar_url
        )
        await user.save()
        
        # 清除用户相关的缓存
        await CacheService.clear_prefix("users")
        await CacheService.clear_prefix("user")
        
        return UserOut(
            id=user.id,
            name=user.name,
            email=user.email,
            is_active=user.is_active,
            create_at=user.create_at,
            avatar_url=user.avatar_url
        )
    
    @staticmethod
    async def delete_user_by_email(email: str) -> Optional[UserOut]:
        """删除指定邮箱的用户"""
        user_in_db: UserInDb | None = await UserInDb.filter(email=email).get_or_none()
        if user_in_db:
            user_out = UserOut(
                id=user_in_db.id,
                name=user_in_db.name,
                email=user_in_db.email,
                is_active=user_in_db.is_active,
                create_at=user_in_db.create_at,
                avatar_url=user_in_db.avatar_url
            )
            await UserInDb.delete(user_in_db)
            # 清除用户相关的缓存
            await CacheService.clear_prefix("users")
            await CacheService.clear_prefix("user")
            return user_out
        return None
    
    @staticmethod
    async def batch_delete_users(emails: List[str]) -> int:
        """批量删除用户"""
        deleted_count = await UserInDb.filter(email__in=emails).delete()
        # 清除用户相关的缓存
        await CacheService.clear_prefix("users")
        await CacheService.clear_prefix("user")
        return deleted_count
    
    @staticmethod
    async def update_user(email: str, user_update: UserUpdate) -> Optional[UserOut]:
        """更新指定邮箱的用户信息"""
        user_in_db: UserInDb | None = await UserInDb.filter(email=email).get_or_none()
        
        if not user_in_db:
            return None
        
        if user_update.email:
            # 检查邮箱是否已存在
            if await UserInDb.filter(email=user_update.email).exists():
                return None
            user_in_db.email = user_update.email
        if user_update.name:
            user_in_db.name = user_update.name
        if user_update.is_active is not None:
            user_in_db.is_active = user_update.is_active
        user_in_db.update_at = datetime.now()
        await user_in_db.save()
        
        # 清除用户相关的缓存
        await CacheService.clear_prefix("users")
        await CacheService.clear_prefix("user")
        
        return UserOut(
            id=user_in_db.id,
            name=str(user_in_db.name),
            email=user_in_db.email,
            is_active=user_in_db.is_active,
            create_at=user_in_db.create_at,
            avatar_url=user_in_db.avatar_url
        )
    
    @staticmethod
    async def upload_user_avatar(user_id: uuid.UUID, file: UploadFile)->str|bool:
        """上传用户头像"""
        # 读取文件内容
        image_file_endswith = (
            '.jpg',
            '.png',
            '.jpeg',
            '.gif',
            '.bmp'
        )

        if file.filename is None or not file.filename.endswith(image_file_endswith):
            return False

        file_data: bytes = await file.read()

        # 生成唯一文件名
        file_extension: str = file.filename.split(".")[-1] # type: ignore
        unique_file_name: str = f"{uuid.uuid4()}.{file_extension}"

        # 删除旧的头像
        user_in_db: UserInDb = await UserInDb.get(id=user_id)
        old_avatar = user_in_db.avatar_url
        if old_avatar:
            delete_file(old_avatar)

        # 上传到MinIO
        avatar_url:str = upload_file(file_data, unique_file_name)

        logger.info(f"<UNK>: {user_id}")

        # 更新用户记录中的avatar_url字段
        await UserInDb.filter(id=user_id).update(avatar_url=avatar_url)

        return avatar_url

    