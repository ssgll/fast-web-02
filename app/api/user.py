from fastapi import APIRouter, File, UploadFile, status
from pydantic import EmailStr
from typing import Union, Annotated, Optional

from urllib3.exceptions import NewConnectionError

from app.core import logger
from app.common import *
from app.models.user import UserInDb
from app.schemas.user import UserFilter
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

        logger.info(f"查询到 {total_users} 个用户")
        return ResponseFactory.page_success(data=user_list, total=total_users, page=page, page_size=page_size)
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

# 多条件联合搜索
@router.post("/",response_model=Union[PageResponse, ErrorResponse])
async def search_users(user_filter:UserFilter,page:Optional[int]=1, page_size:Optional[int]=15) -> Union[PageResponse, ErrorResponse]:
    """多条件联合搜索用户"""
    try:
        logger.info("开始多条件联合搜索用户")
        user_list,total_users = await UserService.get_user_by_union(user_filter, page, page_size)
        logger.info(f"查询到 {total_users} 个用户")
        return ResponseFactory.page_success(data=user_list, total=total_users, page=page, page_size=page_size)
    except Exception as e:
        logger.error(f"多条件联合搜索用户失败: {e}")
        return ResponseFactory.error(code=500, msg="多条件联合搜索用户失败", details=str(e))

@router.delete("/batch", response_model=Union[DataResponse, ErrorResponse])
async def delete_users_batch(emails: list[EmailStr]) -> Union[DataResponse, ErrorResponse]:
    """批量删除用户"""
    try:
        logger.info(f"开始批量删除用户: {emails}")
        deleted_count = await UserService.batch_delete_users(emails)
        logger.info(f"用户批量删除成功: {emails}")
        return ResponseFactory.success(data={"deleted_count": deleted_count})
    except Exception as e:
        logger.error(f"批量删除用户失败: {e}")
        return ResponseFactory.error(code=500, msg="批量删除用户失败", details=str(e))

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


@router.post("/{email}/avatar", response_model=Union[DataResponse, ErrorResponse])
async def upload_avatar_endpoint(email: Annotated[str,EmailStr], file: UploadFile = File(...)) -> DataResponse | ErrorResponse:
    """上传用户头像"""
    try:

        user_in_db = await UserInDb.filter(email=email).get_or_none()
        if not user_in_db:
            return ResponseFactory.error(code=404, msg="用户不存在", details="user not in db")

        logger.info(f"开始上传用户头像: {email}")
        avatar_url = await UserService.upload_user_avatar(user_in_db.id, file)

        if not avatar_url:
            logger.error(f"用户头像上传失败")
            return ResponseFactory.error(code=status.HTTP_201_CREATED, msg="用户头像格式错误")

        # 返回更新后的用户信息

        user = UserOut(
            id=user_in_db.id,
            email=user_in_db.email,
            name=user_in_db.name,
            is_active=user_in_db.is_active,
            create_at=user_in_db.create_at,
            avatar_url=user_in_db.avatar_url
        )
        logger.info(f"用户头像上传成功: {email}")
        return ResponseFactory.success(data=user)
    except NewConnectionError as e:
        logger.error(f"附件服务器无法连接: {e}")
        return ResponseFactory.error(code=500, msg="附件服务器无法连接", details=str(e))
    except Exception as e:
        logger.error(f"更新用户头像失败: {e}")
        return ResponseFactory.error(code=500, msg="更新用户头像失败", details=str(e))
