import asyncio

from app.core.database import BaseModel, engine


async def create_tables():
    print("Creating database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    print("Database tables created.")


if __name__ == "__main__":
    asyncio.run(create_tables())
