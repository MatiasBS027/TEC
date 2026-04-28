import java.time.LocalDate;
import java.util.List;

public class AppUsuario {

    private Usuario usuarioActual;
    private double tarifaActual;

    // Obtener la instancia única de Municipalidad
    private Municipalidad municipalidad = Municipalidad.getMunicipalidad();

    public DetalleCobro solicitarPago(long numeroCedulaUsuario, double tarifaActual, String placa) {
        this.tarifaActual = tarifaActual;
        Usuario usuario = municipalidad.getUsuarioPorCedula(numeroCedulaUsuario);
        if (usuario == null) {
            return null;
        }
        this.usuarioActual = usuario;

        DetalleCobro detalleCobro = new DetalleCobro(
                System.currentTimeMillis(),
                tarifaActual,
                MetodoPago.TARJETA_CREDITO,
                0,
                0,
                placa,
                numeroCedulaUsuario
        );
        usuario.registrarCobro(detalleCobro);
        // También añadirlo a la municipalidad para que quede en las colecciones globales
        municipalidad.addDetalleCobro(detalleCobro);
        return detalleCobro;
    }

    public void mostrarCobro(DetalleCobro comprobante) {
        if (comprobante == null) {
            System.out.println("No hay cobro para mostrar.");
            return;
        }
        System.out.println(comprobante.generarLineaResumen());
    }

    public List<DetalleCobro> mostrarPagosTarjetaPorDia(long numeroCedulaUsuario, LocalDate fecha) {
        Usuario usuario = municipalidad.getUsuarioPorCedula(numeroCedulaUsuario);
        if (usuario == null) {
            return List.of();
        }
        return usuario.obtenerCobrosTarjetaPorDia(fecha);
    }

    public void mostrarAvisoVencimiento(String identificadorEstacionamiento, long minutosRestantes) {
        System.out.println("Aviso: El estacionamiento " + identificadorEstacionamiento + " vence en " + minutosRestantes + " minutos.");
    }

    public Usuario getUsuarioActual() {
        return usuarioActual;
    }

    public void setUsuarioActual(Usuario usuarioActual) {
        this.usuarioActual = usuarioActual;
    }

    public double getTarifaActual() {
        return tarifaActual;
    }
}