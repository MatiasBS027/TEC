/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicios;
import java.util.Arrays;

/**
 *
 * @author Matias
 * carne: 2025102376
 */
public class Ej6 {
    public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {1, 2, 3, 4, 5};

        if (Arrays.equals(array1, array2)) {
            System.out.println("Los arrays son iguales.");
        } else {
            System.out.println("Los arrays son diferentes.");
        }
    }
}