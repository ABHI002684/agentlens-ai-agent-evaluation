from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from agentlens_backend.infrastructure.database.session import AsyncSessionLocal

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session