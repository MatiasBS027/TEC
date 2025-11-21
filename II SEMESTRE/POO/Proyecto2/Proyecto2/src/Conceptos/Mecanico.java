/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conceptos;

import java.io.Serializable;
import java.util.ArrayList;

/**
 *
 * @author Corea
 */
public class Mecanico implements Serializable {
    private static final long serialVersionUID = 1L;
    String id;
    String nombre;
    String puesto;
    ArrayList<String> servicios = new ArrayList<>();

    // Getters y setters
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

    public String getPuesto() {
        return puesto;
    }

    public void setPuesto(String puesto) {
        this.puesto = puesto;
    }

    public ArrayList<String> getServicios() {
        return servicios;
    }

    public void addServicio(String id) {
        this.servicios.add(id);
    }

    @Override
    public String toString() {
        return "id=" + id + ", nombre=" + nombre + ", puesto=" + puesto + ", servicios=" + servicios;
    }

}
