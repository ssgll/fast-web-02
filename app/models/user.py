from tortoise.fields.base import Field
from datetime import datetime
from uuid import UUID, uuid4
from tortoise import fields
from tortoise.models import Model

# 用户数据库模型
class UserInDb(Model):
    id: Field[UUID] = fields.UUIDField(pk=True, default=uuid4)
    name: Field[str] = fields.CharField(max_length=254)
    email: Field[str] = fields.CharField(max_length=254, unique=True)  # 添加unique约束
    password_hash: Field[str] = fields.CharField(max_length=254)
    create_at: Field[datetime] = fields.DatetimeField(auto_now_add=True)
    update_at: Field[datetime] = fields.DatetimeField(auto_now=True)
    is_active: Field[bool] = fields.BooleanField(default=True)
    avatar_url:Field[str] = fields.TextField(null=True)

    class Meta(Model.Meta):
        table = "sys_user"