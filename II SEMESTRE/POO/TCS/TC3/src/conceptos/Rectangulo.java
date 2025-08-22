/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class Rectangulo extends FiguraRegular {

    public Rectangulo() {
        super.agregarLado(0); //ancho = 0
        super.agregarLado(0); //largo = 0
        super.agregarLado(0); //ancho = 0
        super.agregarLado(0); //largo = 0
    }

    public Rectangulo(int ancho, int largo) {
        super.agregarLado(ancho);
        super.agregarLado(largo);
        super.agregarLado(ancho);
        super.agregarLado(largo);
    }

    public int getAncho() {
        return this.lados.get(0);
    }

    public int getLargo() {
        return this.lados.get(1);
    }

    public void setAncho(int ancho) {
        this.lados.set(0, ancho);
        this.lados.set(2, ancho);
    }

    public void setLargo(int largo) {
        this.lados.set(1, largo);
        this.lados.set(3, largo);
    }

    public int area() {
        return this.getAncho() * this.getLargo();
    }
    
}
