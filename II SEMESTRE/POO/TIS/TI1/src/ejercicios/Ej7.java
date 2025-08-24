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
public class Ej7 {
    public static void main(String[] args) {
        int[][] matriz = new int[6][6];
        Random rand = new Random();

        // Llenar matriz
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                matriz[i][j] = rand.nextInt(100);
            }
        }

        // Mostrar matriz completa
        System.out.println("Matriz:");
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }

        // Diagonal principal
        System.out.println("\nDiagonal Principal:");
        for (int i = 0; i < 6; i++) {
            System.out.print(matriz[i][i] + " ");
        }

        // Diagonal inversa
        System.out.println("\nDiagonal Inversa:");
        for (int i = 0; i < 6; i++) {
            System.out.print(matriz[i][5 - i] + " ");
        }
    }
}

