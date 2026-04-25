import java.time.LocalDate;
import java.util.List;

public class AppUsuario {

	private Usuario usuarioActual;
	private double tarifaActual;

	public DetalleCobro solicitarPago(long numeroCedulaUsuario, double tarifaActual) {
		this.tarifaActual = tarifaActual;
		Usuario usuario = Municipalidad.getUsuarioPorCedula(numeroCedulaUsuario);
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
				"",
				numeroCedulaUsuario
		);
		usuario.registrarCobro(detalleCobro);
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
		Usuario usuario = Municipalidad.getUsuarioPorCedula(numeroCedulaUsuario);
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
