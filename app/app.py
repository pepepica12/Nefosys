import asyncio
import asyncpg
from flask import Flask, request, jsonify

app = Flask(__name__)

# URL de conexión a Neon (ajusta usuario/contraseña/host según tu panel de Neon)
DATABASE_URL = "postgresql://usuario:contraseña@ep-neonhost.neon.tech/nefosys"

# Inicializar la base de datos
async def init_db():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            ip TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    await conn.close()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    email = data.get("email")
    ip_publica = request.remote_addr

    async def insert_user():
        conn = await asyncpg.connect(DATABASE_URL)
        try:
            await conn.execute("INSERT INTO usuarios (email, ip) VALUES ($1, $2)", email, ip_publica)
            await conn.close()
            return {"status": "ok", "email": email, "ip": ip_publica}
        except Exception as e:
            await conn.close()
            return {"status": "error", "detail": str(e)}

    result = asyncio.run(insert_user())
    return jsonify(result)

if __name__ == "__main__":
    asyncio.run(init_db())
    app.run(debug=True)
