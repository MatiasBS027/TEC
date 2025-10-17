/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JDialog.java to edit this template
 */
package ventanas;

import conceptos.Servicio;
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
public class ventanaServicios extends javax.swing.JDialog {

    private final ArrayList<Servicio> servicios = new ArrayList<>();
    private DefaultTableModel modelo;

    // Constructor
    public ventanaServicios(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
        configurarTabla();
        llenarTabla();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        this.setSize(screenSize);
    }
    // Configura el modelo de la tabla y el listener de selección
    private void configurarTabla() {
        modelo = new DefaultTableModel(new Object[]{"ID", "Nombre", "Precio"}, 0) {
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
    }
    // Llena la tabla con los datos cargados desde el archivo XML
    private void llenarTabla() {
        servicios.clear();
        modelo.setRowCount(0);
        try {
            
            InputStream is = getClass().getClassLoader().getResourceAsStream("data/servicios.xml");
            if (is == null) {
                throw new FileNotFoundException("No se encontró data/servicios.xml en el classpath");
            }
            
            @SuppressWarnings("unchecked")
            ArrayList<Servicio> datos = (ArrayList<Servicio>) util.cargadorXML.Cargar(is, "servicio");
            servicios.addAll(datos);
            
            for (Servicio s : servicios) {
                modelo.addRow(new Object[]{s.getId(), s.getNombre(), s.getPrecio()});
            }
            
            if (!servicios.isEmpty()) {
                jTable1.setRowSelectionInterval(0, 0);
            }
            
        } catch (FileNotFoundException e) {
            mostrarError("Error al leer servicios: " + e.getMessage());
        }
    }
    // Carga los datos del servicio seleccionado en los campos de texto
    private void cargarDesdeTabla() {
        int fila = jTable1.getSelectedRow();
        if (fila < 0 || fila >= servicios.size()) {
            return;
        }
        
        Servicio servicio = servicios.get(jTable1.convertRowIndexToModel(fila));
        jTextFieldId.setText(servicio.getId());
        jTextFieldNombre.setText(servicio.getNombre());
        jTextFieldPuesto.setText(servicio.getPrecio());
    }
    // Construye un objeto Servicio desde los campos de texto, validando entradas
    private Servicio construirServicioDesdeCampos() {
        String id = jTextFieldId.getText().trim();
        String nombre = jTextFieldNombre.getText().trim();
        String precio = jTextFieldPuesto.getText().trim();
        if (id.isEmpty() || nombre.isEmpty() || precio.isEmpty()) {
            mostrarError("Complete los campos obligatorios");
            return null;
        }
        
        if (!id.matches("\\d+")) {
            mostrarError("El ID debe ser numérico");
            return null;
        }
        
        if (!precio.matches("\\d+(\\.\\d+)?")) {
            mostrarError("El precio debe ser numérico");
            return null;
        }
        
        Servicio servicio = new Servicio();
        servicio.setId(id);
        servicio.setNombre(nombre);
        servicio.setPrecio(precio);
        return servicio;
    }
    // Limpia los campos de texto y la selección de la tabla
    private void limpiarCampos() {
        jTextFieldId.setText("");
        jTextFieldNombre.setText("");
        jTextFieldPuesto.setText("");
        jTable1.clearSelection();
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
        jButtonNuevo = new javax.swing.JButton();
        jButtonModificar = new javax.swing.JButton();
        jButtonBorrar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        jButtonSalir = new javax.swing.JButton();
        jButtonLimpiar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        setTitle("Servicios");

        jLabelTitulo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabelTitulo.setText("Servicios");

        jLabelId.setText("ID");

        jTextFieldId.setColumns(10);

        jLabelNombre.setText("Nombre");

        jTextFieldNombre.setColumns(18);

        jLabelPuesto.setText("Precio");

        jTextFieldPuesto.setColumns(15);

        jButtonNuevo.setText("Nuevo");
        jButtonNuevo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonNuevoActionPerformed(evt);
            }
        });

        jButtonModificar.setText("Modificar");
        jButtonModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonModificarActionPerformed(evt);
            }
        });

        jButtonBorrar.setText("Borrar");
        jButtonBorrar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonBorrarActionPerformed(evt);
            }
        });

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
        jButtonLimpiar.setToolTipText("");
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
                .addGap(6, 6, 6)
                .addComponent(jLabelTitulo, javax.swing.GroupLayout.DEFAULT_SIZE, 642, Short.MAX_VALUE)
                .addContainerGap())
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addComponent(jLabelPuesto)
                                    .addComponent(jLabelId))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jTextFieldId)
                                    .addComponent(jTextFieldPuesto, javax.swing.GroupLayout.PREFERRED_SIZE, 1, Short.MAX_VALUE))
                                .addGap(20, 20, 20)
                                .addComponent(jLabelNombre)
                                .addGap(18, 18, 18)
                                .addComponent(jTextFieldNombre)
                                .addGap(18, 18, 18))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addGap(0, 0, Short.MAX_VALUE)
                                .addComponent(jButtonLimpiar)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButtonNuevo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jButtonModificar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jButtonBorrar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addGap(3, 3, 3))
                    .addComponent(jScrollPane1)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(jButtonSalir)))
                .addGap(20, 20, 20))
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
                    .addComponent(jButtonModificar))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jButtonBorrar)
                    .addComponent(jButtonLimpiar, javax.swing.GroupLayout.PREFERRED_SIZE, 23, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 188, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jButtonSalir)
                .addGap(32, 32, 32))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButtonSalirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonSalirActionPerformed
        dispose();
    }//GEN-LAST:event_jButtonSalirActionPerformed

    private void jButtonNuevoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonNuevoActionPerformed
        // Agregar nuevo servicio
        Servicio servicio = construirServicioDesdeCampos();
        if (servicio == null) {
            return;
        }
        
        for (Servicio existente : servicios) {
            if (existente.getId().equals(servicio.getId())) {
                mostrarError("Ya existe un servicio con ese ID");
                return;
            }
        }
        
        servicios.add(servicio);
        modelo.addRow(new Object[]{servicio.getId(), servicio.getNombre(), servicio.getPrecio()});
        util.GuardarArchivo.guardarServicios(servicios);
        mostrarInfo("Servicio agregado correctamente");
        limpiarCampos();
    }//GEN-LAST:event_jButtonNuevoActionPerformed

    private void jButtonModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonModificarActionPerformed
        // Modificar servicio seleccionado
        int fila = jTable1.getSelectedRow();
        if (fila < 0) {
            mostrarError("Seleccione un servicio");
            return;
        }
        
        Servicio actualizado = construirServicioDesdeCampos();
        if (actualizado == null) {
            return;
        }
        
        int index = jTable1.convertRowIndexToModel(fila);
        
        for (int i = 0; i < servicios.size(); i++) {
            if (i != index && servicios.get(i).getId().equals(actualizado.getId())) {
                mostrarError("Ya existe un servicio con ese ID");
                return;
            }
        }
        
        servicios.set(index, actualizado);
        modelo.setValueAt(actualizado.getId(), index, 0);
        modelo.setValueAt(actualizado.getNombre(), index, 1);
        modelo.setValueAt(actualizado.getPrecio(), index, 2);
        util.GuardarArchivo.guardarServicios(servicios);
        mostrarInfo("Servicio modificado correctamente");
    }//GEN-LAST:event_jButtonModificarActionPerformed

    private void jButtonBorrarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonBorrarActionPerformed
        // Borrar servicio seleccionado
        int fila = jTable1.getSelectedRow();
        
        if (fila < 0) {
            mostrarError("Seleccione un servicio");
            return;
        }
        
        int opcion = JOptionPane.showConfirmDialog(this, "¿Desea eliminar el servicio seleccionado?", "Confirmar", JOptionPane.YES_NO_OPTION);
        if (opcion != JOptionPane.YES_OPTION) {
            return;
        }
        
        int index = jTable1.convertRowIndexToModel(fila);
        servicios.remove(index);
        modelo.removeRow(index);
        util.GuardarArchivo.guardarServicios(servicios);
        mostrarInfo("Servicio eliminado correctamente");
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
            java.util.logging.Logger.getLogger(ventanaServicios.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ventanaServicios.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ventanaServicios.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ventanaServicios.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the dialog */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                ventanaServicios dialog = new ventanaServicios(new javax.swing.JFrame(), true);
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
    private javax.swing.JLabel jLabelId;
    private javax.swing.JLabel jLabelNombre;
    private javax.swing.JLabel jLabelPuesto;
    private javax.swing.JLabel jLabelTitulo;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable jTable1;
    private javax.swing.JTextField jTextFieldId;
    private javax.swing.JTextField jTextFieldNombre;
    private javax.swing.JTextField jTextFieldPuesto;
    // End of variables declaration//GEN-END:variables
}
