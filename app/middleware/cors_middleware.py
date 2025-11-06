from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp
from typing import List, Optional


class CORSMiddleware(BaseHTTPMiddleware):
    """处理跨域资源共享(CORS)的中间件"""
    
    def __init__(
        self,
        app: ASGIApp,
        allow_origins: Optional[List[str]] = None,
        allow_methods: Optional[List[str]] = None,
        allow_headers: Optional[List[str]] = None,
        allow_credentials: bool = False,
        allow_origin_regex: Optional[str] = None,
        expose_headers: Optional[List[str]] = None,
        max_age: int = 600,
    ) -> None:
        super().__init__(app)
        self.allow_origins = allow_origins or ["*"]
        self.allow_methods = allow_methods or ["*"]
        self.allow_headers = allow_headers or ["*"]
        self.allow_credentials = allow_credentials
        self.allow_origin_regex = allow_origin_regex
        self.expose_headers = expose_headers or []
        self.max_age = max_age

    async def dispatch(self, request: Request, call_next) -> Response:
        # 如果是预检请求(OPTIONS)，直接返回200
        if request.method == "OPTIONS":
            response = Response(status_code=200)
            self._set_cors_headers(request, response)
            return response
            
        # 处理实际请求
        response = await call_next(request)
        self._set_cors_headers(request, response)
        return response
    
    def _set_cors_headers(self, request: Request, response: Response) -> None:
        """设置CORS响应头"""
        origin = request.headers.get("origin")
        
        # 检查源是否被允许
        if self._is_allowed_origin(origin):
            # 设置Access-Control-Allow-Origin
            if origin and "*" not in self.allow_origins:
                response.headers["Access-Control-Allow-Origin"] = origin
            elif "*" in self.allow_origins:
                response.headers["Access-Control-Allow-Origin"] = "*"
            
            # 设置其他CORS头部
            if self.allow_credentials:
                response.headers["Access-Control-Allow-Credentials"] = "true"
                
            if self.allow_methods:
                response.headers["Access-Control-Allow-Methods"] = ", ".join(self.allow_methods)
                
            if self.allow_headers:
                response.headers["Access-Control-Allow-Headers"] = ", ".join(self.allow_headers)
                
            if self.expose_headers:
                response.headers["Access-Control-Expose-Headers"] = ", ".join(self.expose_headers)
                
            if request.method == "OPTIONS" and self.max_age:
                response.headers["Access-Control-Max-Age"] = str(self.max_age)
    
    def _is_allowed_origin(self, origin: Optional[str]) -> bool:
        """检查请求源是否被允许"""
        if not origin:
            return False
            
        if "*" in self.allow_origins:
            return True
            
        return origin in self.allow_origins