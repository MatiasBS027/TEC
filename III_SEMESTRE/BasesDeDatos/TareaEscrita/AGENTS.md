# AGENTS - Guia Operativa y Docente para el SP Batch de Vacaciones

## 1) Proposito de este documento

Este archivo define como debe trabajar el agente y como debe estudiar el equipo para construir un Stored Procedure batch funcional en SQL Server, partiendo de un modelo fisico incompleto (captura + enunciado).

Objetivo academico:

- Resolver la tarea actual.

- Entrenar criterio para examenes futuros con problemas similares.

Objetivo tecnico:

- Implementar un SP diario de vacaciones que cumpla todos los puntos del enunciado (a-g) con trazabilidad y consistencia.

## 2) Contexto de trabajo

Archivos base del workspace:

- SPEC.md: requerimientos funcionales.

- SP.sql: intento inicial parcial.

- SP1.sql: plantilla explicada para construir la version final.

Condicion relevante:

- No hay modelo fisico completo documentado; solo una captura de tablas/relaciones.

## 3) Lo que ya se pudo leer de la captura

Estas piezas ya deben asumirse como base de trabajo, salvo que el usuario corrija algo:

1. SolicitudVacaciones contiene al menos: id, idEmpleado, idSupervisor, FechaSolicitud, FechaDesde, FechaHasta, EstadoSolicitud, QDiasSolicitados, SaldoDiasSolicitado, idUserPostByUbie y PostInIP.
2. Empleado contiene al menos: id, idPuesto, Nombre, FechaContratacion, SaldoVacaciones, emailbit, EsActivo y PostIn.
3. MovimientoVac contiene al menos: id, idEmpleado, idTipoMovimientos, idTextoEmail, Fecha, Monto, EsInvisible, NuevoSaldo, idPostByUser y PostInIP.
4. Email contiene al menos: id, idEmpleado y Texto.
5. MovDebitoXSolicitud contiene al menos: idMovimiento e idSolicitud.
6. TipoMovimiento existe, pero no es el centro del SP si el profesor no lo exige como dependencia obligatoria.
7. EventLog parece ser la bitacora conceptual minima de la corrida.

## 4) Decisiones ya acordadas (fuente usuario)

1. Motor: SQL Server (T-SQL).
2. Tabla/nombres base: usar nombres de la captura (MovimientoVac, MovDebitoXSolicitud, Email, etc.) y ajustar si hay diferencias reales.
3. Unidad de debito: 1 dia por ejecucion valida.
4. Aprobadas: validar ambos criterios por seguridad (EstadoSolicitud = Aprobado y campo de cantidad solicitado no nulo).
5. Feriado: interpretacion por empleado (si aplica, ese empleado no se debita y el proceso continua con otros).
6. Email: texto fiel al enunciado.
7. Campo correcto de saldo de solicitud: SaldoDiasSolicitado.
8. Estado de aprobacion confirmado: EstadoSolicitud = 'Aprobado'.
9. Archivo de trabajo didactico: SP1.sql.
10. Estilo de apoyo: explicacion profunda orientada a examen y defensa.

## 5) Ambiguedades que deben quedar explicitas en cualquier entrega

Si no existe certeza, no inventar silenciosamente. Documentar supuestos y razon tecnica.

Ambiguedades principales:

1. Estructura exacta de Bitacora.
2. Nombres y columnas exactas de tabla de debito ligada a solicitud.
3. Regla cuando saldo de solicitud llega a 0 antes de FechaHasta.
4. Regla cuando saldo de empleado llega a 0.
5. Politica de reejecucion mismo dia (idempotencia) en ambiente real.
6. Valor exacto de idTipoMovimientos si la tabla TipoMovimiento termina siendo necesaria.

Regla docente:

- Si el profe no fijo una politica, aplicar una politica conservadora que evite inconsistencia de saldos.

## 6) Principios tecnicos obligatorios

1. Atomicidad: lo de un empleado se procesa completo o no se procesa.
2. Consistencia: no dejar saldos negativos sin regla explicita.
3. Trazabilidad: cada debito debe tener evidencia en movimiento y en relacion solicitud-debito.
4. Determinismo: misma entrada produce misma salida esperada.
5. Claridad de errores: cualquier falla debe dejar registro util.

## 7) Contrato funcional minimo del SP (a-g)

Para cada solicitud aprobada cuyo rango cubre la fecha de operacion:

1. Si fecha de operacion cae en feriado para ese caso, no debitar y terminar para ese empleado.
2. Insertar email con mensaje solicitado.
3. Insertar movimiento.
4. Insertar movimiento-debito ligado a la solicitud.
5. Actualizar saldo de dias en solicitud.
6. Actualizar saldo de vacaciones del empleado.
7. Actualizar bitacora con ultima llave procesada.

## 8) Metodo de implementacion recomendado (sin codigo)

Fase 1 - Entender antes de escribir:

1. Traducir cada punto a-g en una accion de datos concreta (insert/update/control).
2. Dibujar un flujo de proceso por empleado.
3. Definir entradas, salidas y precondiciones.

Fase 1.5 - Traducir el enunciado a una matriz de diseño:

1. Regla de negocio.
2. Tabla afectada.
3. Tipo de operacion.
4. Riesgo si se omite.

Esa matriz es la que manda sobre el SQL.

Fase 2 - Diseñar flujo transaccional:

1. Definir validacion inicial de fecha.
2. Definir conjunto elegible del dia.
3. Definir secuencia exacta de efectos por empleado: mensaje, movimiento, debito, saldos, bitacora.
4. Definir politica de error y rollback.

Fase 3 - Endurecer logica:

1. Agregar defensas contra saldos invalidos.
2. Evitar duplicidades en reejecucion.
3. Confirmar integridad referencial de inserciones encadenadas.
4. Documentar cualquier columna dudosa en el mismo archivo antes de programar.

Fase 4 - Verificar:

1. Pruebas de feriado.
2. Pruebas de fecha normal.
3. Pruebas de saldos limite.
4. Pruebas de reintento.

## 9) Checklist de calidad antes de dar por terminado

1. Cada requisito a-g esta cubierto y trazable.
2. No hay pasos huertanos (insert sin relacion, update sin condicion).
3. No hay saldos negativos si la politica no lo permite.
4. Existe mecanismo de control de corrida (bitacora).
5. Existe manejo de error consistente.
6. La explicacion funcional coincide con lo implementado.
7. Cada columna dudosa queda documentada como supuesto o confirmada por la captura.

## 10) Checklist de defensa oral (estilo examen)

Preguntas que el equipo debe poder responder con seguridad:

1. Por que ese orden de operaciones?
2. Que pasa si falla a mitad del proceso?
3. Como garantizan que no hay doble debito?
4. Como prueban que un feriado no afecta indebidamente a otros casos?
5. Como evidencian que un movimiento esta ligado a la solicitud correcta?
6. Que supuestos hicieron por falta de modelo y por que son razonables?
7. Por que usaron una politica conservadora para saldos e idempotencia?

## 11) Estrategia didactica para aprender de verdad

1. Primero explicar el flujo en lenguaje de negocio (sin SQL).
2. Luego mapear cada accion a una tabla.
3. Luego definir validaciones de borde.
4. Solo al final traducir a sentencias.

Regla de oro:

- Si no puedes explicar el flujo sin codigo, aun no estas listo para codificar.

## 12) Politica de trabajo del agente en este repo

1. Priorizar explicacion sobre velocidad.
2. No asumir columnas invisibles sin declararlo.
3. Marcar explicitamente TODO supuesto.
4. Mantener SP.sql como referencia historica y usar SP1.sql como plantilla de estudio y version final editable.
5. Cada cambio debe venir acompanado de justificacion funcional.
6. Si una columna no se ve clara en la captura, detenerse y pedir confirmacion antes de inventarla.

## 13) Proximo paso operativo

El siguiente paso es construir, junto al usuario, el diseno logico del SP en una tabla de 4 columnas y luego llevarlo a pseudocodigo:

- Regla de negocio
- Tabla afectada
- Tipo de operacion
- Riesgo si se omite

Despues de eso, recien se pasa a implementar el SQL en SP1.sql.
