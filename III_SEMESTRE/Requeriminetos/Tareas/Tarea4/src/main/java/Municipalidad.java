import java.time.LocalDate;
import java.util.*;
import java.util.stream.Collectors;

public class Municipalidad {

    private static final HashMap<Long, Usuario> usuarios = new HashMap<>();
    private static final TreeSet<DetalleCobro> cobrosAgrupadoPorUsuario = new TreeSet<>();
    private static final HashMap<Long, DetalleCobro> cobrosOptimizadoPorId = new HashMap<>();
    private static final HashMap<String, Vehiculo> vehiculos = new HashMap<>();
    private static final List<Estacionamiento> estacionamientos = new ArrayList<>();

    private static double TARIFA_PARQUEO_POR_HORA = 1000.0;
    private static double TARIFA_MULTA_PARQUEO = 5000.0;

    private static Municipalidad municipalidad;

    private Municipalidad() {}

    public static Municipalidad getMunicipalidad() {
        if (municipalidad == null) {
            municipalidad = new Municipalidad();
        }
        return municipalidad;
    }

    // getters/setters tarifas
    public double getTarifaParqueoPorHora() { return TARIFA_PARQUEO_POR_HORA; }
    public void setTarifaParqueoPorHora(double tarifa) { TARIFA_PARQUEO_POR_HORA = tarifa; }
    public double getTarifaMultaParqueo() { return TARIFA_MULTA_PARQUEO; }
    public void setTarifaMultaParqueo(double tarifa) { TARIFA_MULTA_PARQUEO = tarifa; }

    // Usuarios
    public void addUsuario(String nombre, String segundoNombre, String apellido,
                           String segundoApellido, long numeroCedula) {
        usuarios.put(numeroCedula, new Usuario(nombre, segundoNombre, apellido, segundoApellido, numeroCedula));
    }
    public Usuario getUsuarioPorCedula(long cedula) { return usuarios.get(cedula); }
    public Usuario eliminarUsuarioPorCedula(long cedula) { return usuarios.remove(cedula); }

    // Vehículos
    public void addVehiculo(String placa, String modelo, String color, Usuario titular) {
        Vehiculo vehiculo = new Vehiculo(placa, modelo, color);
        titular.addVehiculo(vehiculo);
        vehiculos.put(placa, vehiculo);
    }
    public Vehiculo getVehiculoPorPlaca(String placa) { return vehiculos.get(placa); }
    public Usuario getUsuarioPorPlacaVehiculo(String placa) {
        Vehiculo v = getVehiculoPorPlaca(placa);
        return v == null ? null : v.getTitular();
    }

    // Detalles de cobro
    public void addDetalleCobro(double monto, String metodoPago, double minutos,
                                long espacioId, String placa, long cedula) {
        addDetalleCobro(monto, MetodoPago.valueOf(metodoPago), minutos, espacioId, placa, cedula);
    }
    public void addDetalleCobro(double monto, MetodoPago metodoPago, double minutos,
                                long espacioId, String placa, long cedula) {
        DetalleCobro dc = new DetalleCobro(cobrosAgrupadoPorUsuario.size(), monto, metodoPago,
                minutos, espacioId, placa, cedula);
        cobrosAgrupadoPorUsuario.add(dc);
        cobrosOptimizadoPorId.put(dc.getId(), dc);
        Usuario u = usuarios.get(cedula);
        if (u != null) u.registrarCobro(dc);
    }
    public void addDetalleCobro(DetalleCobro dc) {
        cobrosAgrupadoPorUsuario.add(dc);
        cobrosOptimizadoPorId.put(dc.getId(), dc);
        Usuario u = usuarios.get(dc.getNumeroCedulaUsuario());
        if (u != null) u.registrarCobro(dc);
    }

    public List<DetalleCobro> getDetallesCobrosPagadosPorUsuario(long cedula) {
        return groupDetallesCobroPorUsuario(cedula).stream().filter(DetalleCobro::isPagado).collect(Collectors.toList());
    }
    public List<DetalleCobro> getDetallesCobrosNoPagadosPorUsuario(long cedula) {
        return groupDetallesCobroPorUsuario(cedula).stream().filter(d -> !d.isPagado()).collect(Collectors.toList());
    }
    public List<DetalleCobro> getDetallesCobrosPorUsuario(long cedula) {
        return new ArrayList<>(groupDetallesCobroPorUsuario(cedula));
    }
    public DetalleCobro getDetalleCobroPorId(long id) { return cobrosOptimizadoPorId.get(id); }
    private SortedSet<DetalleCobro> groupDetallesCobroPorUsuario(long cedula) {
        SortedSet<DetalleCobro> set = new TreeSet<>();
        for (DetalleCobro dc : cobrosAgrupadoPorUsuario) {
            if (dc.getNumeroCedulaUsuario() == cedula) set.add(dc);
        }
        return set;
    }

    // Estacionamientos
    public void registrarEstacionamiento(Estacionamiento e) { estacionamientos.add(e); }
    public List<Estacionamiento> getEstacionamientosActivos() {
        return estacionamientos.stream().filter(e -> e.getEstado() == EstadoEstacionamiento.ACTIVO).collect(Collectors.toList());
    }
    public List<Estacionamiento> getEstacionamientosPorUsuario(long cedula) {
        return estacionamientos.stream()
                .filter(e -> e.getVehiculo().getTitular().getNumeroCedula() == cedula)
                .collect(Collectors.toList());
    }

    
    public double obtenerTarifaBase(String tipoVehiculo) {
        double porHora = TARIFA_PARQUEO_POR_HORA;
        double porMinuto = porHora / 60.0;
        if (tipoVehiculo == null) return porMinuto;
        return switch (tipoVehiculo.toUpperCase()) {
            case "MOTO" -> porMinuto * 0.8;
            case "SCOOTER_ELECTRICO" -> porMinuto * 0.6;
            default -> porMinuto;
        };
    }
    public int obtenerMinutosPermitidos(String idZona) {
        if (idZona == null || idZona.isBlank()) return 0;
        return 60; 
    }
    public boolean validarZona(String idZona) { return idZona != null && !idZona.isBlank(); }
    public double calcularTarifaFinal(Vehiculo v, long minutosConsumidos) {
        if (v == null) return 0;
        double base = obtenerTarifaBase(v.getTipoVehiculo());
        return v.calcularTarifaPorMinuto(base) * minutosConsumidos;
    }
}