/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo;
import java.util.Vector;

/**
 *
 * @author Matias
 */
public class ModeloAsignacion {
    //Vectores
    private Vector<String> nombres; //Guarda las personas y tareas
    private Vector<Integer> indices; // Guarda las asignaciones de cada uno

    //Contructor
    public ModeloAsignacion(){
        this.nombres = new Vector<>();
        this.indices = new Vector<>();
    }

    public Vector<String> getNombres() {
        return nombres;
    }

    public void setNombres(Vector<String> nombres) {
        this.nombres = nombres;
    }

    public Vector<Integer> getIndices() {
        return indices;
    }

    public void setIndices(Vector<Integer> indices) {
        this.indices = indices;
    }

    // Agregar elemento
    public void agregar(String nombre){
        this.nombres.add(nombre);
        this.indices.add(-1); // Como no se ah asigando nada ponemos un -1
    }

    //Asiganar 2 elementos
    public void asignar(int posicion, int indice){
        if (posicion >= 0 && posicion < indices.size()){
            indices.set(posicion,indice);
        }
    }

    //Obtener el indice de asignacion del elemento
    public int obtenerIndice(int posicion){
        if (posicion >= 0 && posicion < indices.size()) {
            return indices.get(posicion);
        }
        return -1;  // Si la posición no existe, retorna -1
    }

    //Obtiene el tamaño del modelo (cuántos elementos hay)
    public int getTamanio() {
        return nombres.size();
    }

    //Obtiene un nombre por posición
    public String getNombre(int posicion) {
        if (posicion >= 0 && posicion < nombres.size()) {
            return nombres.get(posicion);
        }
        return null;
    }
}
