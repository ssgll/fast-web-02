from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from uuid import UUID


# 系统基础模型
class SystemBase(BaseModel):
    config_name: str
    config_name_cn: str
    config_value: str

# 添加模型
class SystemCreate(SystemBase):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    config_name: str = Field(
        ...,
        description="配置名称",
        examples=["system_name"],
    )
    config_name_cn: str = Field(
        ...,
        description="配置描述",
    )
    config_value: str = Field(
        ...,
        description="配置值",
    )

# 更新模型
class SystemUpdate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    config_name_cn: Optional[str] = None
    config_value: Optional[str] = None

# 删除模型
class SystemDelete(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    config_value: Optional[str] = None

# 查询模型
class SystemOut(SystemBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID = Field(...)