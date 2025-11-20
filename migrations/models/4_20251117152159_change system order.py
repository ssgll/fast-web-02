from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `sys_config` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `config_name` VARCHAR(128) NOT NULL UNIQUE,
    `config_name_cn` VARCHAR(128) NOT NULL UNIQUE,
    `config_value` VARCHAR(128) NOT NULL,
    `order` INT NOT NULL DEFAULT 0,
    KEY `idx_sys_config_config__6d6448` (`config_name`),
    KEY `idx_sys_config_config__50c35c` (`config_name_cn`)
) CHARACTER SET utf8mb4;
        DROP TABLE IF EXISTS `sys_config`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `sys_config`;"""


MODELS_STATE = (
    "eJztmf9P4jAUwP+VZT9h4hmZ4BFzuQSUO7kIXHTcGY1ZylZG49bi2qHE+L9fW/adbQLRAx"
    "J+UXhftr7Pa/tey6vqEgs69GhAodfBF0P1THlVMXAh/7CgO1RUMJnEGiFgYOhIYzqjhs8t"
    "pdWQMg+YjMtHwKGQiyxITQ9NGCKYS7HvOEJITG6IsB2LfIyefGgwYkM25k87U+4fuBhhC7"
    "5AGn6dPBojBB0rNVxkiXdLucFmEykbDDoXP6SleN3QMInjuzi2nszYmODI3PeRdSR8hM6G"
    "GHqAQSsRhhhlEHEomo+YC5jnw2ioViyw4Aj4joChfhv52BQMFPkm8af2XV0Bj0mwQIswEy"
    "xe3+ZRxTFLqSpedX7ZvK6cnB7IKAlltieVkoj6Jh0BA3NXyTUGKf8voDwfAy8fZWifgckH"
    "ug7GUBBzjOdQCDIEtB411QUvhgOxzcb8q1avlWD807yWJLmVREn4vJ5P+F6g0uY6gTRGCF"
    "2AnFUYRg4fA/H9ubj1CCeA0mfiWcYY0PEqKBcc9/Mygmp6kIdsALYI9IIrGHJhPtSUYwao"
    "FXgehR+2FC8PwepjZxYshxK6eqfbvtGb3d8iEpfSJ0cSauptodGkdJaRVk4ziYgeovzt6J"
    "eK+Krc9Xvt7I4c2el3qhgT8BkxMHk2gJVYuaE0BJNKqz+x1ktrynGf1o2mNRh8oqGhBm+i"
    "0DSnGLcIcSDABa1N0i+T1CF3/Kw8RjXmo3uZVr9/lUpZq6NnNr1Bt9W+rlRlrrgRYlLc6e"
    "mZDRBMedfjGb6XU511+MLyiaa91qonAZz/uDDKFkL7Vk8BDYtGpdu8PUitg6t+72donuB9"
    "ftVvcbSiGR89JrpIIRgC8/EZ8AK8oCEaKbJdVLmam5UADGzJSkQs4guOKE3oIXOs5hxeAs"
    "1h2dEFxDZbc3Dp4IKpmHtu4SnPTsFgvm20SbTFW75o1drXWuPktNbgJnIkkeRryRwN127x"
    "OWUKPSqGtEJvmHDZ1a6wvlRXWC/pCuvZrlAsjRUgBua7CbB6fLwEQG5VCFDqMm01wQzinO"
    "7r102/V9BQxy4ZkAPMA7y3kMkOFQdR9rCdWEsoiqjLy0u2kmR6J/GALSovNzPKoFt0P5bQ"
    "lpYZcUPGGY6QvV2lZn9HtsYd2TyRxqpXZRm3XbzsqWqNZTZQrVG8gQrdwgYacjHMlSr6ou"
    "ceahrqFDj+OpM08tvRQv8ZSIlnzX/iWLJbj+zfb9g/iuHxZhv2jZbst3/wQpFv"
)
