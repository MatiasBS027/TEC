/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package conceptos;

import java.util.ArrayList;
/**
 *
 * @author Matias
 */
public class Expediente {
    private String referencia;
    Animal mascota;
    ArrayList<Antecedente> antecedentes;

    public Expediente(String referencia, Animal mascota) {
        this.referencia = referencia;
        this.mascota = mascota;
        this.antecedentes = new ArrayList<>();
    }

    public Expediente() {
        this.antecedentes = new ArrayList<>();
    }
    public void agregarAntecedente(Antecedente antecedente) {
        this.antecedentes.add(antecedente);
    }
    public void quitarAntecedente(Antecedente antecedente) {
        this.antecedentes.remove(antecedente);
    }
    public String getReferencia() {
        return referencia;
    }
    public void setReferencia(String referencia) {
        this.referencia = referencia;
    }
    public Animal getMascota() {
        return mascota;
    }
    public void setMascota(Animal mascota) {
        this.mascota = mascota;
    }
}
