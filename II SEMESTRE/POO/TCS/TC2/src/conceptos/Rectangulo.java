/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class Rectangulo {
    int ancho;
    int largo;

    public Rectangulo(int ancho, int largo) {
        this.ancho = ancho;
        this.largo = largo;
    }

    public Rectangulo(){
        this.ancho = 1;
        this.largo = 1;
    }

    public Rectangulo perimetro(Rectangulo rectangulo) {
        int perimetro;

        perimetro = 2 * (ancho + largo);

        return new Rectangulo(perimetro, 0);
    }

    public Rectangulo area(Rectangulo rectangulo) {
        int area;

        area = ancho * largo;

        return new Rectangulo(area, 0);
    }

    public boolean esCuadrado() {
        boolean cuadrado;
        if (ancho == largo) {
            cuadrado = true;
        } else {
            cuadrado = false;
        }
        return cuadrado;
    }

    public int getAncho() {
        return ancho;
    }
    public int getLargo() {
        return largo;
    }
    public void setAncho(int ancho) {
        if (ancho > 0.0 && ancho < 20.0) {
            this.ancho = ancho;
        } else {
            System.out.println("El ancho debe estar entre 0.0 y 20.0");
        }
    }
    public void setLargo(int Largo) {
        if (largo > 0.0 && largo < 20.0) {
            this.largo = largo;
        } else {
            System.out.println("El largo debe estar entre 0.0 y 20.0");
        }
    }
}
