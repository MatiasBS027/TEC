/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;
import Conceptos.colegio;
import Conceptos.taller;
/**
 *
 * @author Matias
 */
public class Main {
    public static void main(String[] args) {
        colegio cole1 = new colegio();
        taller taller1 = new taller();
        colegio cole2 = new taller();

        cole1.timbre();
        taller1.timbre();
        cole2.timbre();
    }
}
