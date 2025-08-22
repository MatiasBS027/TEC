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

public class Ej3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese una cadena: ");
        String texto = sc.nextLine();

        for (int i = 0; i < texto.length(); i++) {
            System.out.println(texto.charAt(i));
        }
    }
}
