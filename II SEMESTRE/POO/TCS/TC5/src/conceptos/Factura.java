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
public class Factura {
    public String referencia;
    Diagnostico diagnostico;
    ArrayList<ElementoFactura> items;
    public Factura (String referencia, Diagnostico diagnostico) {
        this.diagnostico = diagnostico;
        this.referencia = referencia;
        this.items = new ArrayList<>();
    }

    public Factura() {
        this.items = new ArrayList<>();
    }

    public void agregarItem(ElementoFactura item) {
        this.items.add(item);
    }

    public void quitarItem(ElementoFactura item) {
        this.items.remove(item);
    }

    public float totalizar() {
        float total = 0;
        for (ElementoFactura item : items) {
            total += item.precio * item.cantidad;
        }
        return total;
    }
}
