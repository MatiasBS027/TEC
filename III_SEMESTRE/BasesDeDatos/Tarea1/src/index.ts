import express from 'express';
import { getPool } from './db/connection';

const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Servidor funcionando');
});

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