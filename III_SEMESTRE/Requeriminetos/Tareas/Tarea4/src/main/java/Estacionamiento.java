import java.time.LocalDateTime;
import java.time.Duration;

public class Estacionamiento {
    private String idEstacionamiento;
    private Vehiculo vehiculo;
    private String idZona;
    private LocalDateTime horaInicio;
    private LocalDateTime horaFinEstimada;
    private EstadoEstacionamiento estado;
    private LocalDateTime horaFinReal;

    public Estacionamiento(String idEstacionamiento, Vehiculo vehiculo, String idZona,
                           LocalDateTime horaInicio, int minutosPermitidos) {
        this.idEstacionamiento = idEstacionamiento;
        this.vehiculo = vehiculo;
        this.idZona = idZona;
        this.horaInicio = horaInicio;
        this.horaFinEstimada = horaInicio.plusMinutes(minutosPermitidos);
        this.estado = EstadoEstacionamiento.ACTIVO;
        this.horaFinReal = null;
    }

    public void finalizar(LocalDateTime horaFinReal) {
        if (estado != EstadoEstacionamiento.ACTIVO) {
            throw new IllegalStateException("Solo se puede finalizar un estacionamiento ACTIVO");
        }
        this.horaFinReal = horaFinReal;
        this.estado = EstadoEstacionamiento.FINALIZADO;
    }

    public long minutosRestantes(LocalDateTime ahora) {
        if (estado != EstadoEstacionamiento.ACTIVO) return 0;
        if (ahora.isAfter(horaFinEstimada)) return 0;
        return Duration.between(ahora, horaFinEstimada).toMinutes();
    }

    public boolean estaProximoAVencer(LocalDateTime ahora) {
        long restantes = minutosRestantes(ahora);
        return restantes > 0 && restantes <= 5;
    }

    public DetalleCobro generarCobro(MetodoPago metodoPago, Municipalidad municipalidad) {
        if (estado != EstadoEstacionamiento.FINALIZADO || horaFinReal == null) {
            throw new IllegalStateException("El estacionamiento debe estar FINALIZADO para generar cobro");
        }
        long minutosConsumidos = Duration.between(horaInicio, horaFinReal).toMinutes();
        double tarifaBase = municipalidad.obtenerTarifaBase(vehiculo.getTipoVehiculo());
        double tarifaPorMinuto = vehiculo.calcularTarifaPorMinuto(tarifaBase);
        double montoBase = tarifaPorMinuto * minutosConsumidos;
        DetalleCobro detalle = new DetalleCobro(
                System.currentTimeMillis(),
                montoBase,
                metodoPago,
                minutosConsumidos,
                0,
                vehiculo.getPlaca(),
                vehiculo.getTitular().getNumeroCedula()
        );
        return detalle;
    }

    // Getters
    public String getIdEstacionamiento() { return idEstacionamiento; }
    public Vehiculo getVehiculo() { return vehiculo; }
    public String getIdZona() { return idZona; }
    public LocalDateTime getHoraInicio() { return horaInicio; }
    public LocalDateTime getHoraFinEstimada() { return horaFinEstimada; }
    public EstadoEstacionamiento getEstado() { return estado; }
    public LocalDateTime getHoraFinReal() { return horaFinReal; }
}