import uvicorn
import os
from app import app

if __name__ == "__main__":
    # 从环境变量获取主机和端口配置
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", 8000))
    debug = os.getenv("APP_DEBUG", "true").lower() == "true"
    
    # 启动应用
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        access_log=False  # 禁用访问日志
    )