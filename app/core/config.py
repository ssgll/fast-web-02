import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    VERSION: str = "v0.0.1"
    NAME: str = "CRUD demo"
    ADMIN_EMAIL: str = "admin@example.com"
    DATABASE_TYPE: str = "mysql"
    DATABASE_NAME: str = "fast"
    DATABASE_HOST: str = "127.0.0.1"
    DATABASE_PORT: int = 3306
    DATABASE_USERNAME: str = "ssgll"
    DATABASE_PASSWORD: str = "guojian"
    DATABASE_DRIVER: str = "pymysql"
    SECRET_KEY: str = "HM7vYldLbO5HHG"
    DEBUG: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    # minio配置
    MINIO_ENDPOINT: str = "127.0.0.1:9000"
    MINIO_BUCKET_NAME: str = "test"
    MINIO_SECRET_KEY: str = "ssgll"
    MINIO_ACCESS_KEY: str = "ssgll"
    MINIO_USE_SSL: bool = False


    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        extra="allow",
        case_sensitive=False
    )

    @property
    def project_root(self) -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    @property
    def tortoise_orm(self) -> dict:
        # 开发环境自动生成表结构，生产环境需要手动迁移
        generate_schemas = self.DEBUG
        
        return {
            "connections": {
                "localhost": f"{self.DATABASE_TYPE}://{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
            },
            "apps": {
                "models": {
                    "models": ["app.models.user", "aerich.models"],
                    "default_connection": "localhost",
                }
            },
            "use_tz": False,
            "generate_schemas": generate_schemas,
            "echo": self.DEBUG,
        }


config = Config()

# 为Aerich导出配置
TORTOISE_ORM = config.tortoise_orm