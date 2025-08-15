/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

/**
 *
 * @author Matias
 */
public class Walkman {
    String color;
    String marca;
    String tipoDisquette;
    String[] listaBotones;

    // Constructor sin parámetros
    public Walkman() {
    }

    // Constructor con parámetros
    public Walkman(String color, String marca, String tipoDisquette, String[] listaBotones) {
        this.color = color;
        this.marca = marca;
        this.tipoDisquette = tipoDisquette;
        this.listaBotones = listaBotones;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTipoDisquette() {
        return tipoDisquette;
    }

    public void setTipoDisquette(String tipoDisquette) {
        this.tipoDisquette = tipoDisquette;
    }

    public String[] getListaBotones() {
        return listaBotones;
    }

    public void setListaBotones(String[] listaBotones) {
        this.listaBotones = listaBotones;
    }
}
