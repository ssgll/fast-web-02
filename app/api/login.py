from fastapi.security.oauth2 import OAuth2PasswordBearer


from typing import cast
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.models.user import UserInDb
from app.schemas.user import UserOut
from app.common.responses import ErrorResponse, ResponseFactory, DataResponse
from app.services.auth_service import AuthService

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="login")

router: APIRouter = APIRouter()


async def get_current_user(token: str = Depends(dependency=oauth2_scheme)) -> UserInDb:
    """获取当前用户"""
    return await AuthService.get_current_user(token)


@router.post("/login", response_model=DataResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> ErrorResponse | DataResponse:
    """用户登录接口"""
    user: UserInDb | bool = await AuthService.authenticate_user(
        email=form_data.username, password=form_data.password
    )
    if not user:
        return ResponseFactory.error(
            code=status.HTTP_401_UNAUTHORIZED,
            msg="用户名或密码错误",
            error_code="AUTH_ERROR",
        )

    # 创建访问令牌
    access_token_expires: timedelta = timedelta(
        minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    # 确保user是UserInDb类型
    user_db: UserInDb = cast(UserInDb, user)
    access_token: str = AuthService.create_access_token(
        data={"sub": user_db.email}, expires_delta=access_token_expires
    )

    return ResponseFactory.success(
        data={"access_token": access_token, "token_type": "bearer"}, msg="登录成功"
    )


@router.get("/user/me", response_model=DataResponse)
async def read_users_me(current_user: UserInDb = Depends(get_current_user)):
    """获取当前用户信息"""
    user_out = UserOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        is_active=current_user.is_active,
        create_at=current_user.create_at,
    )
    return ResponseFactory.success(data=user_out, msg="获取用户信息成功")
