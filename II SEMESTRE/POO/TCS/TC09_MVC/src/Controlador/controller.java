/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controlador;
import Vista.VentanaSumar;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import modelo.Suma;

/**
 *
 * @author Matias
 */
public class controller implements ActionListener {
    VentanaSumar vista;
    Suma modelo;

    public controller(VentanaSumar vista, Suma modelo) {
        this.vista = vista;
        this.modelo = modelo;
        this.vista.jButtonSumar.addActionListener(this);

    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        modelo.setN1(Integer.parseInt(vista.jTextN1.getText()));
        modelo.setN2(Integer.parseInt(vista.jTextN2.getText()));
        modelo.sumar();
        this.vista.jLabelResultado.setText(String.valueOf(modelo.getResultado()));
        
    }
    
    public void iniciar(){
        this.vista.setTitle("Operacion de Suma");
        this.vista.setLocationRelativeTo(null);
                
    }
}
