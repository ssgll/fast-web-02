from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `sys_config` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `config_name` VARCHAR(128) NOT NULL UNIQUE,
    `config_value` VARCHAR(128) NOT NULL,
    `order` INT NOT NULL DEFAULT 0,
    KEY `idx_sys_config_config__6d6448` (`config_name`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `sys_config`;"""


MODELS_STATE = (
    "eJztmP9P4jAUwP+VZT9h4hmZ4BFzuQSUO7koXHTcGY1ZylpG49bOtUOJ8X+/tuwLG2MC0Q"
    "MSf1H2vmx9n9f2vfZF9yhELjvoMxR0yNlAP9FedAI8JH7M6fY1Hfh+qpECDgauMmYTZoXC"
    "UlkNGA+AzYV8CFyGhAgiZgfY55gSISWh60ohtYUhJk4qCgl+DJHFqYP4SLztRLu7F2JMIH"
    "pGLH70H6whRi7MDBdD+W0lt/jEV7J+v3P2Q1nKzw0sm7qhR1Jrf8JHlCTmYYjhgfSROgcR"
    "FACO4EwYcpRRxLFoOmIh4EGIkqHCVADREISuhKF/G4bElgw09SX5p/ZdXwGPTYlEiwmXLF"
    "5ep1GlMSupLj91et68qhwd76koKeNOoJSKiP6qHAEHU1fFNQWp/s+hPB2BoBhlbJ+DKQa6"
    "DsZYkHJM51AMMga0HjXdA8+Wi4jDR+LRqNdKMP5pXimSwkqhpGJeTyd8N1IZU51EmiJEHs"
    "DuKgwTh/eB+PZc3HqEPmDsiQbQGgE2WgXlnOPnvEyg2gESIVuAzwM9EwqOPVQMNeOYAwoj"
    "z4P4x5biFSHAHnEn0XIooWt2LtvXZvPyt4zEY+zRVYSaZltqDCWd5KSV41wikpdofzvmuS"
    "Yftdtet53fkRM781aXYwIhpxahTxaAMys3lsZgMmkNfbheWjOOn2ndaFqjwc80NMwSTRQe"
    "FxTjFqUuAmRBazPrl0vqQDh+VB6TGvPevUyr17vIpKzVMXObXv+y1b6qVFWuhBHmStzpmr"
    "kNEIxF1xNYYVBQnU30zIuJZr3WqicRnP+4MMoWQvvGzACNi0blsnmzl1kHF73uz9h8hvfp"
    "Ra8l0MpmfPgw00VKwQDYD09AFOA5DTXoItt5lWd4eQkgwFGsZMQyvuiI0kQBtkd6weEl0u"
    "yXHV1AarM1B5cOWTAVC88tIuX5KRjNt402iY78yhejWvtaaxwd1xrCRI0kkXwtmaPx2l18"
    "ThmjgMkhrdAbzrjsaldYX6orrJd0hfV8VyiXxgoQI/PdBFg9PFwCoLBaCFDpcm01JRyRgu"
    "7r13Wvu6ChTl1yIPtEBHgHsc33NRczfr+dWEsoyqjLy0u+kuR6J/mCLSov1xPGkVdUXiJN"
    "aXmRN2OC3RA721ViPu/G1rgbmybSWvWKLOe2i5c8VaOxzMZpNBZvnFI3t3FKLmPghuvwTP"
    "x2tBZ9BFIawOkt/JINZWL/dk/5XgwPN9tTbrSqvP4Do2shRA=="
)
