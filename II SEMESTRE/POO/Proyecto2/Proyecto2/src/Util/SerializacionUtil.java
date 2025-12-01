/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import java.io.*;
import java.util.ArrayList;

/**
 * Utilidad para serializar y deserializar objetos en archivos .DAT
 * Maneja la lectura y escritura de ArrayLists completos
 * 
 * @author Matias 
 */
public class SerializacionUtil{
    
    // Ruta base donde se guardan los archivos .DAT
    private static final String RUTA_BASE = "src/data/";

    private static void asegurarRutaBase() {
        File base = new File(RUTA_BASE);
        if (!base.exists()) {
            base.mkdirs();
        }
    }
    
    /**
     * Guarda un ArrayList de objetos en un archivo .DAT
     * lista ArrayList a guardar
     * nombreArchivo Nombre del archivo (ej: "CLIENTES.DAT")
     */
    public static boolean guardarLista(ArrayList<?> lista, String nombreArchivo) {
        asegurarRutaBase();
        try (ObjectOutputStream oos = new ObjectOutputStream(
                new FileOutputStream(RUTA_BASE + nombreArchivo))) {
            oos.writeObject(lista);
            return true;
        } catch (IOException e) {
            System.err.println("Error al guardar " + nombreArchivo + ": " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Carga un ArrayList de objetos desde un archivo .DAT
     * Nombre del archivo (ej: "CLIENTES.DAT")
     * ArrayList con los objetos cargados, o lista vacía si hay error
     */
    @SuppressWarnings("unchecked")
    public static <T> ArrayList<T> cargarLista(String nombreArchivo) {
        asegurarRutaBase();
        File archivo = new File(RUTA_BASE + nombreArchivo);
        
        // Si el archivo no existe o está vacío, retornar lista vacía
        if (!archivo.exists() || archivo.length() == 0) {
            return new ArrayList<>();
        }
        
        try (ObjectInputStream ois = new ObjectInputStream(
                new FileInputStream(archivo))) {
            return (ArrayList<T>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error al cargar " + nombreArchivo + ": " + e.getMessage());
            return new ArrayList<>();
        }
    }
    
    /**
     * Vacía un archivo .DAT 
     * Nombre del archivo a vaciar
     * true si se vació correctamente
     */
    public static boolean vaciarArchivo(String nombreArchivo) {
        asegurarRutaBase();
        try (FileOutputStream fos = new FileOutputStream(RUTA_BASE + nombreArchivo)) {
            // Simplemente abre y cierra el archivo, dejándolo vacío
            return true;
        } catch (IOException e) {
            System.err.println("Error al vaciar " + nombreArchivo + ": " + e.getMessage());
            return false;
        }
    }
    
    /**
     * Verifica si un archivo .DAT existe
     * Nombre del archivo
     * true si existe
     */
    public static boolean existeArchivo(String nombreArchivo) {
        return new File(RUTA_BASE + nombreArchivo).exists();
    }
    
    /**
     * Crea un archivo .DAT vacío si no existe
     * Nombre del archivo a crear
     * true si se creó o ya existía
     */
    public static boolean crearArchivoSiNoExiste(String nombreArchivo) {
        asegurarRutaBase();
        File archivo = new File(RUTA_BASE + nombreArchivo);
        if (!archivo.exists()) {
            try {
                archivo.getParentFile().mkdirs(); // Crear carpeta si no existe
                return archivo.createNewFile();
            } catch (IOException e) {
                System.err.println("Error al crear " + nombreArchivo + ": " + e.getMessage());
                return false;
            }
        }
        return true;
    }
}