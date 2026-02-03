import express from "express";
import dotenv from "dotenv";
import path from "path";

// Cargar .env desde la raíz del proyecto
dotenv.config({
  path: path.resolve(process.cwd(), ".env")
});

const app = express();
app.use(express.json());

// Importar rutas
import brainRoute from "./routes/brain.ts";

// Registrar rutas
brainRoute(app);

// Puerto
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Servidor Nefosys escuchando en puerto ${PORT}`);
});
