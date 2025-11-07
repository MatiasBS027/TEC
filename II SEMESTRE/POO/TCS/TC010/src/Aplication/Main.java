/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;

import Conceptos.Contacto;
import Util.ContactoInput;
import Util.ContactoOuput;

import java.io.IOException;

/**
 * @author Matias
 * carnee: 2025102376
 */
public class Main {

    public static void main(String[] args) {
        Contacto c1 = new Contacto();
        Contacto c2 = new Contacto();
        Contacto c3 = new Contacto();
        ContactoInput cargar = new ContactoInput();
        ContactoOuput salvar = new ContactoOuput();

        c1.setNombre("Juan Perez");
        c1.setEmail("juan@gmail.com");

        c2.setNombre("Juana Rojas");
        c2.setEmail("juana@gmail.com");

        c3.setNombre("Rosa Rojas");
        c3.setEmail("rosa@gmail.com");

        //Serializando los objetos
        try {
            System.out.println("Escribiendo objetos....");
            salvar.open();
            salvar.write(c1);
            salvar.write(c2);
            salvar.write(c3);
            salvar.close();
        } catch (IOException e) {
            System.out.println(e.toString());
        }

        //Deserializar
        try{
            cargar.open();
            do {
                c1 = cargar.read();
                if (c1 != null)
                    System.out.println("Contacto: " + c1.toString());
            } while (c1 != null);
            cargar.close();
        } catch (IOException  | ClassNotFoundException e){
            e.printStackTrace();
        }
    }
}
