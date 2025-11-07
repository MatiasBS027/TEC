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
public class ControladorAsociar implements ActionListener {
    private Ventana vista;
    private ModeloAsignacion modeloPersonas;
    private ModeloAsignacion modeloTareas;
    private DefaultListModel<String> listModelPersonas;
    private DefaultListModel<String> listModelTareas;
    
    public ControladorAsociar(Ventana vista,ModeloAsignacion modeloPersonas,ModeloAsignacion modeloTareas,
                                DefaultListModel<String> listModelPersonas, DefaultListModel<String> listModelTareas) {
        this.vista = vista;
        this.modeloPersonas = modeloPersonas;
        this.modeloTareas = modeloTareas;
        this.listModelPersonas = listModelPersonas;
        this.listModelTareas = listModelTareas;
        
        this.vista.jButtonAsignacion.addActionListener(this);
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == vista.jButtonAsignacion) {
            int indicePersona = vista.jComboBoxPersona.getSelectedIndex();
            int indiceTarea = vista.jComboBoxTareas.getSelectedIndex();
            
            if (indicePersona >= 0 && indiceTarea >= 0) {
                // Hacer la asignación bidireccional
                modeloPersonas.asignar(indicePersona, indiceTarea);
                modeloTareas.asignar(indiceTarea, indicePersona);
                
                // Actualizar las listas (esto lo delegamos al otro controlador)
                actualizarListas();
            }
        }
    }
    
    private void actualizarListas() {
        listModelPersonas.clear();
        for (int i = 0; i < modeloPersonas.getTamanio(); i++) {
            listModelPersonas.addElement(modeloPersonas.getNombre(i));
        }
        
        listModelTareas.clear();
        for (int i = 0; i < modeloTareas.getTamanio(); i++) {
            listModelTareas.addElement(modeloTareas.getNombre(i));
        }
    }
}

