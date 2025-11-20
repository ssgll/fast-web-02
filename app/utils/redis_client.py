from app.core import logger
import aioredis
from app.core.config import config

# 创建Redis客户端实例
# 注意：aioredis v2.0版本中Redis构造函数不支持prefix参数
redis_client = aioredis.Redis(
    host=config.CACHE_REDIS_HOST,
    port=config.CACHE_REDIS_PORT,
    password=config.CACHE_REDIS_PASSWORD,
    db=config.CACHE_REDIS_DB,
    socket_timeout=config.REDIS_TIMEOUT,
    ssl=config.CACHE_REDIS_SSL,
)


async def get_redis_client():
    """获取Redis客户端实例"""
    if await redis_client.ping():
        return redis_client
    else:
        raise Exception("Redis连接异常")


async def close_redis_client():
    """关闭Redis客户端连接"""
    if redis_client:
        await redis_client.close()
        logger.info("Redis连接已关闭")


# async def cache(key:str):
#     def decorator(func:Callable):
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#         # 先查redis缓存
#             cached_data = await redis_client.get(key.format(**kwargs))
#             if cached_data:
#                 return json.loads(cached_data)
#
#             # 缓存未命中时，执行原方法获取数据
#             result = await func(*args,**kwargs)
#             if isinstance(result,list):
#                 data = [item.dict() for item in result]
#             else:
#                 data = result.dict() if result else None
#             await redis_client.setex(key,expire, json.dumps(data))
#