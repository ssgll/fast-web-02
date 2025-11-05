#!/usr/bin/env python3
"""
数据库初始化脚本
用于在开发环境中初始化数据库表结构
"""

import asyncio
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.config import TORTOISE_ORM
from tortoise import Tortoise

async def init_db():
    """初始化数据库"""
    try:
        print("初始化数据库...")
        await Tortoise.init(config=TORTOISE_ORM)
        
        if TORTOISE_ORM.get("generate_schemas", False):
            print("生成数据库表结构...")
            await Tortoise.generate_schemas()
            print("数据库表结构生成完成!")
        else:
            print("数据库连接初始化完成!")
            
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        return False
    finally:
        await Tortoise.close_connections()
        print("数据库连接已关闭")
    
    return True

if __name__ == "__main__":
    result = asyncio.run(init_db())
    sys.exit(0 if result else 1)