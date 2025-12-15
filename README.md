# Nefosys

Plataforma Neón con integración de base de datos  
Sistema para gestión de compras e inventario  
No está orientado al cliente final, sino a la administración interna  

## Características
- Registro automático de usuarios con IP pública
- Inventario con historial de compras y ventas
- Documentación reproducible para auditoría
- Backend Flask + Neon (PostgreSQL)
- Despliegue en Vercel

## Instalación
```bash
# Clonar el repositorio
git clone https://github.com/pepepica12/nefosys.git
cd nefosys

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (ejemplo)
export DATABASE_URL="postgresql://usuario:password@neon-host/dbname"
export FLASK_APP=app/app.py

# Ejecutar servidor local
flask run
