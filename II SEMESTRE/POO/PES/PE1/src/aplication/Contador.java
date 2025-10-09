/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;
import java.util.Scanner;

/**
 *
 * @author Matias
 * carnee: 2025102376
 */
public class Contador {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int[] contador = new int[26];
        Scanner scanner = new Scanner(System.in);

        //Solicitar al usuario una palabra
        System.out.print("Ingrese una sola palabra (letras solo, por favor): ");
        String palabra = scanner.nextLine();

        // Convertir la palabra a mayusculas para facilitar la comparación
        palabra = palabra.toUpperCase();

        // Contar la frecuencia de cada letra en la palabra
        for (int i = 0; i < palabra.length(); i++) {
            try {
                char c = palabra.charAt(i);
                contador[c - 'A']++;
            } catch (ArrayIndexOutOfBoundsException e) {
                char c = palabra.charAt(i);
                System.out.println("No es una letra: " + c);
            }
        }

        // Mostrar los resultados
        System.out.println();
        for (int i = 0; i < contador.length; i++) {
            if (contador[i] > 0) {
                System.out.println((char) (i + 'A') + ": " + contador[i]);
            }
        }
    }
}
