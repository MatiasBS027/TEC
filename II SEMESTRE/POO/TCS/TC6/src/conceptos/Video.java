/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

import interfaces.Validacion;

/**
 * @author Matias
 * carnee:2025102376
 * Clase que representa un video con su clasificación y censura.
 */
public class Video implements Validacion {
    String clasificacion;
    String censura;

    public Video(String clasificacion, String censura) {
        this.clasificacion = clasificacion;
        this.censura = censura;
    }

    public String getClasificacion() {
        return clasificacion;
    }

    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
    }

    public String getCensura() {
        return censura;
    }

    public void setCensura(String censura) {
        this.censura = censura;
    }

    @Override
    public void validar(){
        System.out.println("Video: " + this.clasificacion + ". Validado" );
    }
}
