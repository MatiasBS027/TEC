/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import conceptos.Mesa;
        
/**
 *
 * @author Matias
 * carne 2025102376
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Mesa mesa1 = new Mesa();
        
        mesa1.setMaterial("Madera");
        
        System.out.println("Material: " + mesa1.getMaterial());
        System.out.println("Material: " + mesa1.getForma());
    }
    
}
