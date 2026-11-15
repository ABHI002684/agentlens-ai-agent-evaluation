import asyncio
from sqlalchemy import text
from agentlens_backend.infrastructure.database.engine import engine

async def test_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1;"))
        value = result.scalar()

        print("Database connection successful!")
        print(f"Query result: {value}")

    await engine.dispose()


asyncio.run(test_connection())