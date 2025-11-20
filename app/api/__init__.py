from fastapi import APIRouter, Depends

from .user import router as user_router
from .login import router as login_router
from .system import router as system_router

from app.api.login import get_current_user

api_router: APIRouter = APIRouter()

api_router.include_router(router=login_router, prefix="/auth", tags=["auth"])

# 为整个用户路由添加登录认证依赖
# api_router.include_router(router=user_router, prefix="/user", tags=["user"])
api_router.include_router(router=user_router, prefix="/user",dependencies=[Depends(dependency=get_current_user)], tags=["user"])
api_router.include_router(router=system_router, prefix="/system",dependencies=[Depends(dependency=get_current_user)], tags=["system"])

__all__ = ["api_router"]
