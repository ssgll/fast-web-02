from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_user` ADD `avatar_url` LONGTEXT;
        ALTER TABLE `sys_user` MODIFY COLUMN `create_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `sys_user` DROP COLUMN `avatar_url`;
        ALTER TABLE `sys_user` MODIFY COLUMN `create_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);"""


MODELS_STATE = (
    "eJztl21P2zAQx79KlFdFYghKyxCaJrXQjU60mSDdEAhFbuymFokdYgeoEN99tptHN81oxU"
    "aReAPN/+5i3+/s+PxkBhQin+2MGIr65GRsHhlPJgEBEj8WbNuGCcIwt0iBg7GvnNmMObHw"
    "VF5jxiPgcqFPgM+QkCBiboRDjikRKol9X4rUFY6YeLkUE3wXI4dTD/GpeNuRcX0jZEwgek"
    "QsfQxvnQlGPixNF0M5ttIdPguVNhr1T74pTznc2HGpHwck9w5nfEpJ5h7HGO7IGGnzEEER"
    "4AgW0pCzTDJOpfmMhcCjGGVThbkA0QTEvoRhfpnExJUMDDWS/NP6aq6Ax6VEosWESxZPz/"
    "Os8pyVasqhjk875439gy2VJWXci5RRETGfVSDgYB6quOYg1f8FlMdTEFWjTP01mGKi62BM"
    "hZxjvoZSkCmg9aiZAXh0fEQ8PhWPzXarBuOvzrkiKbwUSirW9XzBDxNTc26TSHOEKADYX4"
    "VhFvA6EP++FjceYQgYe6ARdKaATVdBuRD4sS4zqG6ERMoO4ItAT4SB4wBVQy0FakBhErmT"
    "/thQvCIFaBF/lmyHGrp2f9C7sDuDnzKTgLE7XxHq2D1paSp1pqmNA60Q2UuM33371JCPxp"
    "U17Olf5MzPvjLlnEDMqUPogwNgYeemagqmVNY4hOuVtRT4UdY3LWsy+UJDwxzRROH7isO4"
    "S6mPAFnS2hTjtKKOReC/qmN2xrx2L9O1rLNSybp9W/vojQbd3nljT9VKOGGu5P7Q1j6A4F"
    "50PZETRxWns40eeTXRctRa50kC5z9ujLqN0Lu0S0DTQ6Mx6FxulfbBmTX8nroXeB+fWV2B"
    "Vjbjk9tCFymFMXBvH4A4gBcstEmX+S6agmagK4AAT7GSGcv8kitKB0XYnZoVl5fEsl13dQ"
    "G5z8ZcXPpkyVKsvLeIkutLMFlvb9okenKUT8291ufW4f5B61C4qJlkyueaNZru3eX3lHsU"
    "MTmlFXrDQsh77QrbL+oK2zVdYVvvCuXWWAFi4v4+Ae7t7r4AoPBaClDZtLaaEo5IRff148"
    "IaLmmo8xAN5IiIBK8hdvm24WPGbzYTaw1FmXX98aKfJFrvJF/w5sfL8x+Q7Bpr"
)
