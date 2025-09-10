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
public class Veterinario extends Personal {
    String codigo;
    public Veterinario(String nombre, String apellidos, Date fechaContratacion) {
        super(nombre, apellidos, fechaContratacion);
        this.codigo = codigo;
    }
    public String getCodigo() {
        return codigo;
    }
    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
}

