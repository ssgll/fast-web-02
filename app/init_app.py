from fastapi import FastAPI

from app.core import config

from tortoise import Tortoise
from contextlib import asynccontextmanager
from app.api import api_router
from app.core import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # 初始化数据库连接
        await Tortoise.init(config=config.tortoise_orm)
        await Tortoise.generate_schemas()
        logger.info("数据库初始化成功")

        # 注册API路由
        app.include_router(router=api_router)
        logger.info("路由注册成功")

        yield
    except Exception as e:
        logger.error(f"应用启动失败: {e}")
        raise
    finally:
        try:
            if Tortoise._inited:  # type: ignore
                await Tortoise.close_connections()
                logger.info("数据库连接已关闭")
        except Exception as e:
            logger.error(f"关闭数据库连接时出错: {e}")