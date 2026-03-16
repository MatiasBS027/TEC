# Caso de Uso: CU-02 – Reportar ventas para una fecha dada

**Actor Principal:** Auditoría / Administrativo
**Actores Secundarios:** Base de Datos de Transacciones

---

## 1. Resumen

El usuario consulta el historial de movimientos de dinero (cobros a clientes y retiros de caja) realizados en un periodo específico (diario, semanal o mensual) para verificar la contabilidad del local  .

---

## 2. Precondiciones

- Deben existir registros previos de cobros y retiros en la base de datos  .
- El usuario debe tener permisos de **Administrativo** o **Auditoría**  .

---

## 3. Flujo Básico (Happy Path)

1. El usuario solicita la generación de un reporte de ventas.
2. El sistema solicita el rango de fechas [día exacto, semana o mes].
3. El usuario ingresa la fecha o periodo a consultar  .
4. El sistema busca en el historial todos los cobros realizados y los retiros de caja registrados  .
5. El sistema desglosa los productos vendidos con sus respectivos precios y sumas totales  .
6. El sistema muestra el reporte final en pantalla con el balance neto  .

---

## 4. Flujos Alternos / Excepciones

### 4.1 Sin movimientos registrados

  Si en el **paso 4** no se encuentran datos para la fecha seleccionada, el sistema muestra el mensaje: "No existen registros de movimientos para el periodo seleccionado"  .

### 4.2 Discrepancia detectada (Modo Auditoría)

  Si el actor es de **Auditoría**, el sistema resalta automáticamente cualquier diferencia entre el total reportado por el cajero y el historial de cobros almacenado  .

---

## 5. Postcondiciones

- **Éxito:** Se visualiza el reporte detallado sin modificar ningún dato del historial  .
- **Fallo:** El sistema informa que no pudo acceder a la base de datos o que los parámetros de fecha son inválidos  .
