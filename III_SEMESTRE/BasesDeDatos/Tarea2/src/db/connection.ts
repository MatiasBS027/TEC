import sql from 'mssql';

const dbConfig: sql.config = {
    user: 'sa',
    password: 'Bd1Tarea2025!',
    server: 'localhost',
    port: 1433,
    database: 'EmpleadosDB',
    options: {
    encrypt: false,
    trustServerCertificate: true,
    },
};

let pool: sql.ConnectionPool | null = null;

export async function getPool(): Promise<sql.ConnectionPool> {
    if (pool && pool.connected) {
    return pool;
    }
    pool = await sql.connect(dbConfig);
    console.log('Conexión a SQL Server exitosa');
    return pool;
}

export { sql };

