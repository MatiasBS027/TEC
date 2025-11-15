/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;

/**
 *
 * @author Matias
 */
public class Ejercicio2 {
    // super clase
    public static class superclass {
        void print() {
            System.out.println("print en superclass es llamado");
        }
    }

    // clase estatica derivada
    public static class subclass extends superclass {
        @Override
        void print() {
            System.out.println("print en subclass es llamado");
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
