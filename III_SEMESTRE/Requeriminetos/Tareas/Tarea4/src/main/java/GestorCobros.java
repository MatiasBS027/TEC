public class GestorCobros {

    public double calcularMonto(double tarifaPorMinuto, long minutosConsumidos) {
        return tarifaPorMinuto * minutosConsumidos;
    }

    public boolean registrarPago(DetalleCobro detalleCobro, MetodoPago metodoPago) {
        if (detalleCobro == null || metodoPago == null) {
            return false;
        }
        detalleCobro.setPagado();
        return true;
    }

    public String generarComprobante(DetalleCobro detalleCobro) {
        if (detalleCobro == null) {
            return "";
        }
        return detalleCobro.generarLineaResumen();
    }
}
