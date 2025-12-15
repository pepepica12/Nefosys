import asyncio
import asyncpg
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cadena real de conexión a Neon (con sslmode=require)
DATABASE_URL = "postgresql://nefosys_owner:3nCw0kYfGfYh@ep-wispy-snowflake-123456.us-east-2.aws.neon.tech/nefosys?sslmode=require"

# Inicialización de la base de datos
async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                email TEXT NOT NULL,
                ip_publica TEXT NOT NULL,
                fecha TIMESTAMP DEFAULT NOW()
            )
        """)
    finally:
        await conn.close()

# Endpoint de registro
@app.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    email = data.get("email")
    ip_publica = request.remote_addr

    async def insert_user():
        conn = await asyncpg.connect(DATABASE_URL)
        try:
            await conn.execute(
                "INSERT INTO usuarios (email, ip_publica) VALUES ($1, $2)",
                email, ip_publica
            )
            return {"status": "ok", "email": email, "ip": ip_publica}
        except Exception as e:
            return {"status": "error", "detail": str(e)}
        finally:
            await conn.close()

    result = asyncio.run(insert_user())
    return jsonify(result)

if __name__ == "__main__":
    asyncio.run(init_db())
