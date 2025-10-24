/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;

import Controlador.controller;
import Vista.VentanaSumar;
import modelo.Suma;

/**
 * @author Matias
 * Carnee: 2025102376
 */
public class Main {

    public static void main(String[] args) {
        Suma modelo = new Suma();
        VentanaSumar vista = new VentanaSumar();
        controller c = new controller(vista,modelo);

        c.iniciar();
        vista.setVisible(true);
    }
    
}
