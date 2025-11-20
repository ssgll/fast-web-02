from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_config` ADD `config_name_cn` VARCHAR(128) NOT NULL UNIQUE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_config` DROP INDEX `config_name_cn`;
        ALTER TABLE `sys_config` DROP COLUMN `config_name_cn`;"""


MODELS_STATE = (
    "eJztme1P4jAYwP+VZZ8w8YxM8Ii5XALKnVwELjrujMYsZSujcWvn2qHE+L9fW/bCXphA9I"
    "CEL8Cel63P72n7PB2vqkss6NCjAYV+B18M1TPlVcXAhfxHTneoqMDzEo0QMDB0pDGdUiPg"
    "ltJqSJkPTMblI+BQyEUWpKaPPIYI5lIcOI4QEpMbImwnogCjpwAajNiQjfndzpT7By5G2I"
    "IvkEaX3qMxQtCxUsNFlni2lBts6knZYNC5+CEtxeOGhkmcwMWJtTdlY4Jj8yBA1pHwETob"
    "YugDBq25MMQow4gj0WzEXMD8AMZDtRKBBUcgcAQM9dsowKZgoMgniY/ad3UFPCbBAi3CTL"
    "B4fZtFlcQspap41Pll87pycnogoySU2b5USiLqm3QEDMxcJdcEpPzOoTwfA78YZWSfgckH"
    "ug7GSJBwTOZQBDICtB411QUvhgOxzcb8UqvXSjD+aV5LktxKoiR8Xs8mfC9UaTOdQJoghC"
    "5AzioMY4ePgfj+XNx6hB6g9Jn4ljEGdLwKypzjfl7GUE0f8pANwPJAL7iCIRcWQ005ZoBa"
    "oedR9GNL8fIQrD52puFyKKGrd7rtG73Z/S0icSl9ciShpt4WGk1Kpxlp5TSTiPgmyt+Ofq"
    "mIS+Wu32tnd+TYTr9TxZhAwIiBybMBrLmVG0kjMKm0Bp61XlpTjvu0bjSt4eDnGhpq8CYK"
    "TQqKcYsQBwK8oLWZ98skdcgdPyuPcY356F6m1e9fpVLW6uiZTW/QbbWvK1WZK26EmBR3en"
    "pmAwQT3vX4RuAXVGcdvrBiommvtepJCOc/LoyyhdC+1VNAo6JR6TZvD1Lr4Krf+xmZz/E+"
    "v+q3OFrRjI8e57pIIRgC8/EZ8AKc0xCNLLLNq1zNzUoABrZkJSIW8YVHlCb0kTlWCw4voe"
    "aw7OgCEputObh08IKpWHhu4SnPTsFwvm20SbTFU75o1drXWuPktNbgJnIkseRryRyN1u7i"
    "c8oE+lQMaYXecM5lV7vC+lJdYb2kK6xnu0KxNFaAGJrvJsDq8fESALnVQoBSl2mrCWYQF3"
    "Rfv276vQUNdeKSATnAPMB7C5nsUHEQZQ/bibWEooi6vLxkK0mmdxI32KLycjOlDLpF5SXU"
    "lJYX8WaMsxshe7tKzP7d2BrvxmaJNFZ9RZZx28WXPFWtsczGqTUWb5xCl9s4Iy6GuVIlz3"
    "vuoaahToATrDNJY78dLfCfgZT41uyvjSW79Nj+/Ub9oxgeb7ZR32ipfvsHKCmOtQ=="
)
