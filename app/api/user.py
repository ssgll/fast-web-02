from fastapi import APIRouter
from pydantic import EmailStr
from typing import Union

from app.core import logger
from app.common import *
from app.services import *
from app.schemas import *



router: APIRouter = APIRouter()


# 分页获取用户列表
@router.get("/all", response_model=Union[PageResponse, ErrorResponse])
async def get_users_page(page: int = 1, page_size: int = 10) -> PageResponse | ErrorResponse:
    """分页获取用户列表"""
    try:
        logger.info("开始获取用户列表")
        user_list, total_users = await UserService.get_users_page(page, page_size)
        logger.info(f"查询到 {len(user_list)} 个用户")
        return ResponseFactory.page_success(data=user_list, total=total_users, page=page, page_size=page_size)
    except Exception as e:
        logger.error(f"获取用户列表失败: {e}")
        return ResponseFactory.error(code=500, msg="获取用户列表失败", details=str(e))


# 获取用户列表
@router.get("/", response_model=Union[ListDataResponse, ErrorResponse])
async def get_users() -> Union[ListDataResponse, ErrorResponse]:
    """获取所有用户列表"""
    try:
        logger.info("开始获取用户列表")
        user_list = await UserService.get_all_users()
        logger.info(f"查询到 {len(user_list)} 个用户")
        logger.info("用户列表获取成功")
        return ResponseFactory.list_success(data=user_list)
    except Exception as e:
        logger.error(f"获取用户列表失败: {e}")
        return ResponseFactory.error(code=500, msg="获取用户列表失败", details=str(e))


# 根据邮箱查询用户
@router.get("/{email}", response_model=Union[DataResponse, ErrorResponse])
async def get_user(email: EmailStr) -> Union[DataResponse, ErrorResponse]:
    """获取指定邮箱的用户信息"""
    try:
        logger.info(f"开始查询用户: {email}")
        user_out = await UserService.get_user_by_email(email)
        if user_out:
            logger.info(f"用户查询成功: {email}")
            return ResponseFactory.success(data=user_out)
        logger.warning(f"用户不存在: {email}")
        return ResponseFactory.error(code=404, msg="用户不存在")
    except Exception as e:
        logger.error(f"查询用户失败: {e}")
        return ResponseFactory.error(code=500, msg="查询用户失败", details=str(e))


# 创建用户
@router.post("/", response_model=Union[DataResponse, ErrorResponse])
async def create_user(user_create: UserCreate) -> Union[DataResponse, ErrorResponse]:
    """创建用户"""
    try:
        logger.info(f"开始创建用户: {user_create.email}")
        user_out = await UserService.create_user(user_create)
        if not user_out:
            logger.warning(f"用户已存在: {user_create.email}")
            return ResponseFactory.error(code=400, msg="用户已存在")
        
        logger.info(f"用户创建成功: {user_out.email}")
        return ResponseFactory.success(data=user_out)
    except Exception as e:
        logger.error(f"创建用户失败: {e}")
        return ResponseFactory.error(code=500, msg="创建用户失败", details=str(e))


# 删除用户
@router.delete("/{email}", response_model=Union[DataResponse, ErrorResponse])
async def delete_user(email: EmailStr) -> Union[DataResponse, ErrorResponse]:
    """删除指定邮箱的用户"""
    try:
        logger.info(f"开始删除用户: {email}")
        user_out = await UserService.delete_user_by_email(email)
        if user_out:
            logger.info(f"用户删除成功: {email}")
            return ResponseFactory.success(data=user_out)
        logger.warning(f"用户不存在: {email}")
        return ResponseFactory.error(code=404, msg=f"用户不存在: {email}")
    except Exception as e:
        logger.error(f"删除用户失败: {e}")
        return ResponseFactory.error(code=500, msg="删除用户失败", details=str(e))


# 修改用户
@router.patch("/{email}", response_model=Union[DataResponse, ErrorResponse])
async def update_user(email: EmailStr, user_update: UserUpdate) -> Union[DataResponse, ErrorResponse]:
    """更新指定邮箱的用户信息"""
    try:
        logger.info(f"开始更新用户: {email}")
        user_out: UserOut | None = await UserService.update_user(email, user_update)

        if user_out is None:
            logger.warning(f"用户不存在或邮箱已存在: {email}")
            return ResponseFactory.error(code=404, msg="用户不存在或邮箱已存在")

        logger.info(f"用户更新成功: {email}")
        return ResponseFactory.success(data=user_out)
    except Exception as e:
        logger.error(f"更新用户失败: {e}")
        return ResponseFactory.error(code=500, msg="更新用户失败", details=str(e))