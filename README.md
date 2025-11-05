# FastAPI User Management System

## 项目介绍
基于 FastAPI 和 Tortoise ORM 构建的用户管理系统，支持用户增删改查功能。

## 环境要求
- Python 3.10+
- MySQL 5.7+

## 安装依赖
```bash
pip install -r requirements.txt
```

或使用 uv:
```bash
uv sync
```

## 环境变量配置
项目使用 `.env` 文件进行配置，主要配置项包括：
- `APP_DEBUG`: 是否为调试模式
- `LOG_LEVEL`: 日志级别 (DEBUG, INFO, WARNING, ERROR)
- `DISABLE_ACCESS_LOG`: 是否禁用访问日志 (true/false)

## 数据库初始化

### 开发环境
在开发环境中，系统会自动创建和更新表结构：
```bash
python init_db.py
```

### 生产环境数据库迁移

#### 初始化Aerich
```bash
aerich init -t app.core.config.TORTOISE_ORM
aerich init-db
```

#### 创建迁移文件
当模型结构发生变化时:
```bash
aerich migrate --name "description of changes"
```

#### 执行迁移
```bash
aerich upgrade
```

## 启动服务
```bash
uvicorn main:app --reload
```

访问 http://localhost:8000/docs 查看 API 文档。