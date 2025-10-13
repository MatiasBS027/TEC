/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JDialog.java to edit this template
 */
package ventanas;

import conceptos.Mecanico;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;
import java.awt.Dimension;
import java.awt.Toolkit;

/**
 *
 * @author Matias
 */
public class ventanaMecanico extends javax.swing.JDialog {

    private final ArrayList<Mecanico> mecanicos = new ArrayList<>();
    private final ArrayList<String> serviciosSeleccionados = new ArrayList<>();
    private DefaultTableModel modelo;

    // Creates new form ventanaMecanico
    public ventanaMecanico(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
        configurarTabla();
        llenarTabla();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        this.setSize(screenSize);
    }
    // Configura la tabla y sus eventos
    private void configurarTabla() {
        modelo = new DefaultTableModel(new Object[]{"ID", "Nombre", "Puesto"}, 0) {
            @Override public boolean isCellEditable(int row, int column) { return false; }
        };
        
        jTable1.setModel(modelo);
        jTable1.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);
        jTable1.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
            
            @Override public void valueChanged(ListSelectionEvent e) {
                if (!e.getValueIsAdjusting()) {
                    cargarDesdeTabla();
                }
            }
        });
        actualizarEtiquetaServicios();
    }
    // Llena la tabla con los datos de los mecánicos desde el archivo XML
    private void llenarTabla() {
        mecanicos.clear();
        modelo.setRowCount(0);
        try {
            InputStream is = getClass().getClassLoader().getResourceAsStream("data/mecanicos.xml");
            
            if (is == null) {
                throw new FileNotFoundException("No se encontró data/mecanicos.xml en el classpath");
            }
            
            @SuppressWarnings("unchecked")
            ArrayList<Mecanico> datos = (ArrayList<Mecanico>) util.cargadorXML.Cargar(is, "mecanico");
            mecanicos.addAll(datos);
            
            for (Mecanico m : mecanicos) {
                modelo.addRow(new Object[]{m.getId(), m.getNombre(), m.getPuesto()});
            }
            
            if (!mecanicos.isEmpty()) {
                jTable1.setRowSelectionInterval(0, 0);
            }
            
        } catch (FileNotFoundException e) {
            mostrarError("Error al leer mecanicos: " + e.getMessage());
        }
    }
    // Carga los datos del mecánico seleccionado en la tabla a los campos de texto
    private void cargarDesdeTabla() {
        int fila = jTable1.getSelectedRow();
        if (fila < 0 || fila >= mecanicos.size()) {
            return;
        }
        
        Mecanico mecanico = mecanicos.get(jTable1.convertRowIndexToModel(fila));
        jTextFieldId.setText(mecanico.getId());
        jTextFieldNombre.setText(mecanico.getNombre());
        jTextFieldPuesto.setText(mecanico.getPuesto());
        serviciosSeleccionados.clear();
        serviciosSeleccionados.addAll(mecanico.getServicios());
        actualizarEtiquetaServicios();
    }
    // Construye un objeto Mecanico desde los campos de texto
    private Mecanico construirMecanicoDesdeCampos() {
        String id = jTextFieldId.getText().trim();
        String nombre = jTextFieldNombre.getText().trim();
        String puesto = jTextFieldPuesto.getText().trim();
        
        if (id.isEmpty() || nombre.isEmpty() || puesto.isEmpty()) {
            mostrarError("Complete los campos obligatorios");
            return null;
        }
        
        if (!id.matches("\\d+")) {
            mostrarError("El ID debe ser numérico");
            return null;
        }
        
        Mecanico mecanico = new Mecanico();
        mecanico.setId(id);
        mecanico.setNombre(nombre);
        mecanico.setPuesto(puesto);
        mecanico.getServicios().addAll(serviciosSeleccionados);
        return mecanico;
    }
    // Limpia los campos de texto y la selección de servicios
    private void limpiarCampos() {
        jTextFieldId.setText("");
        jTextFieldNombre.setText("");
        jTextFieldPuesto.setText("");
        serviciosSeleccionados.clear();
        actualizarEtiquetaServicios();
        jTable1.clearSelection();
    }

    private void actualizarEtiquetaServicios() {
        jLabelServicios.setText("Servicios (" + serviciosSeleccionados.size() + ")");
    }

    private void mostrarError(String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, "Error", JOptionPane.ERROR_MESSAGE);
    }

    private void mostrarInfo(String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, "Información", JOptionPane.INFORMATION_MESSAGE);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabelTitulo = new javax.swing.JLabel();
        jLabelId = new javax.swing.JLabel();
        jTextFieldId = new javax.swing.JTextField();
        jLabelNombre = new javax.swing.JLabel();
        jTextFieldNombre = new javax.swing.JTextField();
        jLabelPuesto = new javax.swing.JLabel();
        jTextFieldPuesto = new javax.swing.JTextField();
        jLabelServicios = new javax.swing.JLabel();
        jButtonVerEditar = new javax.swing.JButton();
        jButtonNuevo = new javax.swing.JButton();
        jButtonModificar = new javax.swing.JButton();
        jButtonBorrar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        jButtonSalir = new javax.swing.JButton();
        jButtonLimpiar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        jLabelTitulo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabelTitulo.setText("Mecanicos");

        jLabelId.setText("ID");

        jTextFieldId.setColumns(10);

        jLabelNombre.setText("Nombre");

        jTextFieldNombre.setColumns(18);

        jLabelPuesto.setText("Puesto");

        jTextFieldPuesto.setColumns(15);

        jLabelServicios.setText("Servicios");

        jButtonVerEditar.setText("Ver Editar");
        jButtonVerEditar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonVerEditarActionPerformed(evt);
            }
        });

        jButtonNuevo.setText("Nuevo");
        jButtonNuevo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonNuevoActionPerformed(evt);
            }
        });

        jButtonModificar.setText("Modificar");

        jButtonBorrar.setText("Borrar");

        jTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        jScrollPane1.setViewportView(jTable1);

        jButtonSalir.setText("Salir");
        jButtonSalir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonSalirActionPerformed(evt);
            }
        });

        jButtonLimpiar.setText("Limpiar");
        jButtonLimpiar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonLimpiarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(jButtonSalir))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(jLabelPuesto)
                                    .addComponent(jLabelId))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTextFieldId, javax.swing.GroupLayout.DEFAULT_SIZE, 150, Short.MAX_VALUE)
                                    .addComponent(jTextFieldPuesto, javax.swing.GroupLayout.DEFAULT_SIZE, 150, Short.MAX_VALUE))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(jLabelServicios)
                                    .addComponent(jLabelNombre))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTextFieldNombre, javax.swing.GroupLayout.DEFAULT_SIZE, 220, Short.MAX_VALUE)
                                    .addComponent(jButtonVerEditar, javax.swing.GroupLayout.DEFAULT_SIZE, 220, Short.MAX_VALUE))
                                .addGap(18, 18, 18))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addGap(0, 0, Short.MAX_VALUE)
                                .addComponent(jButtonLimpiar)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButtonModificar, javax.swing.GroupLayout.DEFAULT_SIZE, 90, Short.MAX_VALUE)
                            .addComponent(jButtonBorrar, javax.swing.GroupLayout.DEFAULT_SIZE, 90, Short.MAX_VALUE)
                            .addComponent(jButtonNuevo, javax.swing.GroupLayout.DEFAULT_SIZE, 90, Short.MAX_VALUE))))
                .addGap(20, 20, 20))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabelTitulo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addComponent(jLabelTitulo)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabelId)
                    .addComponent(jTextFieldId, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabelNombre)
                    .addComponent(jTextFieldNombre, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButtonNuevo))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabelPuesto)
                    .addComponent(jTextFieldPuesto, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabelServicios)
                    .addComponent(jButtonVerEditar)
                    .addComponent(jButtonModificar))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jButtonBorrar)
                    .addComponent(jButtonLimpiar))
                .addGap(18, 18, 18)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 188, Short.MAX_VALUE)
                .addGap(18, 18, 18)
                .addComponent(jButtonSalir)
                .addGap(20, 20, 20))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButtonSalirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonSalirActionPerformed
        dispose();
    }//GEN-LAST:event_jButtonSalirActionPerformed

    private void jButtonNuevoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonNuevoActionPerformed
        // Agregar nuevo mecánico
        Mecanico mecanico = construirMecanicoDesdeCampos();
        if (mecanico == null) {
            return;
        }
        for (Mecanico existente : mecanicos) {
            if (existente.getId().equals(mecanico.getId())) {
                mostrarError("Ya existe un mecánico con ese ID");
                return;
            }
        }
        
        mecanicos.add(mecanico);
        modelo.addRow(new Object[]{mecanico.getId(), mecanico.getNombre(), mecanico.getPuesto()});
        util.GuardarArchivo.guardarMecanicos(mecanicos);
        mostrarInfo("Mecánico agregado correctamente");
        limpiarCampos();
    }//GEN-LAST:event_jButtonNuevoActionPerformed

    private void jButtonVerEditarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonVerEditarActionPerformed
        ventanaServiciosValidados validados = new ventanaServiciosValidados((java.awt.Frame) getParent(), true, serviciosSeleccionados);
        validados.setVisible(true);
        
        if (validados.fueAceptado()) {
            serviciosSeleccionados.clear();
            serviciosSeleccionados.addAll(validados.getServiciosSeleccionados());
            actualizarEtiquetaServicios();
        }
    }//GEN-LAST:event_jButtonVerEditarActionPerformed

    private void jButtonModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonModificarActionPerformed
        // Modificar mecánico seleccionado
        int fila = jTable1.getSelectedRow();
        if (fila < 0) {
            mostrarError("Seleccione un mecánico");
            return;
        }
        
        Mecanico actualizado = construirMecanicoDesdeCampos();
        
        if (actualizado == null) {
            return;
        }
        
        int index = jTable1.convertRowIndexToModel(fila);
        for (int i = 0; i < mecanicos.size(); i++) {
            if (i != index && mecanicos.get(i).getId().equals(actualizado.getId())) {
                mostrarError("Ya existe un mecánico con ese ID");
                return;
            }
        }
        
        Mecanico original = mecanicos.get(index);
        original.setId(actualizado.getId());
        original.setNombre(actualizado.getNombre());
        original.setPuesto(actualizado.getPuesto());
        original.getServicios().clear();
        original.getServicios().addAll(actualizado.getServicios());
        modelo.setValueAt(original.getId(), index, 0);
        modelo.setValueAt(original.getNombre(), index, 1);
        modelo.setValueAt(original.getPuesto(), index, 2);
        util.GuardarArchivo.guardarMecanicos(mecanicos);
        mostrarInfo("Mecánico modificado correctamente");
    }//GEN-LAST:event_jButtonModificarActionPerformed

    private void jButtonBorrarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonBorrarActionPerformed
        // Borrar mecánico seleccionado
        int fila = jTable1.getSelectedRow();
        if (fila < 0) {
            mostrarError("Seleccione un mecánico");
            return;
        }
        
        int opcion = JOptionPane.showConfirmDialog(this, "¿Desea eliminar el mecánico seleccionado?", "Confirmar", JOptionPane.YES_NO_OPTION);
        if (opcion != JOptionPane.YES_OPTION) {
            return;
        }
        
        int index = jTable1.convertRowIndexToModel(fila);
        mecanicos.remove(index);
        modelo.removeRow(index);
        util.GuardarArchivo.guardarMecanicos(mecanicos);
        mostrarInfo("Mecánico eliminado correctamente");
        limpiarCampos();
    }//GEN-LAST:event_jButtonBorrarActionPerformed

    private void jButtonLimpiarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonLimpiarActionPerformed
    limpiarCampos();
    }//GEN-LAST:event_jButtonLimpiarActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(ventanaMecanico.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ventanaMecanico.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ventanaMecanico.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ventanaMecanico.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the dialog */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                ventanaMecanico dialog = new ventanaMecanico(new javax.swing.JFrame(), true);
                dialog.addWindowListener(new java.awt.event.WindowAdapter() {
                    @Override
                    public void windowClosing(java.awt.event.WindowEvent e) {
                        System.exit(0);
                    }
                });
                dialog.setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButtonBorrar;
    private javax.swing.JButton jButtonLimpiar;
    private javax.swing.JButton jButtonModificar;
    private javax.swing.JButton jButtonNuevo;
    private javax.swing.JButton jButtonSalir;
    private javax.swing.JButton jButtonVerEditar;
    private javax.swing.JLabel jLabelId;
    private javax.swing.JLabel jLabelNombre;
    private javax.swing.JLabel jLabelPuesto;
    private javax.swing.JLabel jLabelServicios;
    private javax.swing.JLabel jLabelTitulo;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable jTable1;
    private javax.swing.JTextField jTextFieldId;
    private javax.swing.JTextField jTextFieldNombre;
    private javax.swing.JTextField jTextFieldPuesto;
    // End of variables declaration//GEN-END:variables
}
