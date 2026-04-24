# Todas las clases que se necesitan

## App Del Usuario

-Atributos-

- idUsuario: String
- usuarioActual: Usuario
- tarifaActual: double

-Metodos-

- solicitarPago(idUsuario, tarifaActual): Cobro
- mostrarCobro(comprobante): void
- iniciarEstacionamiento(placaVehiculo, idZona): Estacionamiento
- mostrarAvisoVencimiento(estacionamiento): void
- mostrarPagosTarjetaPorDia(idUsuario, fecha): List<Cobro>

## Usuario

-Atributos-

- idUsuario: String
- nombreCompleto: String
- correo: String
- telefono: String
- vehiculos: List<Vehiculo>

-Metodos-

- registrarVehiculo(vehiculo): void
- obtenerVehiculoPorPlaca(placa): Vehiculo
- obtenerCobrosPorDia(fecha): List<Cobro>
- obtenerCobrosTarjetaPorDia(fecha): List<Cobro>

## Cobros

-Atributos-

- idCobro: String
- usuario: Usuario
- estacionamiento: Estacionamiento
- metodoPago: MetodoPago
- estado: EstadoCobro
- fechaHoraCobro: LocalDateTime
- montoTotal: double

-Metodos-

- calcularMonto(): double
- registrarPago(metodoPago): boolean
- generarComprobante(): String
- obtenerDetalle(): DetalleCobro

## Parqueo 

-Atributos-

- idEstacionamiento: String
- vehiculo: Vehiculo
- idZona: String
- horaInicio: LocalDateTime
- horaFinEstimada: LocalDateTime
- estado: EstadoEstacionamiento

-Metodos-

- iniciar(vehiculo, idZona, horaInicio, minutosPermitidos): void
- finalizar(horaFinReal): void
- minutosRestantes(ahora): long
- estaProximoAVencer(ahora): boolean
- generarCobro(tarifaPorMinuto, metodoPago): Cobro

## Vehiculo

-Atributos-

- placa: String
- tipo: TipoVehiculo
- usuarioPropietario: Usuario

-Metodos-

- calcularTarifaPorMinuto(tarifaBase): double
- validarPlaca(): boolean
- obtenerDescripcion(): String

## Municipalidad

-Atributos-

- nombre: String
- tarifasBasePorTipo: Map<TipoVehiculo, Double>
- minutosMaximosPorZona: Map<String, Integer>

-Metodos-

- obtenerTarifaBase(tipoVehiculo): double
- obtenerMinutosPermitidos(idZona): int
- validarZona(idZona): boolean
- calcularTarifaFinal(vehiculo, minutosConsumidos): double

## Detalles Cobro

-Atributos-

- idDetalle: String
- cobro: Cobro
- minutosConsumidos: long
- tarifaAplicadaPorMinuto: double
- subtotal: double
- impuesto: double
- total: double

-Metodos-

- calcularSubtotal(): double
- calcularImpuesto(porcentaje): double
- calcularTotal(): double
- generarLineaResumen(): String

## Enums sugeridos

- TipoVehiculo: CARRO, MOTO, SCOOTER_ELECTRICO
- MetodoPago: TARJETA_CREDITO
- EstadoCobro: PENDIENTE, PAGADO
- EstadoEstacionamiento: ACTIVO, FINALIZADO

## Relaciones UML (resumen)

- Usuario 1..* Vehiculo
- Usuario 1..* Cobro
- Estacionamiento 1..1 Cobro
- Cobro 1..1 DetalleCobro
- Municipalidad define reglas/tarifas para Estacionamiento y Cobro

## Cobertura de Historias de Usuario

- HU 7.1 Estacionar un vehiculo en la calle:
iniciarEstacionamiento -> Parqueo.iniciar -> Cobro generado al finalizar
- HU 7.2 Aviso de que faltan 5 min:
Parqueo.estaProximoAVencer -> AppDelUsuario.mostrarAvisoVencimiento
- HU 7.3 Ver pagos por tarjeta en un dia para cliente especifico:
AppDelUsuario.mostrarPagosTarjetaPorDia -> Usuario.obtenerCobrosTarjetaPorDia