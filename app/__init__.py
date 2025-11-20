from .init_app import lifespan
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
# from prometheus_fastapi_instrumentator import Instrumentator

# 导入异常处理器
from app.exceptions import (
    global_exception_handler,
    validation_exception_handler,
    http_exception_handler
)

# 导入中间件
from app.middleware import LoggingMiddleware
from app.middleware import CORSMiddleware



# 创建FastAPI应用实例并注册中间件
app: FastAPI = FastAPI(lifespan=lifespan)
app.add_middleware(middleware_class=CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(middleware_class=LoggingMiddleware)
# Prometheus 性能监控工具
# instrumentator = Instrumentator()
# instrumentator.instrument(app=app).expose(app,"/metrics")

# 注册全局异常处理器
app.exception_handler(exc_class_or_status_code=Exception)(global_exception_handler)
app.exception_handler(exc_class_or_status_code=RequestValidationError)(validation_exception_handler)
app.exception_handler(exc_class_or_status_code=StarletteHTTPException)(http_exception_handler)

__all__ = ["app"]