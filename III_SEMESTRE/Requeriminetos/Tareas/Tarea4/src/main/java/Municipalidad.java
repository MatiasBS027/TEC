import java.time.LocalDate;
import java.util.*;


public class Municipalidad {

    private static final HashMap<Long, Usuario> usuarios = new HashMap<>();
    private static final TreeSet<DetalleCobro> cobrosAgrupadoPorUsuario = new TreeSet<>();
    private static final HashMap<Long, DetalleCobro> cobrosOptimizadoPorId = new HashMap<>();
    private static final HashMap<String, Vehiculo> vehiculos = new HashMap<>();
    private static double TARIFA_PARQUEO_POR_HORA = 1000.0;
    private static double TARIFA_MULTA_PARQUEO = 5000.0;
    private static Municipalidad municipalidad;


    private Municipalidad() {

    }

    public static Municipalidad getMunicipalidad(){
        if(municipalidad == null){
            municipalidad = new Municipalidad();
        }
        return municipalidad;
    }

    public static double getTarifaParqueoPorHora() {
        return TARIFA_PARQUEO_POR_HORA;
    }

    public void setTarifaParqueoPorHora(double tarifaParqueoPorHora) {
        TARIFA_PARQUEO_POR_HORA = tarifaParqueoPorHora;
    }

    public static double getTarifaMultaParqueo() {
        return TARIFA_MULTA_PARQUEO;
    }

    public void setTarifaMultaParqueo(double tarifaMultaParqueo) {
        TARIFA_MULTA_PARQUEO = tarifaMultaParqueo;
    }

    /**Agrega un nuevo usuario a la municipalidad, con los datos proporcionados. */
    public static void addUsuario(String nombre, String segundoNombre, String apellido, String segundoApellido, long numeroCedula){

        Municipalidad.usuarios.put(
                numeroCedula,
                new Usuario(
                        nombre,
                        segundoNombre,
                        apellido,
                        segundoApellido,
                        numeroCedula
                )
        );
    }
    /**Retorna un usuario desde la municipalidad, con los datos proporcionados. */
    public static Usuario getUsuarioPorCedula(long numeroCedula){
        return Municipalidad.usuarios.get(numeroCedula);
    }
    /**Elimina un usuario en la municipalidad, con los datos proporcionados. */
    public static Usuario eliminarUsuarioPorCedula(long numeroCedula){
        return Municipalidad.usuarios.remove(numeroCedula);
    }

    public static void addDetalleCobro(double detalleMonto, String nombreMetodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario){
        addDetalleCobro(detalleMonto, MetodoPago.valueOf(nombreMetodoPago), tiempoTranscurridoMinutos, numeroEspacioUtilizado, numeroPlacaVehiculo, numeroCedulaUsuario);
    }

    public static void addDetalleCobro(double detalleMonto, MetodoPago metodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario){

        DetalleCobro detalleCobro = new DetalleCobro(
                cobrosAgrupadoPorUsuario.size(),
                detalleMonto,
                metodoPago,
                tiempoTranscurridoMinutos,
                numeroEspacioUtilizado,
                numeroPlacaVehiculo,
                numeroCedulaUsuario
        );
        Municipalidad.cobrosAgrupadoPorUsuario.add(detalleCobro);
        Municipalidad.cobrosOptimizadoPorId.put(detalleCobro.getId(), detalleCobro);

        Usuario usuario = usuarios.get(numeroCedulaUsuario);
        if (usuario != null) {
            usuario.registrarCobro(detalleCobro);
        }
    }

    /**Agrupa los detalles de cobro por cedula del usuario*/
    private static SortedSet<DetalleCobro> groupDetallesCobroPorUsuario(long numeroCedulaUsuario){
        SortedSet<DetalleCobro> detallesDelUsuario = new TreeSet<>();
        for (DetalleCobro detalleCobro : cobrosAgrupadoPorUsuario) {
            if (detalleCobro.getNumeroCedulaUsuario() == numeroCedulaUsuario) {
                detallesDelUsuario.add(detalleCobro);
            }
        }
        return detallesDelUsuario;
    }
    /**Retorna todos los detalles de cobro pagados por un usuario especificado por numero de cedula*/
    public static List<DetalleCobro> getDetallesCobrosPagadosPorUsuario(long numeroCedulaUsuario){

        return groupDetallesCobroPorUsuario(numeroCedulaUsuario)
                .stream().filter(DetalleCobro::isPagado).toList(); // el :: es para aplicar lambda a cada elemento DetalleCobro del stream

    }


    /**Retorna todos los detalles de cobro pendientes por un usuario especificado por numero de cedula*/
    public static List<DetalleCobro> getDetallesCobrosNoPagadosPorUsuario(long numeroCedulaUsuario){

        return groupDetallesCobroPorUsuario(numeroCedulaUsuario)
                .stream().filter(detalleCobro -> !detalleCobro.isPagado()).toList();

    }

    /**Retorna todos los detalles de cobro por un usuario especificado por numero de cedula*/
    public static List<DetalleCobro> getDetallesCobrosPorUsuario(long numeroCedulaUsuario){

        return new ArrayList<>(groupDetallesCobroPorUsuario(numeroCedulaUsuario));

    }

    public static DetalleCobro getDetalleCobroPorId(long id){
        return cobrosOptimizadoPorId.get(id);
    }

    public static void addVehiculo(String placa, String modelo, String color, Usuario titular){
        Vehiculo vehiculo = new Vehiculo(placa, modelo, color);
        titular.addVehiculo(vehiculo);
        vehiculos.put(placa, vehiculo);
    }

    public static Vehiculo getVehiculoPorPlaca(String placa){
        return vehiculos.get(placa);
    }

    public static Usuario getUsuarioPorPlacaVehiculo(String placa){
        Vehiculo vehiculo = getVehiculoPorPlaca(placa);
        return vehiculo == null ? null : vehiculo.getTitular();
    }

    public static double obtenerTarifaBase(String tipoVehiculo) {
        if (tipoVehiculo == null) {
            return TARIFA_PARQUEO_POR_HORA / 60.0;
        }
        return switch (tipoVehiculo.toUpperCase()) {
            case "MOTO" -> (TARIFA_PARQUEO_POR_HORA / 60.0) * 0.8;
            case "SCOOTER_ELECTRICO" -> (TARIFA_PARQUEO_POR_HORA / 60.0) * 0.6;
            default -> TARIFA_PARQUEO_POR_HORA / 60.0;
        };
    }

    public static int obtenerMinutosPermitidos(String idZona) {
        if (idZona == null || idZona.isBlank()) {
            return 0;
        }
        return 60;
    }

    public static boolean validarZona(String idZona){
        return idZona != null && !idZona.isBlank();
    }

    public static double calcularTarifaFinal(Vehiculo vehiculo, long minutosConsumidos){
        if (vehiculo == null) {
            return 0.0;
        }
        double tarifaBase = obtenerTarifaBase(vehiculo.getTipoVehiculo());
        return vehiculo.calcularTarifaPorMinuto(tarifaBase) * minutosConsumidos;
    }

}