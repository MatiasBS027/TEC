import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static Municipalidad municipalidad = Municipalidad.getMunicipalidad();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AppUsuario appUsuario = new AppUsuario();
        SensorParqueo sensorParqueo = new SensorParqueo(1L);
        boolean ejecutando = true;

        while (ejecutando) {
            System.out.println("\n___ePark Requerimientos___");
            System.out.println("1. Registrar usuario");
            System.out.println("2. Registrar vehiculo");
            System.out.println("3. Estacionar vehiculo (HU 7.1)");
            System.out.println("4. Ver pagos tarjeta por dia (HU 7.3)");
            System.out.println("5. Revisar vencimientos (HU 7.2)");
            System.out.println("6. Ver estado sensor");
            System.out.println("7. Salir");
            System.out.print("Seleccione una opcion: ");

            String opcion = scanner.nextLine();
            switch (opcion) {
                case "1" -> registrarUsuario(scanner);
                case "2" -> registrarVehiculo(scanner);
                case "3" -> estacionarVehiculo(scanner, appUsuario, sensorParqueo);
                case "4" -> verPagosTarjeta(scanner, appUsuario);
                case "5" -> revisarVencimientos(appUsuario);
                case "6" -> mostrarEstadoSensor(sensorParqueo);
                case "7" -> ejecutando = false;
                default -> System.out.println("Opcion invalida.");
            }
        }
        scanner.close();
        System.out.println("Programa finalizado.");
    }

    // HU 7.1
    private static void estacionarVehiculo(Scanner scanner, AppUsuario appUsuario, SensorParqueo sensorParqueo) {
        System.out.print("Cedula del usuario: ");
        long cedula = Long.parseLong(scanner.nextLine());
        Usuario usuario = municipalidad.getUsuarioPorCedula(cedula);
        if (usuario == null) {
            System.out.println("Usuario no encontrado.");
            return;
        }

        System.out.print("Placa del vehiculo: ");
        String placa = scanner.nextLine();
        Vehiculo vehiculo = municipalidad.getVehiculoPorPlaca(placa);
        if (vehiculo == null || vehiculo.getTitular().getNumeroCedula() != cedula) {
            System.out.println("Vehiculo no pertenece al usuario o no existe.");
            return;
        }

        System.out.print("Zona (ej: Zona_4): ");
        String zona = scanner.nextLine();
        if (!municipalidad.validarZona(zona)) {
            System.out.println("Zona invalida.");
            return;
        }

        if (!sensorParqueo.ingresarVehiculo(vehiculo)) {
            System.out.println("Espacio ocupado, no se puede estacionar.");
            return;
        }

        int minutosPermitidos = municipalidad.obtenerMinutosPermitidos(zona);
        LocalDateTime ahora = LocalDateTime.now();
        String idEst = "EST-" + System.currentTimeMillis();
        Estacionamiento estacionamiento = new Estacionamiento(idEst, vehiculo, zona, ahora, minutosPermitidos);
        municipalidad.registrarEstacionamiento(estacionamiento);

        System.out.println("Estacionamiento creado: " + idEst);
        System.out.println("Hora inicio: " + ahora);
        System.out.println("Minutos permitidos: " + minutosPermitidos);

        System.out.print("Minutos realmente estacionado: ");
        long minutosReales = Long.parseLong(scanner.nextLine());
        LocalDateTime horaFin = ahora.plusMinutes(minutosReales);
        estacionamiento.finalizar(horaFin);

        DetalleCobro detalle = estacionamiento.generarCobro(MetodoPago.TARJETA_CREDITO, municipalidad);
        detalle.setPagado();
        usuario.registrarCobro(detalle);
        municipalidad.addDetalleCobro(detalle);

        sensorParqueo.retirarVehiculo(vehiculo);

        System.out.println("Cobro generado: CRC " + detalle.calcularTotal());
        System.out.println(detalle.generarLineaResumen());
    }

    // HU 7.2
    private static void revisarVencimientos(AppUsuario appUsuario) {
        List<Estacionamiento> activos = municipalidad.getEstacionamientosActivos();
        if (activos.isEmpty()) {
            System.out.println("No hay estacionamientos activos.");
            return;
        }
        LocalDateTime ahora = LocalDateTime.now();
        boolean algunAviso = false;
        for (Estacionamiento e : activos) {
            if (e.estaProximoAVencer(ahora)) {
                long restantes = e.minutosRestantes(ahora);
                appUsuario.mostrarAvisoVencimiento(e.getIdEstacionamiento(), restantes);
                algunAviso = true;
            }
        }
        if (!algunAviso) {
            System.out.println("Ningun estacionamiento esta próximo a vencer (faltan mas de 5 min).");
        }
    }

    // HU 7.3
    private static void verPagosTarjeta(Scanner scanner, AppUsuario appUsuario) {
        try {
            System.out.print("Cedula del usuario: ");
            long cedula = Long.parseLong(scanner.nextLine());
            System.out.print("Fecha (AAAA-MM-DD): ");
            LocalDate fecha = LocalDate.parse(scanner.nextLine());

            List<DetalleCobro> cobros = appUsuario.mostrarPagosTarjetaPorDia(cedula, fecha);
            if (cobros.isEmpty()) {
                System.out.println("\n[!] No se encontraron pagos con tarjeta para el " + fecha);
                return;
            }

            System.out.println("\n______________________________________");
            System.out.println("Reporte De Pagos - Cliente: " + cedula);
            System.out.println("Fecha: " + fecha);
            System.out.println("________________________________________");
            double total = 0;
            for (DetalleCobro c : cobros) {
                System.out.println(c.generarLineaResumen());
                total += c.calcularTotal();
            }
            System.out.println("________________________________________");
            System.out.printf("Total Pagado en el dia: CRC %.2f\n", total);
            System.out.println("________________________________________");
        } catch (Exception e) {
            System.out.println("Error: Formato de datos incorrecto.");
        }
    }

    // Registros
    private static void registrarUsuario(Scanner scanner) {
        System.out.print("Cedula (numero): ");
        long cedula = Long.parseLong(scanner.nextLine());
        System.out.print("Nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Segundo nombre (opcional): ");
        String segundoNombre = scanner.nextLine();
        System.out.print("Apellido: ");
        String apellido = scanner.nextLine();
        System.out.print("Segundo apellido (opcional): ");
        String segundoApellido = scanner.nextLine();
        municipalidad.addUsuario(nombre, segundoNombre, apellido, segundoApellido, cedula);
        System.out.println("Usuario registrado correctamente.");
    }

    private static void registrarVehiculo(Scanner scanner) {
        System.out.print("Cedula del titular: ");
        long cedula = Long.parseLong(scanner.nextLine());
        Usuario usuario = municipalidad.getUsuarioPorCedula(cedula);
        if (usuario == null) {
            System.out.println("No existe un usuario con esa cedula.");
            return;
        }
        System.out.print("Placa: ");
        String placa = scanner.nextLine();
        System.out.print("Modelo: ");
        String modelo = scanner.nextLine();
        System.out.print("Color: ");
        String color = scanner.nextLine();
        System.out.print("Tipo (CARRO, MOTO, SCOOTER_ELECTRICO): ");
        String tipo = scanner.nextLine().toUpperCase();
        Vehiculo vehiculo = new Vehiculo(placa, modelo, color, tipo);
        usuario.addVehiculo(vehiculo);
        municipalidad.addVehiculo(placa, modelo, color, usuario);
        System.out.println("Vehiculo registrado correctamente.");
    }

    private static void mostrarEstadoSensor(SensorParqueo sensorParqueo) {
        String estado = sensorParqueo.isOcupado() ? "Ocupado" : "Libre";
        System.out.println("Sensor " + sensorParqueo.getEspacioId() + " -> " + estado);
        if (sensorParqueo.isOcupado()) {
            System.out.println("Placa actual: " + sensorParqueo.getPlacaActual());
        }
    }
}