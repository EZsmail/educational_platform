from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default="postgresql+asyncpg://admin:root@0.0.0.0:5438/postgres"
)