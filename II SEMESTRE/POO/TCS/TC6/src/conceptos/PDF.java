    /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 * @author Matias
 * carnee:2025102376
 * Clase que representa un documento PDF.
 */

public class PDF extends Documento {
    boolean protegido;
    public PDF(String titulo, boolean protegido) {
        this.titulo = titulo;
        this.protegido = protegido;
    }
    public boolean isProtegido() {
        return protegido;
    }
    public void setProtegido(boolean protegido) {
        this.protegido = protegido;
    }

    @Override
    public void validar() {
        System.out.println("Documento PDF: " + this.titulo + ". Validado" );
    }
}
