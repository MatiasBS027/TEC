/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class Cliente {
    String nombre;
    String placa;
    String telefono;

    public Cliente(String nombre, String placa, String telefono) {
        this.nombre = nombre;
        this.placa = placa;
        this.telefono = telefono;
    }

    public Cliente(){
    }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getPlaca() {
        return placa;
    }
    public void setPlaca(String placa) {
        this.placa = placa;
    }
    public String getTelefono() {
        return telefono;
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    @Override
    public String toString() {
        return "Cliente: " +this.getNombre() + " Placa: " + this.getPlaca() + " Telefono: " + this.getTelefono();
    }
}
