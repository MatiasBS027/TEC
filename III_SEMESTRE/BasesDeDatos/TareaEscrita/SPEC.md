# DOS. TAREA ESCRITA

Vale por un quiz, se entrega en grupos de tareas programadas.

Procesamiento batch de solicitudes de vacaciones.

Para cada solicitud de vacaciones que estan aprobadas y en la cual la fecha de operación (que es
entrada al SP) está entre las fechadesde y fechaHasta de la solicitud.

a) Si fecha de operación es feriado no debe aplicar débito y termina para ese empleado.
(Ojo se ocupa una tabla de feriados).

b) Insertar email (‘esperamos que ud esta difrutanto de sus vacaciones, aun le faltan 5

dias de vacaciones según su solicitud aprobada, su nuevo saldo de vacaciones de 14
dias).

c) Insertar el movimiento

d) Insertar el movimiento-debito de vacaciones que se liga a la solicitud, insetar en tabla

DebitoSV, según modelo İsico de clase del 26 dseƟembre.

e) Actualizar Solicitud de vacaciones, el saldodias (de la solicitud)

f) Actualizar el saldo de vacaciones del empleado

g) Actualizar bitacora para llevar control de la úlƟma llave procesada.

## Comentarios del profe

- Es un proceso que corre diario, chequea las solicites vigentes segun fecha de proceso, hace el debito e inserta y actualiza tablas

- Unico parametro es la fecha de operacion, y debe tomar en cuenta todas las solicitudes aprobadas cuyo rango de fechas cubre la fecha de operacion
