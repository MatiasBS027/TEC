/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.Cliente;
import Conceptos.Mecanico;
import Conceptos.Servicio;
import java.io.File;
import java.util.List;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

/**
 *
 * @author Corea
 */
public class GuardarArchivo {
    // Rutas de los archivos XML
    private static final String RUTA_CLIENTES = "src/data/clientes.xml";
    private static final String RUTA_MECANICOS = "src/data/mecanicos.xml";
    private static final String RUTA_SERVICIOS = "src/data/servicios.xml";
    // Método para guardar la lista de clientes en un archivo XML
    public static void guardarClientes(List<Cliente> clientes) {
        try {
            Document doc = crearDocumento();
            Element root = doc.createElement("clientes");
            doc.appendChild(root);
            
            for (Cliente cliente : clientes) {
                Element nodoCliente = doc.createElement("cliente");
                nodoCliente.setAttribute("id", cliente.getId());
                agregarNodoTexto(doc, nodoCliente, "nombre", cliente.getNombre());
                agregarNodoTexto(doc, nodoCliente, "placa", cliente.getPlaca());
                agregarNodoTexto(doc, nodoCliente, "telefono", cliente.getTelefono());
                agregarNodoTexto(doc, nodoCliente, "email", cliente.getEmail());
                root.appendChild(nodoCliente);
            }
            escribirDocumento(doc, RUTA_CLIENTES);
            
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IllegalStateException("Error al guardar clientes", ex);
        }
    }
    // Método para guardar la lista de mecánicos en un archivo XML
    public static void guardarMecanicos(List<Mecanico> mecanicos) {
        try {
            Document doc = crearDocumento();
            Element root = doc.createElement("mecanicos");
            doc.appendChild(root);
            
            for (Mecanico mecanico : mecanicos) {
                Element nodoMecanico = doc.createElement("mecanico");
                nodoMecanico.setAttribute("id", mecanico.getId());
                agregarNodoTexto(doc, nodoMecanico, "nombre", mecanico.getNombre());
                agregarNodoTexto(doc, nodoMecanico, "puesto", mecanico.getPuesto());
                Element servicios = doc.createElement("servicios");
                
                for (String idServicio : mecanico.getServicios()) {
                    agregarNodoTexto(doc, servicios, "id", idServicio);
                }
                nodoMecanico.appendChild(servicios);
                root.appendChild(nodoMecanico);
            }
            escribirDocumento(doc, RUTA_MECANICOS);
            
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IllegalStateException("Error al guardar mecanicos", ex);
        }
    }
    // Método para guardar la lista de servicios en un archivo XML
    public static void guardarServicios(List<Servicio> servicios) {
        try {
            Document doc = crearDocumento();
            Element root = doc.createElement("servicios");
            doc.appendChild(root);
            
            for (Servicio servicio : servicios) {
                Element nodoServicio = doc.createElement("servicio");
                nodoServicio.setAttribute("id", servicio.getId());
                agregarNodoTexto(doc, nodoServicio, "nombre", servicio.getNombre());
                agregarNodoTexto(doc, nodoServicio, "precio", servicio.getPrecio());
                root.appendChild(nodoServicio);
            }
            escribirDocumento(doc, RUTA_SERVICIOS);
            
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IllegalStateException("Error al guardar servicios", ex);
        }
    }
    // Métodos auxiliares para crear y escribir documentos XML
    private static Document crearDocumento() throws ParserConfigurationException {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        return builder.newDocument();
    }
    // Método para agregar un nodo de texto a un elemento padre
    private static void agregarNodoTexto(Document doc, Element padre, String nombre, String valor) {
        Element nodo = doc.createElement(nombre);
        nodo.appendChild(doc.createTextNode(valor == null ? "" : valor));
        padre.appendChild(nodo);
    }
    // Método para escribir el documento XML en un archivo
    private static void escribirDocumento(Document doc, String ruta) throws TransformerException {
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");
        DOMSource source = new DOMSource(doc);
        StreamResult result = new StreamResult(new File(ruta));
        transformer.transform(source, result);
    }
}
