/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import conceptos.PDF;
import conceptos.Video;
import conceptos.Word;
import util.ServicioValidacion;

/**
 * @author Matias
 * carnee:2025102376
 * Crear una interfaz Validacion con un método validar().
 */
public class Main {
    public static void main(String[] args) {
        ServicioValidacion servicio = new ServicioValidacion();

        Word w1 = new Word("doc1.docx", "1.0");
        Word w2 = new Word("doc2.docx", "2.0");
        PDF p1 = new PDF("pdf1.pdf", true);
        PDF p2 = new PDF("pdf2.pdf", false);
        Video v1 = new Video("Anime", "PG");

        servicio.agregarArchivo(w1);
        servicio.agregarArchivo(w2);
        servicio.agregarArchivo(p1);
        servicio.agregarArchivo(p2);
        servicio.agregarArchivo(v1);

        servicio.validar();
    }
}
