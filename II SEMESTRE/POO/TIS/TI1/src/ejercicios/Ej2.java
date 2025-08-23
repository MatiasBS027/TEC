/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicios;

/**
 *
 * @author Matias
 * carne: 2025102376
 */
public class Ej2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Sacar los pares de 1 al 10 con while
        int i = 1;
        System.out.println("Pares de 1 al 10 con while:");
        while (i<= 10) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
            i++;
        }
        // Sacar los pares de 1 al 10 con for
        int j;
        System.out.println("Pares de 1 al 10 con for:");
        for (j = 1; j <= 10; j++) {
            if (j % 2 == 0) {
                System.out.println(j);
            }
        }
    }
}
