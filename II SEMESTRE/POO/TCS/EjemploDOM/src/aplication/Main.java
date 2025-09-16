/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import java.util.ArrayList;
import conceptos.Cliente;

/**
 *
 * @author Matias
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ArrayList<Cliente> clientes;

        clientes = util.CargadorXML.Cargar("clientes.xml");
        for (Cliente cliente : clientes) {
            System.out.println(cliente);
        }
    }
}
