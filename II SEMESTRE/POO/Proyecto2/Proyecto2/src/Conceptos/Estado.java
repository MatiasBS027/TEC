/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conceptos;
import java.io.Serializable;

/**
 *
 * @author Matias
 */
public class Estado implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String id;
    private String nombre;

    // Constructor vacío
    public Estado() {
    }

    // Constructor con parámetros
    public Estado(String id, String nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    // Getters y Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return nombre; // Para que se vea bien en los ComboBox
    }
}
