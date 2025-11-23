/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.XMLReader;

/**
 * Cargador genérico de archivos XML usando parsers SAX
 * Soporta: cliente, mecanico, servicio, estado, solicitud
 * 
 * @author Matias
 */
public class cargadorXML {

    /**
     * Carga objetos desde un archivo XML usando el parser apropiado
     * InputStream del archivo XML
     * Tipo de objeto: "cliente", "mecanico", "servicio", "estado", "solicitud"
     * ArrayList con los objetos cargados
     */
    public static ArrayList<?> Cargar(InputStream input, String tipo) {
        try {
            // Configurar el parser SAX
            InputSource source = new InputSource(input);
            SAXParserFactory parserFactory = SAXParserFactory.newInstance();
            parserFactory.setNamespaceAware(true);
            SAXParser parser = parserFactory.newSAXParser();
            XMLReader reader = parser.getXMLReader();

            // Elegir el handler apropiado según el tipo
            if ("cliente".equals(tipo)) {
                clienteParserHandler handler = new clienteParserHandler();
                reader.setContentHandler(handler);
                reader.parse(source);
                return handler.getClientes();

            } else if ("mecanico".equals(tipo)) {
                mecanicoParserHandler handler = new mecanicoParserHandler();
                reader.setContentHandler(handler);
                reader.parse(source);
                return handler.getMecanicos();

            } else if ("servicio".equals(tipo)) {
                servicioParserHandler handler = new servicioParserHandler();
                reader.setContentHandler(handler);
                reader.parse(source);
                return handler.getServicios();

            } else if ("estado".equals(tipo)) {
                estadoParserHandler handler = new estadoParserHandler();
                reader.setContentHandler(handler);
                reader.parse(source);
                return handler.getEstados();

            } else if ("solicitud".equals(tipo)) {
                solicitudParserHandler handler = new solicitudParserHandler();
                reader.setContentHandler(handler);
                reader.parse(source);
                return handler.getSolicitudes();
            }

        } catch (SAXException | ParserConfigurationException | IOException e) {
            System.err.println("Error al cargar XML tipo '" + tipo + "': " + e.getMessage());
            e.printStackTrace();
        }

        // Si hay error o tipo desconocido, retornar lista vacía
        return new ArrayList<>();
    }
}