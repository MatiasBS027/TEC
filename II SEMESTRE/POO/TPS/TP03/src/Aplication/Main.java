/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package Aplication;

import Controlador.ControladorInsertar;
import Controlador.ControladorAsociar;
import Controlador.ControladorAsignaciones;
import Vista.Ventana;
import Modelo.ModeloAsignacion;
import javax.swing.DefaultListModel;

/**
 * 
 * @author Matias
 * Carnet: 2025102376
 */
public class Main {

    public static void main(String[] args) {
        // Crear modelos
        ModeloAsignacion modeloPersonas = new ModeloAsignacion();
        ModeloAsignacion modeloTareas = new ModeloAsignacion();

        // Crear vista
        Ventana vista = new Ventana();

        // Crear los modelos de las listas
        DefaultListModel<String> listModelPersonas = new DefaultListModel<>();
        DefaultListModel<String> listModelTareas = new DefaultListModel<>();

        // Asignar modelos a las listas de la vista
        vista.jListPersonas.setModel(listModelPersonas);
        vista.jListTareas.setModel(listModelTareas);

        // Crear los 3 controladores
        ControladorInsertar controladorInsertar = new ControladorInsertar(vista, modeloPersonas, modeloTareas, listModelPersonas, listModelTareas);

        ControladorAsociar controladorAsociar = new ControladorAsociar(vista, modeloPersonas, modeloTareas, listModelPersonas, listModelTareas);

        ControladorAsignaciones controladorAsignaciones = new ControladorAsignaciones(vista, modeloPersonas, modeloTareas);

        // Mostrar ventana
        vista.setTitle("Sistema de Asignación de Tareas");
        vista.setLocationRelativeTo(null);
        vista.setVisible(true);
    }
}
