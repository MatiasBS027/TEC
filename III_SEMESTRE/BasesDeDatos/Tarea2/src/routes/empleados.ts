import { Router } from 'express';
import { getEmpleados, insertEmpleado } from '../controllers/empleadoController';

const router = Router();

// GET  /api/empleados → llama a getEmpleados
router.get('/', getEmpleados);

// POST /api/empleados → llama a insertEmpleado
router.post('/', insertEmpleado);

export default router;