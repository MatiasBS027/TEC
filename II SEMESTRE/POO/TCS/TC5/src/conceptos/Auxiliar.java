/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;
import java.util.Date;

/**
 *
 * @author Matias
 */
public class Auxiliar extends Personal {
    String funcion;
    public Auxiliar(String nombre, String apellidos, Date fechaContratacion) {
        super(nombre, apellidos, fechaContratacion);
        this.funcion = funcion;
    }
    public String getFuncion() {
        return funcion;
    }
    public void setFuncion(String funcion) {
        this.funcion = funcion;
    }
}
