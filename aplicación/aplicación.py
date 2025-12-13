import asyncio
import asyncpg
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuración de conexión a Neon
DATABASE_URL = "postgresql://neondb_owner:npg_nRaX64fFLPvz@ep-fancy-glade-a44j0e4a-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Ruta raíz
@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "Flask + Neon funcionando"})

# Ruta webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    token = data.get("token")

    print("Evento recibido:", {
        "evento": data,
        "token_presente": bool(token)
    })

    return jsonify({"status": "ok", "evento": data}), 200

# Ruta de prueba de conexión a Neon
@app.route("/dbtest", methods=["GET"])
def dbtest():
    async def run():
        conn = await asyncpg.connect(DATABASE_URL)
        row = await conn.fetchrow("SELECT NOW() as current_time;")
        await conn.close()
        return row["current_time"]

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(run())
    return jsonify({"neon_time": str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



