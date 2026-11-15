from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from agentlens_backend.infrastructure.database.engine import engine

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)
