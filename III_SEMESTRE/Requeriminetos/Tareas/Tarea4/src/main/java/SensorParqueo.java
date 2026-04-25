public class SensorParqueo {
    private final long espacioId;
    private boolean ocupado;
    private String placaActual;

    public SensorParqueo(long espacioId) {
        this.espacioId = espacioId;
        this.ocupado = false;
        this.placaActual = "";
    }

    public boolean ingresarVehiculo(Vehiculo vehiculo) {
        if (vehiculo == null || ocupado) {
            return false;
        }
        this.ocupado = true;
        this.placaActual = vehiculo.getPlaca();
        return true;
    }

    public boolean retirarVehiculo(Vehiculo vehiculo) {
        if (vehiculo == null || !ocupado) {
            return false;
        }
        if (!vehiculo.getPlaca().equalsIgnoreCase(placaActual)) {
            return false;
        }
        this.ocupado = false;
        this.placaActual = "";
        return true;
    }

    public long getEspacioId() {
        return espacioId;
    }

    public long getEspacioid() {
        return getEspacioId();
    }

    public boolean isOcupado() {
        return ocupado;
    }

    public String getPlacaActual() {
        return placaActual;
    }
}
