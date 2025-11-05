from loguru import logger
import sys
import logging
import os


# 移除默认的日志处理器
logger.remove()

# 从环境变量获取日志级别，默认为 INFO
log_level = os.getenv("LOG_LEVEL", "INFO")

# 添加控制台日志处理器
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
    level=log_level,
    colorize=True
)

# 添加文件日志处理器
logger.add(
    "logs/app.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
    level=log_level,
    rotation="100 MB",
    retention="30 days"
)

# 根据环境变量控制 uvicorn 的访问日志
disable_access_log = os.getenv("DISABLE_ACCESS_LOG", "true").lower() == "true"

if disable_access_log:
    # 禁用 uvicorn 的访问日志
    logging.getLogger("uvicorn.access").disabled = True
    # 设置 uvicorn 日志级别为 WARNING 或更高，以减少输出
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)