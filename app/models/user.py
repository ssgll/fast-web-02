from pydantic import EmailStr
from tortoise.fields.base import Field
from datetime import datetime
from uuid import UUID, uuid4
from tortoise import fields
from tortoise.models import Model

# 用户数据库模型
class UserInDb(Model):
    id: Field[UUID] = fields.UUIDField(pk=True, default=uuid4)
    name: Field[str] = fields.CharField(max_length=254)
    email: Field[EmailStr] = fields.CharField(max_length=254, unique=True)  # 添加unique约束
    password_hash: Field[str] = fields.CharField(max_length=254)
    create_at: Field[datetime] = fields.DatetimeField(auto_now_add=True)
    update_at: Field[datetime] = fields.DatetimeField(auto_now=True)
    is_active: Field[bool] = fields.BooleanField(default=True)
    avatar_url:Field[str] = fields.CharField(max_length=254,nullable=True)

    class Meta(Model.Meta):
        table = "sys_user"

    """用户数据库模型"""
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active,
            "avatar_url": self.avatar_url,
            "create_at": str(self.create_at)
        }
