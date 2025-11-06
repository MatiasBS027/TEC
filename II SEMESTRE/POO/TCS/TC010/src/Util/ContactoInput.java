/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Contacto;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

/**
 *
 * @author Matias
 */
public class ContactoInput {
    FileInputStream file;
    ObjectInputStream entrada;

    public void open() throws IOException {
        file = new FileInputStream("contactos.dat");
        entrada = new ObjectInputStream(file);
    }

    public void close() throws  IOException{
        if (entrada != null)
            entrada.close();
    }

    public Contacto read() throws  IOException, ClassNotFoundException {
        Contacto contacto = null;

        if (entrada != null) {
            try {
                contacto = (Contacto) entrada.readObject();
            } catch (EOFException eof) {
                return null;
            }
        }
        return contacto;
    }
}
