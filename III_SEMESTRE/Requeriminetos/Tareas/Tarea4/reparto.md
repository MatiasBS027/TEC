# Reparto del trabajo

Este reparto está pensado para terminar el proyecto sin cambiar el alcance ni agregar clases nuevas por ahora. La idea es que el trabajo quede parejo entre 3 personas y que lo ya hecho sirva como base común.

## Estado actual del proyecto

- El modelo base ya quedó consistente con lógica mínima funcional.
- El archivo Main ya tiene flujo de consola básico para registrar usuario, registrar vehículo, simular cobro y consultar pagos por día.
- SensorParqueo ya tiene comportamiento de ocupación y retiro de vehículo.
- Ya existe diagrama de secuencia de HU 7.1 en el archivo hu1_secuencia.md.

## Persona 1: Modelo base y clases ya existentes

- Revisar y pulir detalles menores de validación en clases ya listas.
- Confirmar coherencia final de nombres de métodos en todo el dominio.
- Apoyar integración final cuando las otras partes estén listas.

## Persona 2: Flujo de consola

- Terminar HU 7.2 en consola: aviso cuando falten 5 minutos o menos.
- Terminar HU 7.3 en consola: salida más clara con total del día.
- Probar flujos de error y entradas inválidas en menú.

## Persona 3: Diagramas y documentación

- Redibujar diagrama de clases final según el código actual.
- Ajustar y validar diagrama de secuencia HU 7.1 (base: hu1_secuencia.md).
- Crear diagramas de secuencia para HU 7.2 y HU 7.3.
- Alinear documentación de entrega con el estado real del proyecto.

## Lo que ya quedó adelantado

- MetodoPago ya pasó de interfaz a enum.
- Usuario ya registra vehículos y cobros.
- Vehiculo ya calcula tarifa base por tipo.
- DetalleCobro ya tiene resumen y cálculo básico.
- AppUsuario y GestorCobros ya tienen comportamiento mínimo.
- Main ya ejecuta flujo básico por consola.
- SensorParqueo ya refleja estado de ocupación.
- HU 7.1 ya tiene base en código y diagrama de secuencia.

## Pendientes para cerrar entrega

- Cerrar HU 7.2 y HU 7.3 al mismo nivel de HU 7.1.
- Completar diagramas que faltan y revisar consistencia final.
- Pasar pruebas manuales básicas de los tres casos de uso antes de entregar.
