/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package util;

import interfaces.Validacion;
import java.util.ArrayList;

/**
 * @author Matias
 * carnee:2025102376
 * Clase que gestiona la validación de múltiples archivos
 */
public class ServicioValidacion {
    ArrayList<Validacion> archivos;

    public ServicioValidacion() {
        this.archivos = new ArrayList<>();
    }

    public void agregarArchivo(Validacion archivo){
        this.archivos.add(archivo);
    }

    public void validar(){
        for(Validacion archivo : archivos){
            archivo.validar();
        }
    }
    
}
