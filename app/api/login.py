from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from app.models.user import UserInDb
from app.schemas.user import UserLogin, UserOut, UserCreate
from app.common.responses import ErrorResponse, ResponseFactory, DataResponse
from app.services.auth_service import AuthService
from app.core import logger
from typing import Union
from app.services import UserService

oauth2_schema: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="login")

router: APIRouter = APIRouter()


async def get_current_user(token: str = Depends(oauth2_schema),) -> UserInDb:
    """获取当前用户"""
    return await AuthService.get_current_user(token)


@router.post("/login", response_model=DataResponse)
async def login(
        user_login: UserLogin
) -> ErrorResponse | DataResponse:
    """用户登录接口"""
    logger.info(f"用户名: {user_login.username}, 密码: {user_login.password}")
    user: UserInDb | bool = await AuthService.authenticate_user(
        email=user_login.username, password=user_login.password
    )
    logger.info(f"用户认证结果: {user}")
    if not isinstance(user, UserInDb):
        return ResponseFactory.error(
            code=status.HTTP_401_UNAUTHORIZED,
            msg=user.get("detail"),
            error_code="AUTH_ERROR",
        )

    # 创建访问令牌
    access_token_expires: timedelta = timedelta(
        minutes=AuthService.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token: str = AuthService.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return ResponseFactory.success(
        data={"access_token": access_token, "token_type": "bearer"}, msg="登录成功"
    )


@router.get("/me", response_model=DataResponse)
async def read_users_me(current_user: UserInDb = Depends(get_current_user)):
    """获取当前用户信息"""

    logger.info(f"当前用户: {current_user.to_dict()}")
    user_out = UserOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        is_active=current_user.is_active,
        create_at=current_user.create_at,
        avatar_url=current_user.avatar_url,
    )
    return ResponseFactory.success(data=user_out, msg="获取用户信息成功")


@router.get("/logout", response_model=Union[DataResponse, ErrorResponse])
async def logout(
        current_user: UserInDb = Depends(get_current_user),
        token: str = Depends(oauth2_schema)
) -> Union[DataResponse, ErrorResponse]:
    """用户登出接口"""
    # 即使移除token失败，也认为登出是成功的
    # 因为客户端销毁token后，即使服务器端没有成功移除，也不会影响安全性
    await AuthService.remove_token(current_user.id,token)
    return ResponseFactory.success(msg="登出成功")


@router.post("/register", response_model=Union[DataResponse, ErrorResponse])
async def register(user_create: UserCreate) -> Union[DataResponse, ErrorResponse]:
    """用户注册接口"""
    try:
        logger.info(f"开始注册用户: {user_create.email}")
        user_out = await UserService.create_user(user_create)
        if not user_out:
            logger.warning(f"用户已存在: {user_create.email}")
            return ResponseFactory.error(code=400, msg="用户已存在")

        logger.info(f"用户注册成功: {user_out.email}")
        return ResponseFactory.success(data=user_out)
    except Exception as e:
        logger.error(f"注册用户失败: {e}")
        return ResponseFactory.error(code=500, msg="注册用户失败", details=str(e))
