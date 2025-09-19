/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

import interfaces.Validacion;

/**
 * @author Matias
 * carnee:2025102376
 * Clase abstracta que representa un documento genérico.
 */
public abstract class Documento implements Validacion {
    String titulo;

    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

}
