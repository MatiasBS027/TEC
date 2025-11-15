/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;

/**
 *
 * @author Matias
 */
public class Ejercicio1 {
    //super clase estatica
    public static class superclass {
        static void print() {
            System.out.println("print() en superclass es llamada");
        }
    }
    //clase estatica derivada
    public static class subclass extends superclass {
        static void print() {
            System.out.println("print() en subclass es llamada");
        }
    }

    public static void main(String[] args) {
        //creando objetos
        superclass A = new superclass();
        superclass B = new subclass();
        
        //usando el print
        A.print();
        B.print();
    }
}