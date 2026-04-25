import java.time.LocalDate;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AppUsuario appUsuario = new AppUsuario();
        SensorParqueo sensorParqueo = new SensorParqueo(1L);
        boolean ejecutando = true;

        while (ejecutando) {
            System.out.println("\n=== ePark Consola ===");
            System.out.println("1. Registrar usuario");
            System.out.println("2. Registrar vehiculo");
            System.out.println("3. Simular cobro rapido");
            System.out.println("4. Ver pagos tarjeta por dia");
            System.out.println("5. Ver estado sensor");
            System.out.println("6. Salir");
            System.out.print("Seleccione una opcion: ");

            String opcion = scanner.nextLine();
            switch (opcion) {
                case "1" -> registrarUsuario(scanner);
                case "2" -> registrarVehiculo(scanner);
                case "3" -> simularCobro(scanner, appUsuario, sensorParqueo);
                case "4" -> verPagosTarjeta(scanner, appUsuario);
                case "5" -> mostrarEstadoSensor(sensorParqueo);
                case "6" -> ejecutando = false;
                default -> System.out.println("Opcion invalida.");
            }
        }

        scanner.close();
        System.out.println("Programa finalizado.");
    }

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

        Municipalidad.addUsuario(nombre, segundoNombre, apellido, segundoApellido, cedula);
        System.out.println("Usuario registrado correctamente.");
    }

    private static void registrarVehiculo(Scanner scanner) {
        System.out.print("Cedula del titular: ");
        long cedula = Long.parseLong(scanner.nextLine());
        Usuario usuario = Municipalidad.getUsuarioPorCedula(cedula);
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

        Municipalidad.addVehiculo(placa, modelo, color, usuario);
        System.out.println("Vehiculo registrado correctamente.");
    }

    private static void simularCobro(Scanner scanner, AppUsuario appUsuario, SensorParqueo sensorParqueo) {
        System.out.print("Cedula del usuario: ");
        long cedula = Long.parseLong(scanner.nextLine());
        Usuario usuario = Municipalidad.getUsuarioPorCedula(cedula);
        if (usuario == null) {
            System.out.println("Usuario no encontrado.");
            return;
        }

        System.out.print("Placa del vehiculo: ");
        String placa = scanner.nextLine();
        Vehiculo vehiculo = Municipalidad.getVehiculoPorPlaca(placa);
        if (vehiculo == null) {
            System.out.println("Vehiculo no encontrado.");
            return;
        }

        if (!sensorParqueo.ingresarVehiculo(vehiculo)) {
            System.out.println("No se pudo ocupar el espacio, ya esta en uso.");
            return;
        }

        System.out.print("Minutos consumidos: ");
        long minutos = Long.parseLong(scanner.nextLine());
        double monto = Municipalidad.calcularTarifaFinal(vehiculo, minutos);
        DetalleCobro detalleCobro = appUsuario.solicitarPago(cedula, monto);

        sensorParqueo.retirarVehiculo(vehiculo);

        if (detalleCobro == null) {
            System.out.println("No se pudo generar el cobro.");
            return;
        }

        GestorCobros gestorCobros = new GestorCobros();
        gestorCobros.registrarPago(detalleCobro, MetodoPago.TARJETA_CREDITO);
        appUsuario.mostrarCobro(detalleCobro);
    }

    private static void verPagosTarjeta(Scanner scanner, AppUsuario appUsuario) {
        System.out.print("Cedula del usuario: ");
        long cedula = Long.parseLong(scanner.nextLine());
        System.out.print("Fecha (AAAA-MM-DD): ");
        LocalDate fecha = LocalDate.parse(scanner.nextLine());

        List<DetalleCobro> cobros = appUsuario.mostrarPagosTarjetaPorDia(cedula, fecha);
        if (cobros.isEmpty()) {
            System.out.println("No hay pagos para esa fecha.");
            return;
        }

        System.out.println("Pagos del dia:");
        for (DetalleCobro cobro : cobros) {
            System.out.println(cobro.generarLineaResumen());
        }
    }

    private static void mostrarEstadoSensor(SensorParqueo sensorParqueo) {
        String estado = sensorParqueo.isOcupado() ? "Ocupado" : "Libre";
        System.out.println("Sensor " + sensorParqueo.getEspacioId() + " -> " + estado);
        if (sensorParqueo.isOcupado()) {
            System.out.println("Placa actual: " + sensorParqueo.getPlacaActual());
        }
    }
}
