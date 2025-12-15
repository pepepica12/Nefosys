# Nefosys


Plataforma Neón con integración de base de datos auditable y API para PinFlo.

Sistema para gestión de compras e inventario, con trazabilidad vía IP para monitoreo de clientes y usuarios de ventas.  
No está orientado al cliente final, sino a la administración y auditoría interna.

## Características
- Registro automático de usuarios con IP pública
- Inventario con historial de compras y ventas
- Documentación reproducible para auditoría
- Backend Flask + Neon (PostgreSQL)
- Despliegue en Vercel



## Instalación
```bash
git clone https://github.com/tuusuario/nefosys.git
cd nefosys
pip install -r requirements.txt
python app/app.py
