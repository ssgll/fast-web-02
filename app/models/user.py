from uuid import uuid4
from tortoise import fields
from tortoise.models import Model

# 用户数据库模型
class UserInDb(Model):
    id = fields.UUIDField(pk=True, default=uuid4)
    name = fields.CharField(max_length=254)
    email = fields.CharField(max_length=254, unique=True)  # 添加unique约束
    password_hash = fields.CharField(max_length=254)
    create_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(default=True)

    class Meta(Model.Meta):
        table = "sys_user"