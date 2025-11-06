from fastapi.applications import FastAPI


from .init_app import lifespan
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# 导入异常处理器
from app.exceptions.exception import (
    global_exception_handler,
    validation_exception_handler,
    http_exception_handler
)

# 导入中间件
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.cors_middleware import CORSMiddleware

# 创建FastAPI应用实例并注册中间件
app: FastAPI = FastAPI(lifespan=lifespan)
app.add_middleware(middleware_class=CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(middleware_class=LoggingMiddleware)

# 注册全局异常处理器
app.exception_handler(exc_class_or_status_code=Exception)(global_exception_handler)
app.exception_handler(exc_class_or_status_code=RequestValidationError)(validation_exception_handler)
app.exception_handler(exc_class_or_status_code=StarletteHTTPException)(http_exception_handler)

__all__ = ["app"]