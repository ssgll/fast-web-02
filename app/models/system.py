from tortoise.fields.base import Field
from tortoise import fields
from tortoise.models import Model
from uuid import UUID, uuid4


class SystemInDb(Model):
    id: Field[UUID] = fields.UUIDField(pk=True, default=uuid4, editable=False, description="主键")
    config_name: Field[str] = fields.CharField(unique=True, max_length=128, index=True, null=False, description="配置名称")
    config_name_cn: Field[str] = fields.CharField(unique=True, max_length=128, index=True, null=False, description="配置描述")
    config_value: Field[str] = fields.CharField(max_length=128, null=False, description="配置值")
    required: Field[bool] = fields.BooleanField(default=False)

    class Meta(Model.Meta):
        table = "sys_config"
        ordering = ["id"]