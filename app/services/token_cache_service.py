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
        
        key = f"{config.CACHE_REDIS_PREFIX}token:{token}"


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

        key = f"{config.CACHE_REDIS_PREFIX}token:{token}"

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

        key = f"{config.CACHE_REDIS_PREFIX}token:{token}"
        try:
            result = await redis_client.delete(key)
            return result > 0
        except Exception as e:
            logger.error(f"移除token失败,{e}")
            return False

    @staticmethod
    async def is_token_valid(token:str)->bool:
        """检查token是否有效
        Args:
            token (str): token
        Returns:
            bool: 是否有效
        """
        user = await TokenCacheService.get_cached_user(token)
        return user is not None
