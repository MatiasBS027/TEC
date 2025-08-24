/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicios;
import java.util.Random;

/**
 *
 * @author Matias
 * carne: 2025102376
 */

public class Ej5{
    public static void main(String[] args) {
        int[] numeros = new int[10];
        Random rand = new Random();

        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = rand.nextInt(100); // Números entre 0 y 99
        }
        System.out.println("Números aleatorios:");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
    }
}

