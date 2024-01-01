from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
import asyncpg
import settings


async def asyncpg_pool():
    pool = await asyncpg.create_pool("".join(settings.TEST_DATABASE_URL.split("+asyncpg")))
    yield pool
    pool.close()
    


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        
    async def create_user(
        self, name: str, surname: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    async def get_user(
        self, user_id
    ) -> User:
        async with asyncpg_pool.acquire() as connection:
            return await connection.fetch('''SELECT FROM users WHERE user_id = $1;''', user_id)
        
    async def update_user_name(
        self, user_id
    ):
        pass
        