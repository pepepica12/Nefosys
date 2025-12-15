import json
import asyncio
import asyncpg
from flask import Flask, request

app = Flask(__name__)

# 🔐 Cadena de conexión directa a Neon
DATABASE_URL = "postgresql://neondb_owner:npg_nRaX64fFLPvz@ep-fancy-glade-a44j0e4a-pooler.us-east-1.aws.neon.tech/Nefosys3?sslmode=require&channel_binding=require"

# 🔄 Crear el pool global antes de iniciar Flask
loop = asyncio.get_event_loop()
pool = loop.run_until_complete(
    asyncpg.create_pool(dsn=DATABASE_URL)
)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(insert_event(data))
    return {"status": "ok"}

async def insert_event(data):
    try:
        async with pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO webhook_events (id, title, current_status, token, payload)
                VALUES ($1, $2, $3, $4, $5)
            """,
            data.get("id"),
            data.get("title"),
            data.get("current_status"),
            data.get("token"),
            json.dumps(data))  # 👈 JSON válido para columna JSONB
    except Exception as e:
        print(f"Error al insertar evento: {e}")

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}
