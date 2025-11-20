import json
from typing import Optional

from app.core import config,logger
from app.models.user import UserInDb
from app.utils.redis_client import redis_client


class TokenCacheService:
    """Token缓存服务"""

    @staticmethod
    async def cache_token(token:str,user_info:UserInDb)->bool:
        """
        将token缓存到redis中
        Args:
            token (str): token
            user_info (UserInDb): 用户信息
        
        Returns:
            bool: 是否成功
        """

        expire_minutes = config.ACCESS_TOKEN_EXPIRE_MINUTES
        
        key = f"{config.CACHE_REDIS_PREFIX}:token:{token}"


        value = json.dumps(user_info.to_dict())

        try:
            await redis_client.set(key, value, ex=expire_minutes * 60)
            return True
        except Exception as e:
            logger.error(f"缓存token失败,{e}")
            return False

    @staticmethod   
    async def get_cached_user(token:str)->Optional[dict]:
        """获取缓存的用户信息
        Args:
            token (str): token
        Returns:
            Optional[dict]: 用户信息
        """

        key = f"{config.CACHE_REDIS_PREFIX}:token:{token}"

        try:
            value = await redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"获取缓存用户信息失败,{e}")
            return None

    @staticmethod
    async def remove_token(token:str)->bool:
        """从redis中移除token
        Args:
            token (str): token
        Returns:
            bool: 是否成功
        """

        key = f"{config.CACHE_REDIS_PREFIX}:token:{token}"
        try:
            result = await redis_client.delete(key)
            return result > 0
        except Exception as e:
            logger.error(f"移除token失败,{e}")
            return False


    # 查询所有在线用户
    @staticmethod
    async def get_online_users() -> list:
        """获取所有在线用户
        Returns:
            list: 在线用户列表
        """
        pattern = f"{config.CACHE_REDIS_PREFIX}:token:*"
        keys = await redis_client.keys(pattern)
        users = []
        for key in keys:
            user = await TokenCacheService.get_caached_user(key)
            if user:
                users.append(user)
        return users

    @staticmethod
    async def remove_token_by_user_id(user_id: str) -> bool:
        """根据用户ID移除token
        Args:
            user_id (str): 用户ID
        Returns:
            bool: 是否成功
        """
        # 遍历所有user_token 
        pattern = f"{config.CACHE_REDIS_PREFIX}:token:*"
        keys = await redis_client.keys(pattern)
        for key in keys:
            user = await TokenCacheService.get_cached_user(key)
            if user and user.get("user_id") == user_id:
                await redis_client.delete(key)
                return True
        return False
