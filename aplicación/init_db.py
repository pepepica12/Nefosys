import os, asyncio, asyncpg

DDL = """
CREATE TABLE IF NOT EXISTS webhook_events (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    current_status TEXT NOT NULL,
    token TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
"""

async def main():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL no está definida")
    conn = await asyncpg.connect(dsn=db_url)
    try:
        await conn.execute(DDL)
        print("Tabla 'webhook_events' creada/verificada correctamente.")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
