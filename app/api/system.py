from typing import Union
from app.services.system_service import SystemService
from app.common.responses import DataResponse, ErrorResponse, PageResponse, ResponseFactory
from app.core.logger import logger
from app.schemas.system import SystemCreate, SystemUpdate

from fastapi import APIRouter

router = APIRouter()


@router.get("/all", response_model=Union[PageResponse, ErrorResponse])
async def get_systems(page: int = 1, page_size: int = 10) -> PageResponse | ErrorResponse:
    """分页获取系统配置"""
    try:
        logger.info("分页获取系统配置")
        system_list, total = await SystemService.get_system_config_page(page, page_size)
        return ResponseFactory.page_success(data=system_list, total=total, page=page, page_size=page_size)
    except Exception as e:
        logger.error("分页获取系统配置失败")
        return ResponseFactory.error(code=500, msg="获取系统配置错误", details=str(e))


@router.post("/", response_model=Union[DataResponse, ErrorResponse])
async def create_system(system: SystemCreate):
    """创建系统配置"""
    try:
        logger.info("创建系统配置")
        created_system = await SystemService.create_system(system)
        if created_system is None:
            return ResponseFactory.error(code=400, msg="配置已存在")
        return ResponseFactory.success(data=created_system)
    except Exception as e:
        logger.error("创建系统配置失败", exc_info=True)
        return ResponseFactory.error(code=500, msg=str(e))


@router.put("/{config_name}", response_model=Union[DataResponse, ErrorResponse])
async def update_system(config_name: str, system: SystemUpdate):
    """更新系统配置"""
    try:
        logger.info("更新系统配置")
        updated_system = await SystemService.update_system_config(config_name, system)
        if updated_system is None:
            return ResponseFactory.error(code=400, msg="配置不存在")
        return ResponseFactory.success(data=updated_system)
    except Exception as e:
        logger.error("更新系统配置失败", exc_info=True)
        return ResponseFactory.error(code=500, msg=str(e))


@router.delete("/{config_name}", response_model=Union[DataResponse, ErrorResponse])
async def delete_system(config_name: str):
    """删除系统配置"""
    try:
        logger.info("删除系统配置")
        deleted = await SystemService.delete_system_config(config_name)
        if not deleted:
            return ResponseFactory.error(code=400, msg="配置不存在")
        return ResponseFactory.success(data=deleted, msg="删除成功")
    except Exception as e:
        logger.error("删除系统配置失败", exc_info=True)
        return ResponseFactory.error(code=500, msg=str(e))


@router.get("/{config_name}", response_model=Union[DataResponse, ErrorResponse])
async def get_system(config_name: str):
    """获取系统配置"""
    try:
        logger.info("获取系统配置")
        system = await SystemService.get_system_config(config_name)
        if system is None:
            return ResponseFactory.error(code=400, msg="配置不存在")
        return ResponseFactory.success(data=system)
    except Exception as e:
        logger.error("获取系统配置失败", exc_info=True)
        return ResponseFactory.error(code=500, msg=str(e))
