/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class PersonaFisica extends Persona {
    String cedula;

    public PersonaFisica(String email, String direccion, String telefono, String DNI) {
        super(email, direccion, telefono);
        this.cedula = cedula;
    }

    public String getCedula() {
        return cedula;
    }

    public void setCedula(String DNI) {
        this.cedula = cedula;
    }
}
