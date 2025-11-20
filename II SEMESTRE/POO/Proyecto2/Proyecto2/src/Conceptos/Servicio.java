/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conceptos;

/**
 *
 * @author Corea
 */
public class Servicio {
    String id;
    String nombre;
    String precio;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getPrecio() { return precio; }
    public void setPrecio(String precio) { this.precio = precio; }

    @Override
    public String toString() {
        return "id=" + id + ", nombre=" + nombre + ", precio=" + precio;
    }
}
