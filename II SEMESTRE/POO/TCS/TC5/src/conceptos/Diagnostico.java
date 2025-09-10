/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
import java.util.Date;

public class Diagnostico {
    Date fecha;
    String descripcion;
    Animal mascota;
    Personal personal;

    public Diagnostico(Date fecha, String descripcion, Animal mascota, Personal personal) {
        this.fecha = fecha;
        this.descripcion = descripcion;
        this.mascota = mascota;
        this.personal = personal;
    }

    public Date getFecha() {
        return fecha;
    }

    public void setFecha(Date fecha) {
        this.fecha = fecha;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public Animal getMascota() {
        return mascota;
    }
    public void setMascota(Animal mascota) {
        this.mascota = mascota;
    }
    public Personal getPersonal() {
        return personal;
    }
    public void setPersonal(Personal personal) {
        this.personal = personal;
    }
}
