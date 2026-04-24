# Especificacion de implementacion Java (Consola) - ePark

## 1. Objetivo
Implementar en Java una version funcional minima por consola de ePark, enfocada unicamente en estas historias de usuario:
1. HU 7.1 Estacionar un vehiculo en la calle.
2. HU 7.2 Enviar mensaje al usuario cuando faltan 5 minutos para vencer el parqueo.
3. HU 7.3 Visualizar pagos realizados por tarjeta de credito en un dia para un cliente especifico.

## 2. Alcance y limites

### Incluye
- Modelado orientado a objetos con clases cohesionadas.
- Encapsulamiento (atributos privados, metodos publicos).
- Flujo por consola con Scanner, impresiones y menu simple.
- Logica basica para calcular tiempo y cobro.
- Soporte de tipo de vehiculo extensible (incluyendo SCOOTER_ELECTRICO).

### No incluye
- Interfaz grafica.
- Base de datos real.
- API REST.
- Autenticacion o seguridad avanzada.
- Integraciones externas.

## 3. Requisitos funcionales

### RF-7.1 Estacionar vehiculo
- El sistema debe permitir seleccionar usuario, vehiculo y zona.
- Debe registrar hora de inicio y tiempo maximo permitido en zona.
- Debe crear un estacionamiento en estado ACTIVO.
- Al finalizar, debe generar un cobro asociado.

### RF-7.2 Aviso de vencimiento
- El sistema debe evaluar minutos restantes de un estacionamiento ACTIVO.
- Si faltan 5 minutos o menos, debe mostrar aviso por consola.
- El aviso debe incluir id del estacionamiento y tiempo restante.

### RF-7.3 Consulta de pagos por tarjeta
- El sistema debe permitir buscar por idUsuario y fecha.
- Debe mostrar solo cobros con metodo TARJETA_CREDITO.
- Debe listar montos y total del dia para ese usuario.

## 4. Requisitos no funcionales
- Codigo simple, legible y mantenible.
- Sin sobreingenieria.
- Estructura clara para poder extender nuevos tipos de vehiculo.
- Validaciones basicas de entrada de consola.

## 5. Modelo de clases obligatorio
Usar como base la definicion de clases en clases.md.

### Clases
- AppDelUsuario
- Usuario
- Vehiculo
- Estacionamiento (corresponde a Parqueo)
- Cobro
- DetalleCobro
- Municipalidad

### Enums
- TipoVehiculo: CARRO, MOTO, SCOOTER_ELECTRICO
- MetodoPago: TARJETA_CREDITO
- EstadoCobro: PENDIENTE, PAGADO
- EstadoEstacionamiento: ACTIVO, FINALIZADO

## 6. Relaciones UML esperadas
- Usuario 1..* Vehiculo
- Usuario 1..* Cobro
- Estacionamiento 1..1 Cobro
- Cobro 1..1 DetalleCobro
- Municipalidad provee tarifas y limites de tiempo

## 7. Estructura minima de proyecto sugerida

```text
src/
  main/
    java/
      epk/
        Main.java
        app/AppDelUsuario.java
        domain/Usuario.java
        domain/Vehiculo.java
        domain/Estacionamiento.java
        domain/Cobro.java
        domain/DetalleCobro.java
        domain/Municipalidad.java
        enums/TipoVehiculo.java
        enums/MetodoPago.java
        enums/EstadoCobro.java
        enums/EstadoEstacionamiento.java
```

## 8. Flujo de consola obligatorio

Menu principal:
1. Estacionar vehiculo (HU 7.1)
2. Revisar vencimientos (HU 7.2)
3. Ver pagos por tarjeta de un dia (HU 7.3)
4. Salir

## 9. Contratos de metodos minimos

### AppDelUsuario
- iniciarEstacionamiento(placaVehiculo, idZona): Estacionamiento
- mostrarAvisoVencimiento(estacionamiento): void
- mostrarPagosTarjetaPorDia(idUsuario, fecha): List<Cobro>

### Estacionamiento
- iniciar(vehiculo, idZona, horaInicio, minutosPermitidos): void
- minutosRestantes(ahora): long
- estaProximoAVencer(ahora): boolean
- finalizar(horaFinReal): void
- generarCobro(tarifaPorMinuto, metodoPago): Cobro

### Cobro
- calcularMonto(): double
- registrarPago(metodoPago): boolean
- generarComprobante(): String

### Municipalidad
- obtenerTarifaBase(tipoVehiculo): double
- obtenerMinutosPermitidos(idZona): int
- calcularTarifaFinal(vehiculo, minutosConsumidos): double

## 10. Casos de uso detallados

### HU 7.1 Estacionar vehiculo
1. Usuario ingresa placa e idZona.
2. Sistema valida zona y existencia de vehiculo.
3. Sistema crea Estacionamiento ACTIVO con horaInicio.
4. Sistema imprime confirmacion.
5. Cuando usuario finaliza, sistema calcula y registra Cobro PAGADO por TARJETA_CREDITO.

Salida esperada minima:
- "Estacionamiento creado: EST-001"
- "Hora inicio: ..."
- "Tarifa por minuto: ..."
- "Cobro generado: CRC ..."

### HU 7.2 Aviso 5 min
1. Sistema recorre estacionamientos ACTIVO.
2. Para cada uno calcula minutosRestantes.
3. Si <= 5, imprime aviso.

Salida esperada minima:
- "Aviso: El estacionamiento EST-001 vence en 5 minutos."

### HU 7.3 Pagos por tarjeta en un dia
1. Usuario ingresa idUsuario y fecha.
2. Sistema filtra cobros de ese usuario en esa fecha.
3. Mantiene solo metodo TARJETA_CREDITO.
4. Imprime listado y total.

Salida esperada minima:
- "Pagos con tarjeta del usuario U-01 en 2026-04-24"
- lineas de cada cobro
- "Total del dia: CRC ..."

## 11. Criterios de aceptacion
- Las 3 HU se ejecutan desde consola sin errores de compilacion.
- Los objetos reflejan responsabilidades claras.
- No hay logica central metida completamente en Main.
- El modelo soporta agregar SCOOTER_ELECTRICO sin reescribir Cobro completo.
- Coincidencia entre clases, secuencias y comportamiento de consola.

## 12. Pruebas manuales minimas

### Prueba A (HU 7.1)
- Dado un usuario con vehiculo registrado.
- Cuando estaciona en una zona valida.
- Entonces se crea estacionamiento ACTIVO y luego cobro al finalizar.

### Prueba B (HU 7.2)
- Dado un estacionamiento con 5 minutos restantes.
- Cuando se ejecuta revisar vencimientos.
- Entonces aparece aviso de vencimiento.

### Prueba C (HU 7.3)
- Dado cobros mixtos de varios dias y usuarios.
- Cuando se consulta por usuario y fecha.
- Entonces solo se listan pagos con tarjeta de ese usuario en ese dia.

## 13. Prompt listo para IntelliJ AI Assistant
Copiar y pegar tal cual:

"""
Genera un proyecto Java de consola llamado eParkConsola en paquete base epk.
Implementa SOLAMENTE las HU 7.1, 7.2 y 7.3 del contexto de parqueo.
No uses GUI, ni DB, ni API.

Requisitos de dominio:
- Clases: AppDelUsuario, Usuario, Vehiculo, Estacionamiento, Cobro, DetalleCobro, Municipalidad.
- Enums: TipoVehiculo(CARRO, MOTO, SCOOTER_ELECTRICO), MetodoPago(TARJETA_CREDITO), EstadoCobro(PENDIENTE, PAGADO), EstadoEstacionamiento(ACTIVO, FINALIZADO).
- Encapsulamiento completo con atributos privados.
- Cohesion de responsabilidades por clase.

Comportamiento obligatorio:
1) HU 7.1: estacionar vehiculo por consola (placa + zona), registrar hora de inicio, finalizar y generar cobro.
2) HU 7.2: revisar estacionamientos activos y avisar por consola cuando falten 5 minutos o menos.
3) HU 7.3: consultar pagos por tarjeta de credito por usuario y fecha, listar y totalizar.

Detalles tecnicos:
- Usa LocalDate y LocalDateTime para fechas/horas.
- Usa List y Map en memoria como almacenamiento temporal.
- Crea menu de consola con opciones para las 3 HU.
- Incluye datos semilla minimos para probar.
- Evita if gigantes para tipo de vehiculo: usar metodo en Vehiculo para calcular tarifa por minuto a partir de tarifa base.

Entrega codigo compilable y ejecutable con Main.java.
"""
