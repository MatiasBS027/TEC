/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 * @author Matias
 * carnee:2025102376
 * Clase que representa un documento de Word.
 */
public class Word extends Documento {
    String version;

    public Word(String titulo, String version) {
        this.titulo = titulo;
        this.version = version;
    }
    public String getVersion() {
        return version;
    }
    public void setVersion(String version) {
        this.version = version;
    }

    @Override
    public void validar(){
        System.out.println("Documento Word: " + this.titulo + ". Validado" );
    }
    
}
