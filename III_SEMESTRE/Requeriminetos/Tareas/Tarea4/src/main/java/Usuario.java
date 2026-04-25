import java.util.ArrayList;
import java.time.LocalDate;
import java.util.List;

public class Usuario{

    private final String nombre;
    private final String segundoNombre;
    private final String apellido;
    private final String segundoApellido;
    private final long numeroCedula;
    private final List<Vehiculo> vehiculos = new ArrayList<>();
    private final List<DetalleCobro> cobros = new ArrayList<>();

    public Usuario(String nombre, String segundoNombre, String apellido, String segundoApellido, long numeroCedula) {
        this.nombre = nombre;
        this.segundoNombre = segundoNombre;
        this.apellido = apellido;
        this.segundoApellido = segundoApellido;
        this.numeroCedula = numeroCedula;
    }


    public void addVehiculo(Vehiculo vehiculo) {
        if (vehiculo == null) {
            return;
        }
        this.vehiculos.add(vehiculo);
        vehiculo.setTitular(this);
    }

    public void registrarVehiculo(Vehiculo vehiculo) {
        addVehiculo(vehiculo);
    }

    public Vehiculo obtenerVehiculoPorPlaca(String placa) {
        if (placa == null) {
            return null;
        }
        return vehiculos.stream()
                .filter(vehiculo -> placa.equalsIgnoreCase(vehiculo.getPlaca()))
                .findFirst()
                .orElse(null);
    }

    public void registrarCobro(DetalleCobro cobro) {
        if (cobro == null) {
            return;
        }
        cobros.add(cobro);
    }

    public List<DetalleCobro> obtenerCobrosPorDia(LocalDate fecha) {
        if (fecha == null) {
            return List.of();
        }
        return cobros.stream()
                .filter(cobro -> fecha.equals(cobro.getFechaGeneracion()))
                .toList();
    }

    public List<DetalleCobro> obtenerCobrosTarjetaPorDia(LocalDate fecha) {
        if (fecha == null) {
            return List.of();
        }
        return cobros.stream()
                .filter(cobro -> fecha.equals(cobro.getFechaGeneracion()))
                .filter(cobro -> MetodoPago.TARJETA_CREDITO.obtenerNombre().equals(cobro.getNombreMetodoPago()))
                .toList();
    }

    public List<Vehiculo> getVehiculos() {
        return List.copyOf(vehiculos);
    }

    public List<DetalleCobro> getCobros() {
        return List.copyOf(cobros);
    }


    public long getNumeroCedula() {
        return numeroCedula;
    }

    public String getSegundoApellido() {
        return segundoApellido;
    }

    public String getApellido() {
        return apellido;
    }

    public String getSegundoNombre() {
        return segundoNombre;
    }

    public String getNombre() {
        return nombre;
    }

    public String getIdUsuario() {
        return String.valueOf(numeroCedula);
    }

}
