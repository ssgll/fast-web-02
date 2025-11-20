from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_user` MODIFY COLUMN `avatar_url` VARCHAR(254) NOT NULL;
        ALTER TABLE `sys_user` MODIFY COLUMN `avatar_url` VARCHAR(254) NOT NULL;
        ALTER TABLE `sys_config` ADD `required` BOOL NOT NULL DEFAULT 0;
        ALTER TABLE `sys_config` DROP COLUMN `order`;
        ALTER TABLE `sys_config` MODIFY COLUMN `config_name_cn` VARCHAR(128) NOT NULL COMMENT '配置描述';
        ALTER TABLE `sys_config` MODIFY COLUMN `config_name` VARCHAR(128) NOT NULL COMMENT '配置名称';
        ALTER TABLE `sys_config` MODIFY COLUMN `config_value` VARCHAR(128) NOT NULL COMMENT '配置值';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_user` MODIFY COLUMN `avatar_url` LONGTEXT;
        ALTER TABLE `sys_user` MODIFY COLUMN `avatar_url` LONGTEXT;
        ALTER TABLE `sys_config` ADD `order` INT NOT NULL DEFAULT 0;
        ALTER TABLE `sys_config` DROP COLUMN `required`;
        ALTER TABLE `sys_config` MODIFY COLUMN `config_name_cn` VARCHAR(128) NOT NULL;
        ALTER TABLE `sys_config` MODIFY COLUMN `config_name` VARCHAR(128) NOT NULL;
        ALTER TABLE `sys_config` MODIFY COLUMN `config_value` VARCHAR(128) NOT NULL;"""


MODELS_STATE = (
    "eJztmFtv2jAUgP8KyhOTugpCoLSaJkHLVKYCUwvb1FJFJnHAauLQ2KZFVf/7bJMLMZcS1h"
    "Wq9aVNziX2+Y7tc8yT5vk2dMlhj8Cgic8G2knuScPAg/xhQXeQ08B4nGiEgIKBK43JlJiM"
    "W0qrAaEBsCiXO8AlkItsSKwAjSnyMZdi5rpC6FvcEOFhImIY3TNoUn8I6Yh/7SR3c8vFCN"
    "vwEZLodXxnOgi6dmq6yBZjS7lJp2Mp6/WaZ9+kpRhuYFq+yzycWI+ndOTj2JwxZB8KH6Eb"
    "QgwDQKE9F4aYZRhxJJrNmAtowGA8VTsR2NABzBUwtC8Ow5ZgkJMjiT/GVy0DHsvHAi3CVL"
    "B4ep5FlcQspZoY6vS8dpkvVT7JKH1Ch4FUSiLas3QEFMxcJdcEpPy/gPJ0BILlKCN7BSaf"
    "6DYYI0HCMVlDEcgI0HbUNA88mi7EQzrir3rZWIPxZ+1SkuRWEqXP1/VswbdDlT7TCaQJQu"
    "gB5GZhGDu8DsSX1+LeIxwDQh78wDZHgIyyoFxw/FiXMVQrgDxkE9BFoGdcQZEHl0NNOSpA"
    "7dDzMHrYU7w8BLuD3Wm4HdbQ7TZbjaturfVDROIRcu9KQrVuQ2h0KZ0q0nxFSUT8kdyvZv"
    "c8J15z1512Qz2RY7vutSbmBBj1Tew/mMCe27mRNAKTSisb29ulNeX4kdadpjWc/FxDQ0ze"
    "RKHJkmJc930XAryitZn3U5I64I7/Ko9xjXntXqbe6VykUlZvdpVDr9eqNy7zRZkrboSoFD"
    "fbXeUABBPe9QQmCzJV57TXf15PRAPu3M11jkIwANbdA+BFd0Hj6/4q20WVp3uqBGAwlHhE"
    "kCKC8FpyNSUUeqsuLXPag5euLRybg4YfF5e/v7hofWbA0qDPjsu6PH12dYWZpdTMepNR3H"
    "bai3OWx0XD7rMjpwL7rGwUxPOxU9iMa3rzF/XqBpufW63c/FKnNJMJLdPCW3IOPfcJdaVk"
    "OX1WdfYP9QS4bJsFHfvtuHSpa7pQsvYGcQDvGQrgkrN4bbM17/aGvVbW8vRmzdaedAc1GC"
    "BrtKwzCDVruwKQ2OxNR9DENENDwBOtLr3wLNzpz0ZDMcpnvWgcGdVSxahyEzmTWHK0ZmVG"
    "3fzqsj+BARFTynBCzrm8176+vFFfX17T15fVw1BsjQwQQ/P3CbBYKGxSTQqF1dVE6BYKNo"
    "V4ye8x36867ZW1OnJRQPYwD/DGRhY9yLmI0Nv9xLqGoog6VVQiePlW7bfK9fSiU1d7fvGB"
    "+q7Ly/MfcWuu7Q=="
)
