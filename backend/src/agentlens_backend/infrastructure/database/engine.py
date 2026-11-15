from sqlalchemy.ext.asyncio import create_async_engine
from agentlens_backend.core.config import get_settings


settings = get_settings()

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
)
