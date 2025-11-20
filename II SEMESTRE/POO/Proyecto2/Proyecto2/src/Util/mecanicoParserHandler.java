/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Mecanico;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import java.util.ArrayList;
import java.util.Stack;

/**
 *
 * @author Matias
 */
public class mecanicoParserHandler extends DefaultHandler {
    ArrayList<Mecanico> mecanicos = new ArrayList<>();
    Stack pilaElementos = new Stack();
    Stack pilaObjetos = new Stack();

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        pilaElementos.push(qName);
        if ("mecanico".equals(qName)) {
            Mecanico mecanico = new Mecanico();
            mecanico.setId(attributes.getValue("id"));
            pilaObjetos.push(mecanico);
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        pilaElementos.pop();
        if ("mecanico".equals(qName)) {
            Mecanico mecanico = (Mecanico) pilaObjetos.pop();
            mecanicos.add(mecanico);
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        String valor = new String(ch, start, length).trim();
        if (valor.length() == 0 || pilaObjetos.isEmpty()) return;

        if ("nombre".equals(elementoActual())) {
            Mecanico mecanico = (Mecanico) pilaObjetos.peek();
            mecanico.setNombre(valor);
        } else if ("puesto".equals(elementoActual())) {
            Mecanico mecanico = (Mecanico) pilaObjetos.peek();
            mecanico.setPuesto(valor);
        } else if ("id".equals(elementoActual()) && "servicios".equals(elementoPadre())) {
            Mecanico mecanico = (Mecanico) pilaObjetos.peek();
            mecanico.addServicio(valor);
        }
    }

    private String elementoActual() {
        return (String) pilaElementos.peek();
    }
    private String elementoPadre() {
        if (pilaElementos.size() < 2) return "";
        return (String) pilaElementos.get(pilaElementos.size() - 2);
    }
    public ArrayList<Mecanico> getMecanicos() { return mecanicos; }
}
