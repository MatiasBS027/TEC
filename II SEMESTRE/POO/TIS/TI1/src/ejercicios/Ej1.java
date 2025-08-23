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
 **/
public class Ej1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el primer numero: ");
        int n1 = sc.nextInt();
        System.out.println("Ingrese el segundo numero: ");
        int n2 = sc.nextInt();
        int suma = n1 + n2;
        System.out.println("La suma de " + n1 + " y " + n2 + " es: " + suma);
        int resta = n1 - n2;
        System.out.println("La resta de " + n1 + " y " + n2 + " es: " + resta);
        int multiplicacion = n1 * n2;
        System.out.println("La multiplicacion de " + n1 + " y " + n2 + " es: " + multiplicacion);
        if (n2 != 0) {
            double division = (double) n1 / n2;
            System.out.println("La division de " + n1 + " y " + n2 + " es: " + division);
        } else {
            System.out.println("No se puede dividir por cero.");
        }
    }
    
}
