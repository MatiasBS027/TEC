public class Vehiculo {
    private final String placa;
    private Usuario titular;
    private String modelo;
    private String color;
    private String tipoVehiculo;

    public Vehiculo(String placa, String modelo, String color) {
        this(placa, modelo, color, "CARRO");
    }

    public Vehiculo(String placa, String modelo, String color, String tipoVehiculo) {
        this.placa = placa;
        this.color = color;
        this.modelo = modelo;
        this.tipoVehiculo = tipoVehiculo;
    }

    public String getPlaca() {
        return placa;
    }

    public void setTitular(Usuario titular) {
        this.titular = titular;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public Usuario getTitular() {
        return titular;
    }

    public String getModelo() {
        return modelo;
    }

    public String getTipoVehiculo() {
        return tipoVehiculo;
    }

    public void setTipoVehiculo(String tipoVehiculo) {
        this.tipoVehiculo = tipoVehiculo;
    }

    public double calcularTarifaPorMinuto(double tarifaBase) {
        if (tipoVehiculo == null) {
            return tarifaBase;
        }
        return switch (tipoVehiculo.toUpperCase()) {
            case "MOTO" -> tarifaBase * 0.8;
            case "SCOOTER_ELECTRICO" -> tarifaBase * 0.6;
            default -> tarifaBase;
        };
    }

    public boolean validarPlaca() {
        return placa != null && !placa.isBlank();
    }

    public String obtenerDescripcion() {
        return tipoVehiculo + " " + modelo + " " + placa;
    }
}
