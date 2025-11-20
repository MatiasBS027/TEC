/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;
import Conceptos.Servicio;
import java.util.ArrayList;
import java.util.Stack;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

/**
 *
 * @author Matias
 */

public class servicioParserHandler extends DefaultHandler {
    ArrayList<Servicio> servicios = new ArrayList<>();
    Stack pilaElementos = new Stack();
    Stack pilaObjetos = new Stack();

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        pilaElementos.push(qName);
        if ("servicio".equals(qName)) {
            Servicio servicio = new Servicio();
            servicio.setId(attributes.getValue("id"));
            pilaObjetos.push(servicio);
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        pilaElementos.pop();
        if ("servicio".equals(qName)) {
            Servicio servicio = (Servicio) pilaObjetos.pop();
            servicios.add(servicio);
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        String valor = new String(ch, start, length).trim();
        if (valor.length() == 0 || pilaObjetos.isEmpty()) return;

        Servicio servicio = (Servicio) pilaObjetos.peek();
        if ("nombre".equals(elementoActual())) {
            servicio.setNombre(valor);
        } else if ("precio".equals(elementoActual())) {
            servicio.setPrecio(valor);
        }
    }

    private String elementoActual() {
        return (String) pilaElementos.peek();
    }

    public ArrayList<Servicio> getServicios() {
        return servicios;
    }
}

