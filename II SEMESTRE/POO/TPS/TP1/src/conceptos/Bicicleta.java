/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;
import util.Direccion;
/**
 *
 * @author Matias
 */

public class Bicicleta {
    String tipoSillin;
    int numRadios;
    float diamRueda;

    // Constructor sin parámetros
    public Bicicleta() {
    }

    // Constructor con parámetros
    public Bicicleta(String tipoSillin, int numRadios, float diamRueda) {
        this.tipoSillin = tipoSillin;
        this.numRadios = numRadios;
        this.diamRueda = diamRueda;
    }

    public void girar(Direccion direccion) {
        System.out.println("Girar a la " + direccion);
    }

    public String getTipoSillin() {
        return tipoSillin;
    }
    public void setTipoSillin(String tipoSillin) {
        this.tipoSillin = tipoSillin;
    }
    public int getNumRadios() {
        return numRadios;
    }
    public void setNumRadios(int numRadios) {
        this.numRadios = numRadios;
    }
    public float getDiamRueda() {
        return diamRueda;
    }
    public void setDiamRueda(float diamRueda) {
        this.diamRueda = diamRueda;
    }

}
