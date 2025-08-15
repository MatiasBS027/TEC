/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;
import conceptos.Bicicleta;
import util.Direccion;
import conceptos.Telefono;
import conceptos.Walkman;


/**
 *
 * @author Matias
 * 
 * 
 */

public class Main {
    public static void main(String[] args) {
        // Bicicleta
        Bicicleta b1 = new Bicicleta("Deportivo", 36, 26.6f);//El f es por que es un float
        System.out.println("Sillin: " + b1.getTipoSillin());
        System.out.println("Radios: " + b1.getNumRadios());
        System.out.println("Diametro de la rueda: " + b1.getDiamRueda());

        // Telefono
        Telefono t1 = new Telefono("Negro", 150.0, 2.5, "Rueda");
        System.out.println("Color: " + t1.getColor());
        System.out.println("Precio: " + t1.getPrecio());
        System.out.println("Extension de cable: " + t1.getExtensionCable());
        System.out.println("Forma de marcar: " + t1.getFormaMarcar());

        //Walkman
        String[] botones = {"Play", "Stop", "Rewind", "Fast Forward"};
        Walkman w1 = new Walkman("Rojo", "Sony", "3.5mm", botones);
        System.out.println("Color: " + w1.getColor());
        System.out.println("Marca: " + w1.getMarca());
        System.out.println("Tipo de disquette: " + w1.getTipoDisquette());
        System.out.print("Lista de botones: ");
        for (Object boton : w1.getListaBotones()) {
            System.out.print(boton + " ");
        }
    }
}
