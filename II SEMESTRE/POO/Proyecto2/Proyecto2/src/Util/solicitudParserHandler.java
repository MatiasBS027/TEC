/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Solicitud;
import java.util.ArrayList;
import java.util.Stack;
import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

/**
 * Parser SAX para leer solicitudes desde XML
 * Lee el archivo solicitudes.xml y crea objetos Solicitud
 * 
 * @author Matias 
 */
public class solicitudParserHandler extends DefaultHandler {
    
    private ArrayList<Solicitud> solicitudes = new ArrayList<>();
    private Stack<String> pilaElementos = new Stack<>();
    private Stack<Object> pilaObjetos = new Stack<>();
    
    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        pilaElementos.push(qName);
        
        if ("solicitud".equals(qName)) {
            Solicitud solicitud = new Solicitud();
            solicitud.setId(attributes.getValue("id"));
            pilaObjetos.push(solicitud);
        }
    }
    
    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        pilaElementos.pop();
        
        if ("solicitud".equals(qName)) {
            Solicitud solicitud = (Solicitud) pilaObjetos.pop();
            solicitudes.add(solicitud);
        }
    }
    
    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        String valor = new String(ch, start, length).trim();
        
        if (valor.length() == 0 || pilaObjetos.isEmpty()) {
            return;
        }
        
        Solicitud solicitud = (Solicitud) pilaObjetos.peek();
        String elemento = elementoActual();
        
        switch (elemento) {
            case "placa":
                solicitud.setPlaca(valor);
                break;
            case "servicio":
                solicitud.setIdServicio(valor);
                break;
            case "cliente":
                solicitud.setIdCliente(valor);
                break;
            case "mecanico":
                solicitud.setIdMecanico(valor);
                break;
            case "estado":
                solicitud.setIdEstado(valor);
                break;
            case "observaciones":
                solicitud.setObservaciones(valor);
                break;
            case "id":
                // Solo agregar si estamos dentro de "otros_servicios"
                if ("otros_servicios".equals(elementoPadre())) {
                    solicitud.addOtroServicio(valor);
                }
                break;
        }
    }
    
    private String elementoActual() {
        return pilaElementos.isEmpty() ? "" : pilaElementos.peek();
    }
    
    private String elementoPadre() {
        if (pilaElementos.size() < 2) return "";
        return pilaElementos.get(pilaElementos.size() - 2);
    }
    
    public ArrayList<Solicitud> getSolicitudes() {
        return solicitudes;
    }
}
