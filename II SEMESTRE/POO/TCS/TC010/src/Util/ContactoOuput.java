/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Contacto;

import java.io.*;

/**
 *
 * @author Matias
 */
public class ContactoOuput {
    FileOutputStream file;
    ObjectOutputStream salida;

    public void open() throws IOException {
        file = new FileOutputStream("contactos.dat");
        salida = new ObjectOutputStream(file);
        };

    public void close() throws  IOException{
        if (salida != null)
            salida.close();
    }

    public void write(Contacto contacto) throws IOException{
        if (salida != null)
            salida.writeObject(contacto);
    }

}
