/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class Telefono {
    String color;
    double precio;
    double extensionCable;
    String formaMarcar;

    // Constructor sin parámetros
    public Telefono() {
    }

    // Constructor con parámetros
    public Telefono(String color, double precio, double extensionCable, String formaMarcar) {
        this.color = color;
        this.precio = precio;
        this.extensionCable = extensionCable;
        this.formaMarcar = formaMarcar;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public double getExtensionCable() {
        return extensionCable;
    }

    public void setExtensionCable(double extensionCable) {
        this.extensionCable = extensionCable;
    }

    public String getFormaMarcar() {
        return formaMarcar;
    }

    public void setFormaMarcar(String formaMarcar) {
        this.formaMarcar = formaMarcar;
    }
    
}
