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
 *
 * @author Matias
 */
public class cargadorXML {
    // tipo puede ser "cliente", "mecanico" o "servicio"
    public static ArrayList<?> Cargar(InputStream input, String tipo) {
        try {
            InputSource source = new InputSource(input);
            SAXParserFactory parserFactory = SAXParserFactory.newInstance();
            parserFactory.setNamespaceAware(true);
            SAXParser parser = parserFactory.newSAXParser();
            XMLReader reader = parser.getXMLReader();

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
            }
            
        } catch (SAXException | ParserConfigurationException | IOException e) {
            e.printStackTrace();
        }
        return new ArrayList<>();
    }
}