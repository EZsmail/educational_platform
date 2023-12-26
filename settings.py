from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default="postgresql+asyncpg://admin:root@0.0.0.0:5438/postgres"
)

TEST_DATABASE_URL = env.str(
    'TEST_DATABASE_URL',
    default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5439/postgres_test"
)