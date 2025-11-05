from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `sys_user` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `name` VARCHAR(254) NOT NULL,
    `email` VARCHAR(254) NOT NULL UNIQUE,
    `password_hash` VARCHAR(254) NOT NULL,
    `create_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `update_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `is_active` BOOL NOT NULL DEFAULT 1
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm9P2zAQxr9KlFedxBAtLSA0TWppJzLRFkG6TSAUubGbWDh2iB2gQnz32W7+tG6bUc"
    "REkXgDzXN3ie93Tvw82RGDiPDdEUeJQ7tj+9h6simIkPyxFNuxbBDHZUQJAoyJTuZT7qUy"
    "U2eNuUiAL6Q+AYQjKUHE/QTHAjMqVZoSokTmy0RMg1JKKb5LkSdYgEQo73ZsXd9IGVOIHh"
    "HPL+Nbb4IRgQvLxVA9W+uemMZaG42c7g+dqR439nxG0oiW2fFUhIwW6WmK4a6qUbEAUZQA"
    "geBcG2qVWce5NFuxFESSomKpsBQgmoCUKBj2t0lKfcXA0k9Sf5rf7Q3w+IwqtJgKxeLped"
    "ZV2bNWbfWok9P2RW3/4IvuknERJDqoidjPuhAIMCvVXEuQ+v8SypMQJKtR5vkGTLnQ12DM"
    "hZJjuYdykDmg11GzI/DoEUQDEcrLRqtZgfFX+0KTlFkaJZP7erbhB1moMYsppCVCFAFMNm"
    "FYFLwNxH/vxa1HGAPOH1gCvRDwcBOUS4Wf+7KA6idItuwBsQy0KwMCR2g11IVCAyjMKnfz"
    "H1uKV7YAh5RMs9ehgq7r9HuXbrt/rjqJOL8jmlDb7alIQ6tTQ60dGIMobmL9dtxTS11aV8"
    "NBz/wiF3nula3WBFLBPMoePADn3txcLRdfTjWN4eumulD4OdXtmirmnvRQ+H7FWdxhjCBA"
    "1zib+TpjqGNZ+L/mWBwxb21lOsPh2cLIOo5rfPNG/U7volbXs5JJWGjZGbjy+6cM4+R2zu"
    "koYQz82wcgD4mlCGuwdbnLoagRmQqgINCEVJ+qq8xGt1GC/dBeYbCzSKW9BmXO1phrh4oN"
    "vLUctLnzsh3zrkYmUE/52qg3D5tH+wfNI5miV1IohxU7c7bBqrz0PUq4WtIG/mWu5KM6l9"
    "aLnEurwrm0TOeiXo0NIGbpHxNgfW/vBQBl1lqAOmZYP0YFoissws/L4WCN6StLDJAjKhu8"
    "htgXOxbBXNxsJ9YKiqrrhUMlh1frt/+YXE/Ohh3zgFc36Lz38fL8FxQHq2g="
)
