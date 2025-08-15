/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import conceptos.Tiempo;
import conceptos.Rectangulo;
/**
 *
 * @author Matias
 * carne 2025102376
 */
public class Main {
    public static void main(String[] args) {
        Tiempo t1 = new Tiempo(6, 23, 0);
        Tiempo t2 = new Tiempo(7, 39, 0);
        Tiempo t3;
        t3 = t1.diferencia(t2);

        System.out.println(t3.getHoras() + " horas");
        System.out.println(t3.getMinutos() + " minutos");
        System.out.println(t3.getSegundos() + " segundos");

        Rectangulo r1 = new Rectangulo(11, 10);

        Rectangulo r3 = r1.perimetro(r1);
        Rectangulo r4 = r1.area(r1);

        System.out.println("Perímetro: " + r3.getAncho());
        System.out.println("Área: " + r4.getAncho());
        System.out.println("Es cuadrado: " + r1.esCuadrado());
    }
}
