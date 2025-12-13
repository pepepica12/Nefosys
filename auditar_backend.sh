#!/bin/bash
# Script maestro de auditoría para backend Flask + Neon en Vercel
# Corrige errores previos y genera evidencia reproducible

set -e

# === CONFIGURACIÓN ===
PROYECTO_URL="https://TU_PROYECTO.vercel.app"
CONN="postgresql://neondb_owner:TU_PASSWORD@ep-fancy-glade-a44j0e4a-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
CARPETA="auditoría_nefosys"

mkdir -p $CARPETA

echo "[+] Guardando versión de PostgreSQL..."
psql "$CONN" -c "SELECT version();" > $CARPETA/version_neon.txt

echo "[+] Exportando datos de tabla playing_with_neon..."
psql "$CONN" -c "SELECT * FROM playing_with_neon;" > $CARPETA/datos_neon.txt
psql "$CONN" -c "\COPY (SELECT * FROM playing_with_neon) TO '$CARPETA/datos_neon.csv' CSV HEADER"

echo "[+] Consultando endpoint /db en Vercel..."
curl -s $PROYECTO_URL/db > $CARPETA/db.txt

echo "[+] Consultando endpoint /auditoria en Vercel..."
curl -s $PROYECTO_URL/auditoria > $CARPETA/visitante.json

# Validar si visitante.json es JSON válido
if jq . $CARPETA/visitante.json >/dev/null 2>&1; then
    echo "[+] Convirtiendo visitante.json a CSV..."
    jq -r '[.ip, .agente, .fecha] | @csv' $CARPETA/visitante.json >> $CARPETA/visitas.csv
else
    echo "[!] Error: visitante.json no contiene JSON válido. Revisa el deployment en Vercel." >> $CARPETA/error.log
fi

echo "[+] Evidencia guardada en $CARPETA/"
ls -lh $CARPETA
