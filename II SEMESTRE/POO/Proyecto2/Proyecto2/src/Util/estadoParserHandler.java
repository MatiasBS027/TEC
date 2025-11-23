/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Estado;
import java.util.ArrayList;
import java.util.Stack;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

/**
 * Parser SAX para leer estados desde XML
 * Lee el archivo estados.xml y crea objetos Estado
 * 
 * @author Matias 
 */
public class estadoParserHandler extends DefaultHandler {
    
    private ArrayList<Estado> estados = new ArrayList<>();
    private Stack<String> pilaElementos = new Stack<>();
    private Stack<Object> pilaObjetos = new Stack<>();
    
    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        pilaElementos.push(qName);
        
        if ("estado".equals(qName)) {
            Estado estado = new Estado();
            estado.setId(attributes.getValue("id"));
            pilaObjetos.push(estado);
        }
    }
    
    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        pilaElementos.pop();
        
        if ("estado".equals(qName)) {
            Estado estado = (Estado) pilaObjetos.pop();
            estados.add(estado);
        }
    }
    
    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        String valor = new String(ch, start, length).trim();
        
        if (valor.length() == 0 || pilaObjetos.isEmpty()) {
            return;
        }
        
        if ("nombre".equals(elementoActual())) {
            Estado estado = (Estado) pilaObjetos.peek();
            estado.setNombre(valor);
        }
    }
    
    private String elementoActual() {
        return pilaElementos.isEmpty() ? "" : pilaElementos.peek();
    }
    
    public ArrayList<Estado> getEstados() {
        return estados;
    }
}