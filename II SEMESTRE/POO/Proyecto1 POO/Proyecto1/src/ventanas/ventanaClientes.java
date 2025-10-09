
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JDialog.java to edit this template
 */
package ventanas;

import conceptos.Cliente;
import util.GestorClientes;

import javax.swing.table.DefaultTableModel;
import javax.swing.JOptionPane;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.util.ArrayList;
import java.util.Vector;

/**
 * Ventana para gestionar clientes
 * @author Matias
 */

public class ventanaClientes extends javax.swing.JDialog {

    //Instancia del gestor
    private GestorClientes gestor;

    public ventanaClientes(java.awt.Frame parent, boolean modal) {
        super(parent, modal);
        initComponents();
        
        // NUEVO: Inicializar el gestor
        gestor = new GestorClientes();
        
        llenarTabla();
        
        // Obtener el tamaño de la pantalla
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        this.setSize(screenSize);
        
        // NUEVO: Agregar listener para selección de tabla
        jTable1.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) {
                cargarClienteSeleccionado();
            }
        });
    }
    /**
     * Llena la tabla con todos los clientes del gestor
     */
    private void llenarTabla(){
        // MODIFICADO: Usa el gestor en lugar de cargar directo del XML
        ArrayList<Cliente> clientes = gestor.obtenerTodos();
        
        Vector<String> columnas = new Vector<>();
        columnas.add("ID");
        columnas.add("Nombre");
        columnas.add("Placa");
        columnas.add("Telefono");
        columnas.add("Email");

        Vector<Vector<String>> filas = new Vector<>();
        for(Cliente c : clientes){
            Vector<String> fila = new Vector<>();
            fila.add(c.getId());
            fila.add(c.getNombre());
            fila.add(c.getPlaca());
            fila.add(c.getTelefono());
            fila.add(c.getEmail());
            filas.add(fila);
        }
        DefaultTableModel datos = new DefaultTableModel(filas, columnas);
        this.jTable1.setModel(datos);
    }
    
    /**
     * Carga los datos del cliente seleccionado en la tabla a los campos
     */
    private void cargarClienteSeleccionado() {
        int filaSeleccionada = jTable1.getSelectedRow();
        if (filaSeleccionada != -1) {
            String id = jTable1.getValueAt(filaSeleccionada, 0).toString();
            Cliente cliente = gestor.buscarPorId(id);
            
            if (cliente != null) {
                jTextFieldId.setText(cliente.getId());
                jTextFieldNombre.setText(cliente.getNombre());
                jTextFieldPlaca.setText(cliente.getPlaca());
                jTextFieldTelefono.setText(cliente.getTelefono());
                jTextFieldEmail.setText(cliente.getEmail());
            }
        }
    }
    
    /**
     * Limpia todos los campos del formulario
     */
    private void limpiarCampos() {
        jTextFieldId.setText("");
        jTextFieldNombre.setText("");
        jTextFieldPlaca.setText("");
        jTextFieldTelefono.setText("");
        jTextFieldEmail.setText("");
        jTable1.clearSelection();
    }
    
    /**
     * Valida que todos los campos estén llenos
     * @return true si son válidos, false si no
     */
    private boolean validarCampos() {
        if (jTextFieldId.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "El ID es obligatorio", "Error", JOptionPane.ERROR_MESSAGE);
            jTextFieldId.requestFocus();
            return false;
        }
        if (jTextFieldNombre.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "El nombre es obligatorio", "Error", JOptionPane.ERROR_MESSAGE);
            jTextFieldNombre.requestFocus();
            return false;
        }
        if (jTextFieldPlaca.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "La placa es obligatoria", "Error", JOptionPane.ERROR_MESSAGE);
            jTextFieldPlaca.requestFocus();
            return false;
        }
        if (jTextFieldTelefono.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "El teléfono es obligatorio", "Error", JOptionPane.ERROR_MESSAGE);
            jTextFieldTelefono.requestFocus();
            return false;
        }
        if (jTextFieldEmail.getText().trim().isEmpty()) {
            JOptionPane.showMessageDialog(this, "El email es obligatorio", "Error", JOptionPane.ERROR_MESSAGE);
            jTextFieldEmail.requestFocus();
            return false;
        }
        return true;
    }

    /**
     * Crea un objeto Cliente desde los campos del formulario
     */
    private Cliente obtenerClienteDeFormulario() {
        Cliente cliente = new Cliente();
        cliente.setId(jTextFieldId.getText().trim());
        cliente.setNombre(jTextFieldNombre.getText().trim());
        cliente.setPlaca(jTextFieldPlaca.getText().trim());
        cliente.setTelefono(jTextFieldTelefono.getText().trim());
        cliente.setEmail(jTextFieldEmail.getText().trim());
        return cliente;
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
        jLabelPlaca = new javax.swing.JLabel();
        jTextFieldPlaca = new javax.swing.JTextField();
        jLabelTelefono = new javax.swing.JLabel();
        jTextFieldTelefono = new javax.swing.JTextField();
        jLabelEmail = new javax.swing.JLabel();
        jTextFieldEmail = new javax.swing.JTextField();
        jButtonModificar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        jButtonSalir = new javax.swing.JButton();
        jButtonNuevo = new javax.swing.JButton();
        jButtonBorrar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        jLabelTitulo.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabelTitulo.setText("Clientes");

        jLabelId.setText("ID");

        jTextFieldId.setColumns(12);

        jLabelNombre.setText("Nombre");

        jTextFieldNombre.setColumns(15);

        jLabelPlaca.setText("Placa");

        jTextFieldPlaca.setColumns(12);

        jLabelTelefono.setText("Telefono");

        jTextFieldTelefono.setColumns(15);

        jLabelEmail.setText("Email");

        jTextFieldEmail.setColumns(15);

        jButtonModificar.setText("Modificar");
        jButtonModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonModificarActionPerformed(evt);
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

        jButtonNuevo.setText("Nuevo");
        jButtonNuevo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonNuevoActionPerformed(evt);
            }
        });

        jButtonBorrar.setText("Borrar");
        jButtonBorrar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonBorrarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(6, 6, 6)
                .addComponent(jLabelTitulo, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                .addGap(6, 6, 6))
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabelEmail)
                            .addComponent(jLabelPlaca)
                            .addComponent(jLabelId))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jTextFieldId, javax.swing.GroupLayout.DEFAULT_SIZE, 170, Short.MAX_VALUE)
                            .addComponent(jTextFieldPlaca, javax.swing.GroupLayout.DEFAULT_SIZE, 170, Short.MAX_VALUE)
                            .addComponent(jTextFieldEmail, javax.swing.GroupLayout.DEFAULT_SIZE, 170, Short.MAX_VALUE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabelTelefono)
                            .addComponent(jLabelNombre))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jTextFieldNombre, javax.swing.GroupLayout.DEFAULT_SIZE, 190, Short.MAX_VALUE)
                            .addComponent(jTextFieldTelefono, javax.swing.GroupLayout.DEFAULT_SIZE, 190, Short.MAX_VALUE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButtonModificar, javax.swing.GroupLayout.DEFAULT_SIZE, 90, Short.MAX_VALUE)
                            .addComponent(jButtonNuevo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jButtonBorrar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
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
                    .addComponent(jLabelPlaca)
                    .addComponent(jTextFieldPlaca, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabelTelefono)
                    .addComponent(jTextFieldTelefono, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButtonModificar))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabelEmail)
                    .addComponent(jTextFieldEmail, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButtonBorrar))
                .addGap(18, 18, 18)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 176, Short.MAX_VALUE)
                .addGap(18, 18, 18)
                .addComponent(jButtonSalir)
                .addGap(20, 20, 20))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents
    // ============ EVENTOS DE BOTONES ============
    
    /**
     * NUEVO: Agrega un nuevo cliente
     */
    private void jButtonSalirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonSalirActionPerformed
        dispose();
    }//GEN-LAST:event_jButtonSalirActionPerformed

    private void jButtonModificarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonModificarActionPerformed
        int filaSeleccionada = jTable1.getSelectedRow();
        if (filaSeleccionada == -1) {
            JOptionPane.showMessageDialog(this, 
                "Debe seleccionar un cliente de la tabla", 
                "Advertencia", 
                JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        if (!validarCampos()) {
            return;
        }
        
        String idOriginal = jTable1.getValueAt(filaSeleccionada, 0).toString();
        Cliente clienteModificado = obtenerClienteDeFormulario();
        
        if (gestor.modificar(idOriginal, clienteModificado)) {
            JOptionPane.showMessageDialog(this, 
                "Cliente modificado exitosamente", 
                "Éxito", 
                JOptionPane.INFORMATION_MESSAGE);
            limpiarCampos();
            llenarTabla();
        } else {
            JOptionPane.showMessageDialog(this, 
                "Error al modificar el cliente", 
                "Error", 
                JOptionPane.ERROR_MESSAGE);
        }
    }//GEN-LAST:event_jButtonModificarActionPerformed

    private void jButtonNuevoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonNuevoActionPerformed
        if (!validarCampos()) {
            return;
        }
        
        Cliente nuevoCliente = obtenerClienteDeFormulario();
        
        if (gestor.agregar(nuevoCliente)) {
            JOptionPane.showMessageDialog(this, 
                "Cliente agregado exitosamente", 
                "Éxito", 
                JOptionPane.INFORMATION_MESSAGE);
            limpiarCampos();
            llenarTabla();
        } else {
            JOptionPane.showMessageDialog(this, 
                "Ya existe un cliente con ese ID", 
                "Error", 
                JOptionPane.ERROR_MESSAGE);
        }
    }//GEN-LAST:event_jButtonNuevoActionPerformed

    private void jButtonBorrarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonBorrarActionPerformed
        int filaSeleccionada = jTable1.getSelectedRow();
        if (filaSeleccionada == -1) {
            JOptionPane.showMessageDialog(this, 
                "Debe seleccionar un cliente de la tabla", 
                "Advertencia", 
                JOptionPane.WARNING_MESSAGE);
            return;
        }
        
        String id = jTable1.getValueAt(filaSeleccionada, 0).toString();
        String nombre = jTable1.getValueAt(filaSeleccionada, 1).toString();
        
        int confirmacion = JOptionPane.showConfirmDialog(this, 
                "¿Está seguro de eliminar al cliente '" + nombre + "'?", 
                "Confirmar eliminación", 
                JOptionPane.YES_NO_OPTION,
                JOptionPane.QUESTION_MESSAGE);
        
        if (confirmacion == JOptionPane.YES_OPTION) {
            if (gestor.eliminar(id)) {
                JOptionPane.showMessageDialog(this, 
                    "Cliente eliminado exitosamente", 
                    "Éxito", 
                    JOptionPane.INFORMATION_MESSAGE);
                limpiarCampos();
                llenarTabla();
            } else {
                JOptionPane.showMessageDialog(this, 
                    "Error al eliminar el cliente", 
                    "Error", 
                    JOptionPane.ERROR_MESSAGE);
            }
        }
    }//GEN-LAST:event_jButtonBorrarActionPerformed

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
            java.util.logging.Logger.getLogger(ventanaClientes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ventanaClientes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ventanaClientes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ventanaClientes.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the dialog */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                ventanaClientes dialog = new ventanaClientes(new javax.swing.JFrame(), true);
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
    private javax.swing.JButton jButtonModificar;
    private javax.swing.JButton jButtonNuevo;
    private javax.swing.JButton jButtonSalir;
    private javax.swing.JLabel jLabelEmail;
    private javax.swing.JLabel jLabelId;
    private javax.swing.JLabel jLabelNombre;
    private javax.swing.JLabel jLabelPlaca;
    private javax.swing.JLabel jLabelTelefono;
    private javax.swing.JLabel jLabelTitulo;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTable jTable1;
    private javax.swing.JTextField jTextFieldEmail;
    private javax.swing.JTextField jTextFieldId;
    private javax.swing.JTextField jTextFieldNombre;
    private javax.swing.JTextField jTextFieldPlaca;
    private javax.swing.JTextField jTextFieldTelefono;
    // End of variables declaration//GEN-END:variables
}
