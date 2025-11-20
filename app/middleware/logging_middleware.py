from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp
from app.core.logger import logger
import time


class LoggingMiddleware(BaseHTTPMiddleware):
    """用于记录HTTP请求日志的中间件"""
    
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        # 记录请求开始时间
        start_time = time.time()
        
        # 记录请求信息
        logger.info(f"收到请求: {request.method} {request.url}")
        # logger.info(f"请求头: {dict(request.headers)}")
        # logger.info(f"请求体: {await request.json()}")
        
        # 处理请求并获取响应
        response = await call_next(request)
        
        # 计算处理耗时
        process_time = time.time() - start_time
        
        # 记录响应信息
        # logger.info(f"响应状态: {response.status_code}")
        # logger.info(f"处理耗时: {process_time:.4f}秒")
        
        return response