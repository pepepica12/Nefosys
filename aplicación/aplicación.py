from flask import Flask, request, jsonify
import asyncpg, asyncio, datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask + Neon funcionando"

@app.route("/db")
def db():
    async def fetch_version():
        conn = await asyncpg.connect(
            "postgresql://neondb_owner:npg_nRaX64fFLPvz@ep-fancy-glade-a44j0e4a-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
        )
        version = await conn.fetchval("SELECT version();")
        await conn.close()
        return version

    return asyncio.run(fetch_version())

@app.route("/auditoria")
def auditoria():
    ip = request.remote_addr
    agente = request.headers.get("User-Agent")
    fecha = datetime.datetime.utcnow().isoformat()

    return jsonify({
        "ip": ip,
        "agente": agente,
        "fecha": fecha
    })

if __name__ == "__main__":
    app.run()
