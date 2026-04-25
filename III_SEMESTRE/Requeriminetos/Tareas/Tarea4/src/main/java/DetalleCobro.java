import java.time.LocalDate;

public class DetalleCobro implements Comparable<DetalleCobro>{
    private final long id;
    private final double detalleMonto;
    private final LocalDate fechaGeneracion ;
    private final MetodoPago metodoPago;
    private final double tiempoTranscurridoMinutos;
    private final long numeroEspacioUtilizado;
    private final String numeroPlacaVehiculo;
    private final long numeroCedulaUsuario;
    private boolean pagado = false;

    public DetalleCobro(long id, double detalleMonto, MetodoPago metodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario) {
        this.id = id;
        this.detalleMonto = detalleMonto;
        this.metodoPago = metodoPago;
        this.tiempoTranscurridoMinutos = tiempoTranscurridoMinutos;
        this.numeroEspacioUtilizado = numeroEspacioUtilizado;
        this.numeroPlacaVehiculo = numeroPlacaVehiculo;
        this.numeroCedulaUsuario = numeroCedulaUsuario;
        this.fechaGeneracion = LocalDate.now();
        this.pagado = false;
    }

    public DetalleCobro(long id, double detalleMonto, LocalDate fechaGeneracion, MetodoPago metodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario) {
        this.id = id;
        this.detalleMonto = detalleMonto;
        this.fechaGeneracion = fechaGeneracion;
        this.metodoPago = metodoPago;
        this.tiempoTranscurridoMinutos = tiempoTranscurridoMinutos;
        this.numeroEspacioUtilizado = numeroEspacioUtilizado;
        this.numeroPlacaVehiculo = numeroPlacaVehiculo;
        this.numeroCedulaUsuario = numeroCedulaUsuario;
    }

    public DetalleCobro(long id, double detalleMonto, String nombreMetodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario) {
        this(id, detalleMonto, MetodoPago.valueOf(nombreMetodoPago), tiempoTranscurridoMinutos, numeroEspacioUtilizado, numeroPlacaVehiculo, numeroCedulaUsuario);
    }

    public DetalleCobro(long id, double detalleMonto, LocalDate fechaGeneracion, String nombreMetodoPago, double tiempoTranscurridoMinutos, long numeroEspacioUtilizado, String numeroPlacaVehiculo, long numeroCedulaUsuario) {
        this(id, detalleMonto, fechaGeneracion, MetodoPago.valueOf(nombreMetodoPago), tiempoTranscurridoMinutos, numeroEspacioUtilizado, numeroPlacaVehiculo, numeroCedulaUsuario);
    }

    @Override
    public int compareTo(DetalleCobro otroDetalleCobro) {
        int comparision = Long.compare(this.numeroCedulaUsuario, otroDetalleCobro.getNumeroCedulaUsuario());
        if (comparision == 0) {
            comparision = this.fechaGeneracion.compareTo(otroDetalleCobro.getFechaGeneracion());
        }
        if (comparision == 0){
            comparision = Double.compare(this.detalleMonto, otroDetalleCobro.getDetalleMonto());
        }
        if (comparision == 0){
            comparision = this.numeroPlacaVehiculo.compareTo(otroDetalleCobro.getNumeroPlacaVehiculo());
        }
        if (comparision == 0){
            comparision = Long.compare(this.numeroEspacioUtilizado, otroDetalleCobro.getNumeroEspacioUtilizado());
        }
        if (comparision == 0){
            comparision = Double.compare(this.tiempoTranscurridoMinutos, otroDetalleCobro.getTiempoTranscurridoMinutos());
        }
        if (comparision == 0){
            comparision = this.metodoPago.obtenerNombre().compareTo(otroDetalleCobro.getNombreMetodoPago());
        }
        if (comparision == 0){
            comparision = Long.compare(this.id, otroDetalleCobro.getId());
        }
        return comparision;
    }

    public long getNumeroCedulaUsuario() {
        return numeroCedulaUsuario;
    }

    public boolean isPagado() {
        return pagado;
    }

    public void setPagado() {
        this.pagado = true;
    }

    public double getDetalleMonto() {
        return detalleMonto;
    }

    public LocalDate getFechaGeneracion() {
        return fechaGeneracion;
    }

    public String getNombreMetodoPago() {
        return metodoPago.obtenerNombre();
    }

    public MetodoPago getMetodoPago() {
        return metodoPago;
    }

    public double getTiempoTranscurridoMinutos() {
        return tiempoTranscurridoMinutos;
    }

    public long getNumeroEspacioUtilizado() {
        return numeroEspacioUtilizado;
    }

    public String getNumeroPlacaVehiculo() {
        return numeroPlacaVehiculo;
    }

    public long getId() {
        return id;
    }

    public double calcularSubtotal() {
        return detalleMonto;
    }

    public double calcularImpuesto(double porcentaje) {
        return calcularSubtotal() * porcentaje / 100.0;
    }

    public double calcularTotal() {
        return calcularSubtotal() + calcularImpuesto(13.0);
    }

    public String generarLineaResumen() {
        return "Cobro " + id + " | placa: " + numeroPlacaVehiculo + " | monto: CRC " + calcularTotal();
    }

}
