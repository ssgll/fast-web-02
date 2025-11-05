import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from uuid import UUID
from typing import Optional


# 用户基础模型
class UserBase(BaseModel):
    name: str
    email: EmailStr

# 用户创建模型
class UserCreate(UserBase):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str = Field(
        ...,
        description="用户名",
        examples=["john_doe"],
        min_length=3,
        max_length=18
    )
    email: EmailStr = Field(
        ...,
        description="邮箱地址",
        examples=["user@example.com"]
    )
    password: str = Field(
        ...,
        description="密码至少包含8个字符",
        min_length=8,
        examples=["StrongPassword12"]
    )
    is_active: bool = Field(
        default=True,
        description="是否激活"
    )

# 用户更新模型
class UserUpdate(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    password: Optional[str] = Field(None, description="密码")
    email: Optional[EmailStr] = Field(None, description="邮箱地址")
    name: Optional[str] = Field(None, description="用户名", min_length=3, max_length=18)
    is_active: Optional[bool] = Field(None, description="是否激活")

# 用户响应模型
class UserOut(UserBase):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: UUID = Field(..., examples=[UUID("6a322238-2134-47ea-8a2c-123456789abc")])
    is_active: bool
    create_at: datetime.datetime