/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controlador;

import Vista.Ventana;
import Modelo.ModeloAsignacion;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

/**
 *
 * @author Matias
 */
public class ControladorAsignaciones {
    private Ventana vista;
    private ModeloAsignacion modeloPersonas;
    private ModeloAsignacion modeloTareas;

    public ControladorAsignaciones(Ventana vista, ModeloAsignacion modeloPersonas, ModeloAsignacion modeloTareas) {
        this.vista = vista;
        this.modeloPersonas = modeloPersonas;
        this.modeloTareas = modeloTareas;

        // Agregar listener para cuando seleccionas una persona
        this.vista.jListPersonas.addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                if (!e.getValueIsAdjusting()) {
                    mostrarTareaAsignada();
                }
            }
        });

        // Agregar listener para cuando seleccionas una tarea
        this.vista.jListTareas.addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                if (!e.getValueIsAdjusting()) {
                    mostrarPersonaAsignada();
                }
            }
        });
    }

    private void mostrarTareaAsignada() {
        int indicePersona = vista.jListPersonas.getSelectedIndex();

        if (indicePersona >= 0) {
            int indiceTarea = modeloPersonas.obtenerIndice(indicePersona);

            if (indiceTarea >= 0) {
                vista.jListTareas.setSelectedIndex(indiceTarea);
            } else {
                vista.jListTareas.clearSelection();
            }
        }
    }

    private void mostrarPersonaAsignada() {
        int indiceTarea = vista.jListTareas.getSelectedIndex();
        if (indiceTarea >= 0) {
            int indicePersona = modeloTareas.obtenerIndice(indiceTarea);

            if (indicePersona >= 0) {
                vista.jListPersonas.setSelectedIndex(indicePersona);
            } else {
                vista.jListPersonas.clearSelection();
            }
        }
    }
}