/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import conceptos.Cuadrado;
import conceptos.FiguraRegular;
import conceptos.Rectangulo;

/**
 *
 * @author Matias
 * carne: 2025102376
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        FiguraRegular fg1 = new FiguraRegular();
        Rectangulo r1 = new Rectangulo(10, 40);
        Cuadrado c1 = new Cuadrado(10);

        fg1.agregarLado(20);
        fg1.agregarLado(20);
        fg1.agregarLado(20);

        System.out.println("El perimetro de la figura Regular es: " + fg1.perimetro());

        System.out.println("------------------");

        System.out.println("El perimetro del rectangulo es: " + r1.perimetro());
        System.out.println("Ancho del rectangulo: " + r1.getAncho());
        System.out.println("Largo del rectangulo: " + r1.getLargo());
        System.out.println("El area del rectangulo es: " + r1.area());
        r1.setAncho(20);
        r1.setLargo(100);
        System.out.println("El perimetro del rectangulo 2 es: " + r1.perimetro());
        System.out.println("Ancho del rectangulo 2: " + r1.getAncho());
        System.out.println("Largo del rectangulo 2: " + r1.getLargo());
        System.out.println("El area del rectangulo 2 es: " + r1.area());

        System.out.println("------------------");

        System.out.println("El perimetro del cuadrado es: " + c1.perimetro());
        System.out.println("El area del cuadrado es: " + c1.area());

    }
}
