#!/usr/bin/env bash
set -euo pipefail

# Configuración inicial (solo la primera vez)
git config --global user.name "pepepica12"
git config --global user.email "tu_correo@ejemplo.com"

# Mensaje de commit dinámico con fecha/hora
MSG="Update Nefosys backend $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "[+] Agregando todos los archivos..."
git add .

echo "[+] Creando commit..."
git commit -m "$MSG" || echo "No hay cambios nuevos para commitear."

echo "[+] Subiendo al remoto..."
git push -u origin main

echo "[✓] Push completo. Revisa GitHub Actions para ver el workflow y artefactos."
