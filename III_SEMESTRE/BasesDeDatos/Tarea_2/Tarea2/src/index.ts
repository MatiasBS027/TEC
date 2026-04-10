import express from 'express';
import path from 'path';
import { getPool } from './db/connection';
import empleadosRouter from './routes/empleados';

const app = express();
const PORT = 3000;

// Middlewares
app.use(express.json());

// Servir archivos estáticos del frontend
app.use(express.static(path.join(__dirname, '../public')));

// Rutas API
app.use('/api/empleados', empleadosRouter);

// Iniciar servidor
async function startServer(): Promise<void> {
    try {
    await getPool();
    app.listen(PORT, () => {
        console.log(`Servidor corriendo en http://localhost:${PORT}`);
    });
    } catch (error) {
    console.error('Error al conectar a la BD:', error);
    process.exit(1);
    }
}

startServer();