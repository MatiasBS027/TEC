/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class PersonaJuridica extends Persona {
    String cedulaJuridica;

    public PersonaJuridica(String email, String direccion, String telefono, String CIF) {
        super(email, direccion, telefono);
        this. cedulaJuridica =  cedulaJuridica;
    }

    public String getCedulaJuridica() {
        return  cedulaJuridica;
    }

    public void setCedulaJuridica(String CIF) {
        this. cedulaJuridica =  cedulaJuridica;
    }
}
