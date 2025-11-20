from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse

from app.common.responses import ErrorResponse, ResponseFactory
from app.core.logger import logger

# 全局异常处理器
async def global_exception_handler(request: Request, exc: Exception):
    """处理未捕获的异常"""
    logger.error(f"全局异常: {str(exc)}")
    error_response: ErrorResponse = ResponseFactory.error(
        code=500,
        msg="服务器内部错误",
        details=str(exc) if hasattr(exc, '__str__') else "未知错误"
    )
    return JSONResponse(
        status_code=500,
        content=error_response.model_dump()
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """处理请求验证异常"""
    logger.error(f"请求验证异常: {exc.errors()}")
    error_response: ErrorResponse = ResponseFactory.error(
        code=422,
        msg="请求参数验证失败",
        details=str(exc.errors())
    )
    return JSONResponse(
        status_code=422,
        content=error_response.model_dump()
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """处理HTTP异常"""
    logger.error(f"HTTP异常: {exc.status_code} - {exc.detail}")
    error_response: ErrorResponse = ResponseFactory.error(
        code=exc.status_code,
        msg=exc.detail or "请求失败"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )