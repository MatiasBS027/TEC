/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import java.util.ArrayList;
import conceptos.Cliente;
import ventanas.Escritorio;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

/**
 *
 * @author Matias
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        
        try {
            ArrayList<Cliente> clientes;
            File xmlFile = new File("clientes.xml");
            clientes = util.cargadorXML.Cargar(new FileInputStream(xmlFile));

            for (Cliente c : clientes) {
                System.out.println(c);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
}
