/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controlador;

import Vista.Ventana;
import Modelo.ModeloAsignacion;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.DefaultListModel;

/**
 *
 * @author Matias
 */
public class ControladorInsertar implements ActionListener {
    private Ventana vista;
    private ModeloAsignacion modeloPersonas;
    private ModeloAsignacion modeloTareas;
    private DefaultListModel<String> listModelPersonas;
    private DefaultListModel<String> listModelTareas;
    
    public ControladorInsertar(Ventana vista, ModeloAsignacion modeloPersonas, ModeloAsignacion modeloTareas,
                                DefaultListModel<String> listModelPersonas, DefaultListModel<String> listModelTareas) {
        this.vista = vista;
        this.modeloPersonas = modeloPersonas;
        this.modeloTareas = modeloTareas;
        this.listModelPersonas = listModelPersonas;
        this.listModelTareas = listModelTareas;
        
        this.vista.jButtonInsertarPersona.addActionListener(this);
        this.vista.jButtonInsertarTareas.addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == vista.jButtonInsertarPersona) {
            String nombre = vista.jInsertarPersona.getText();
            if (nombre != null && !nombre.trim().isEmpty()) {
                modeloPersonas.agregar(nombre);
                actualizarListaPersonas();
                actualizarComboBoxes();
                vista.jInsertarPersona.setText("");
            }
        } else if (e.getSource() == vista.jButtonInsertarTareas) {
            String nombre = vista.jInsertarTarea.getText();
            if (nombre != null && !nombre.trim().isEmpty()) {
                modeloTareas.agregar(nombre);
                actualizarListaTareas();
                actualizarComboBoxes();
                vista.jInsertarTarea.setText("");
            }
        }
    }
    private void actualizarListaPersonas() {
        listModelPersonas.clear();
        for (int i = 0; i < modeloPersonas.getTamanio(); i++) {
            listModelPersonas.addElement(modeloPersonas.getNombre(i));
        }
    }
    private void actualizarListaTareas() {
        listModelTareas.clear();
        for (int i = 0; i < modeloTareas.getTamanio(); i++) {
            listModelTareas.addElement(modeloTareas.getNombre(i));
        }
    }
    private void actualizarComboBoxes() {
        // Limpiar ComboBoxes
        vista.jComboBoxPersona.removeAllItems();
        vista.jComboBoxTareas.removeAllItems();
        // Llenar ComboBox de Personas
        for (int i = 0; i < modeloPersonas.getTamanio(); i++) {
            vista.jComboBoxPersona.addItem(modeloPersonas.getNombre(i));
        }
        // Llenar ComboBox de Tareas
        for (int i = 0; i < modeloTareas.getTamanio(); i++) {
            vista.jComboBoxTareas.addItem(modeloTareas.getNombre(i));
        }
    }
}
