from typing import Optional, Union

from app.models import SystemInDb
from app.schemas.system import SystemCreate, SystemUpdate, SystemOut
from app.services.cache_service import cache_result, CacheService


class SystemService:
    """系统管理逻辑处理业务类"""

    @staticmethod
    @cache_result("system", expire=300)
    async def get_system_config(config_name: str) -> Union[SystemOut, None]:
        """根据配置名称获取系统配置"""
        system = await SystemInDb.filter(config_name=config_name).first()
        if not system:
            return None

        return SystemOut(
            id=system.id,
            config_name=system.config_name,
            config_name_cn=system.config_name_cn,
            config_value=system.config_value,
        )

    @staticmethod
    @cache_result("systems", expire=300)
    async def get_system_config_page(page: int = 1, page_size: int = 10):
        """分页获取系统配置"""
        systems = await SystemInDb.all().offset((page - 1) * page_size).limit(page_size)
        total = await SystemInDb.all().count()
        systems = [SystemOut(
            id=system.id,
            config_name=system.config_name,
            config_name_cn=system.config_name_cn,
            config_value=system.config_value,
        ) for system in systems]
        return systems, total

    @staticmethod
    async def create_system(create_system: SystemCreate) -> Union[SystemOut, None]:
        """创建系统配置"""
        # 检查配置是否已存在
        exist_system = await SystemInDb.filter(config_name=create_system.config_name).first()
        if exist_system:
            return None

        # 创建新配置
        system = await SystemInDb.create(
            config_name=create_system.config_name,
            config_name_cn=create_system.config_name_cn,
            config_value=create_system.config_value,
        )
        await system.save()

        # 清除系统相关的缓存
        await CacheService.clear_prefix("systems")
        await CacheService.clear_prefix("system")

        return SystemOut(
            id=system.id,
            config_name=system.config_name,
            config_name_cn=system.config_name_cn,
            config_value=system.config_value,
        )

    @staticmethod
    async def update_system_config(config_name: str, update_system: SystemUpdate) -> Union[SystemOut, None]:
        """更新系统配置"""
        system = await SystemInDb.filter(config_name=config_name).first()
        if not system:
            return None

        # 更新字段
        if update_system.config_name_cn is not None:
            system.config_name_cn = update_system.config_name_cn
        if update_system.config_value is not None:
            system.config_value = update_system.config_value

        await system.save()
        # 清除系统相关的缓存
        await CacheService.clear_prefix("systems")
        await CacheService.clear_prefix("system")
        return SystemOut(
            id=system.id,
            config_name=system.config_name,
            config_name_cn=system.config_name_cn,
            config_value=system.config_value,
        )

    @staticmethod
    async def delete_system_config(config_name: str) -> Optional[SystemOut]:
        """删除系统配置"""
        deleted_count = await SystemInDb.filter(config_name=config_name).first()
        if not deleted_count:
            return None
        await deleted_count.delete()
        # 清除系统相关的缓存
        await CacheService.clear_prefix("systems")
        await CacheService.clear_prefix("system")
        return SystemOut(**deleted_count.__dict__) if deleted_count else None
