import json
import logging
from typing import Any, Optional, Callable, Awaitable
from functools import wraps
from app.utils.redis_client import redis_client
from app.core.config import config
import hashlib

logger = logging.getLogger(__name__)

class CacheService:
    """缓存服务类，提供统一的缓存操作接口"""
    
    @staticmethod
    def _generate_key(prefix: str, key: str) -> str:
        """生成带前缀的缓存键"""
        return f"{config.CACHE_REDIS_PREFIX}{prefix}:{key}"
    
    @staticmethod
    def _hash_key(key: str) -> str:
        """对键进行哈希以确保长度合适"""
        return hashlib.md5(key.encode()).hexdigest()
    
    @staticmethod
    async def get(prefix: str, key: str) -> Optional[Any]:
        """从缓存中获取数据"""
        try:
            cache_key = CacheService._generate_key(prefix, CacheService._hash_key(key))
            cached_data = await redis_client.get(cache_key)
            if cached_data:
                return json.loads(cached_data)
        except Exception as e:
            logger.error(f"Cache get error: {e}")
        return None
    
    @staticmethod
    async def set(prefix: str, key: str, value: Any, expire: int = 3600) -> bool:
        """设置缓存数据"""
        try:
            cache_key = CacheService._generate_key(prefix, CacheService._hash_key(key))
            if isinstance(value, list):
                data = [item.model_dump() if hasattr(item, 'model_dump') else item for item in value]
            elif isinstance(value, tuple):
                # 处理元组类型，特别是分页数据 (list, int)
                if len(value) == 2 and isinstance(value[0], list):
                    # 处理分页数据中的用户列表
                    user_list = [item.model_dump() if hasattr(item, 'model_dump') else item for item in value[0]]
                    data = [user_list, value[1]]
                else:
                    data = list(value)
            elif hasattr(value, 'model_dump'):
                data = value.model_dump()
            else:
                data = value
            
            result = await redis_client.setex(
                cache_key, 
                expire, 
                json.dumps(data, default=str)
            )
            return result
        except Exception as e:
            logger.error(f"Cache set error: {e}")
            return False
    
    @staticmethod
    async def delete(prefix: str, key: str) -> bool:
        """删除缓存数据"""
        try:
            cache_key = CacheService._generate_key(prefix, CacheService._hash_key(key))
            result = await redis_client.delete(cache_key)
            return result > 0
        except Exception as e:
            logger.error(f"Cache delete error: {e}")
            return False
    
    @staticmethod
    async def clear_prefix(prefix: str) -> bool:
        """清除指定前缀的所有缓存"""
        try:
            pattern = f"{config.CACHE_REDIS_PREFIX}{prefix}:*"
            keys = await redis_client.keys(pattern)
            if keys:
                await redis_client.delete(*keys)
            return True
        except Exception as e:
            logger.error(f"Cache clear prefix error: {e}")
            return False


def cache_result(prefix: str, expire: int = 3600):
    """
    缓存装饰器，用于缓存函数结果
    
    Args:
        prefix: 缓存键前缀
        expire: 缓存过期时间（秒），默认1小时
    """
    def decorator(func: Callable[..., Awaitable[Any]]):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # 生成缓存键
            key_parts = [func.__name__]
            if args:
                key_parts.extend(str(arg) for arg in args)
            if kwargs:
                key_parts.extend(f"{k}={v}" for k, v in sorted(kwargs.items()))
            
            cache_key = ":".join(key_parts)
            
            # 尝试从缓存获取
            cached_result = await CacheService.get(prefix, cache_key)
            if cached_result is not None:
                logger.debug(f"Cache hit for key: {cache_key}")
                # 如果缓存的是用户数据，需要转换回Pydantic模型
                import inspect
                # 获取函数的返回类型注解
                return_type = inspect.signature(func).return_annotation
                
                # 如果是列表类型
                if hasattr(return_type, '__origin__') and return_type.__origin__ is list:
                    from app.schemas.user import UserOut
                    if isinstance(cached_result, list):
                        # 确保列表中的每个元素都是字典
                        if cached_result and isinstance(cached_result[0], dict):
                            return [UserOut(**item) for item in cached_result]
                        else:
                            # 如果不是字典，直接返回原始数据
                            return cached_result
                # 如果是元组类型（分页数据）
                elif hasattr(return_type, '__origin__') and return_type.__origin__ is tuple:
                    from app.schemas.user import UserOut
                    # 检查是否为分页数据格式
                    if isinstance(cached_result, list) and len(cached_result) == 2:
                        # 检查第一个元素是否为用户列表
                        if isinstance(cached_result[0], list):
                            # 检查用户列表中的元素是否为字典
                            if cached_result[0] and isinstance(cached_result[0][0], dict):
                                users = [UserOut(**item) for item in cached_result[0]]
                                total = cached_result[1]
                                return (users, total)
                            else:
                                # 如果用户列表中的元素不是字典，直接返回原始数据
                                return (cached_result[0], cached_result[1])
                        else:
                            # 如果第一个元素不是列表，直接返回原始数据
                            return tuple(cached_result)
                    else:
                        # 如果缓存结果不是列表，但返回类型是元组，则尝试转换
                        if isinstance(cached_result, (list, tuple)):
                            return tuple(cached_result)
                        else:
                            # 如果缓存结果既不是列表也不是元组，返回原始数据
                            return cached_result
                # 如果是单个对象
                elif isinstance(cached_result, dict):
                    from app.schemas.user import UserOut
                    return UserOut(**cached_result)
                
                return cached_result
            
            # 缓存未命中，执行函数
            logger.debug(f"Cache miss for key: {cache_key}")
            result = await func(*args, **kwargs)
            
            # 将结果存入缓存
            await CacheService.set(prefix, cache_key, result, expire)
            return result
        
        return wrapper
    return decorator
