/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicios;

import java.util.Scanner;
/**
 *
 * @author Matias
 * carne: 2025102376
 */
public class Ej4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;

        do {
            System.out.print("Ingrese una numero entero: ");
            numero = sc.nextInt();
        } while (numero < 0 || numero > 10);

        System.out.println("El numero valido: " + numero);
    }
}
