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
public class FiguraRegular {
    ArrayList<Integer> lados = new ArrayList();

    public void agregarLado(int lado) {
        this.lados.add(lado);
    }

    public int perimetro() {
        int resultado = 0;
        for (int lado : this.lados) {
            resultado += lado;
        }
        return resultado;
    }

}
