/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.*;
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
 * Clase para guardar objetos en archivos XML
 * Usada SOLO para la operación EXPORTAR
 * 
 * @author Matias 
 * 
 */
public class GuardarArchivo {
    
    // Rutas de los archivos XML (en src/export/)
    private static final String RUTA_CLIENTES = "src/export/clientes.xml";
    private static final String RUTA_MECANICOS = "src/export/mecanicos.xml";
    private static final String RUTA_SERVICIOS = "src/export/servicios.xml";
    private static final String RUTA_ESTADOS = "src/export/estados.xml";
    private static final String RUTA_SOLICITUDES = "src/export/solicitudes.xml";
    
    /**
     * Guarda la lista de clientes en un archivo XML
     * Lista de clientes a guardar
     */
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
    
    /**
     * Guarda la lista de mecánicos en un archivo XML
     * Lista de mecánicos a guardar
     */
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
    
    /**
     * Guarda la lista de servicios en un archivo XML
     * Lista de servicios a guardar
     */
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
    
    /**
     * Guarda la lista de estados en un archivo XML
     * Lista de estados a guardar
     */
    public static void guardarEstados(List<Estado> estados) {
        try {
            Document doc = crearDocumento();
            Element root = doc.createElement("estados");
            doc.appendChild(root);
            
            for (Estado estado : estados) {
                Element nodoEstado = doc.createElement("estado");
                nodoEstado.setAttribute("id", estado.getId());
                agregarNodoTexto(doc, nodoEstado, "nombre", estado.getNombre());
                root.appendChild(nodoEstado);
            }
            escribirDocumento(doc, RUTA_ESTADOS);
            
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IllegalStateException("Error al guardar estados", ex);
        }
    }
    
    /**
     * Guarda la lista de solicitudes en un archivo XML
     * Lista de solicitudes a guardar
     */
    public static void guardarSolicitudes(List<Solicitud> solicitudes) {
        try {
            Document doc = crearDocumento();
            Element root = doc.createElement("solicitudes");
            doc.appendChild(root);
            
            for (Solicitud solicitud : solicitudes) {
                Element nodoSolicitud = doc.createElement("solicitud");
                nodoSolicitud.setAttribute("id", solicitud.getId());
                
                agregarNodoTexto(doc, nodoSolicitud, "placa", solicitud.getPlaca());
                agregarNodoTexto(doc, nodoSolicitud, "servicio", solicitud.getIdServicio());
                agregarNodoTexto(doc, nodoSolicitud, "cliente", solicitud.getIdCliente());
                agregarNodoTexto(doc, nodoSolicitud, "mecanico", 
                    solicitud.getIdMecanico() != null ? solicitud.getIdMecanico() : "");
                agregarNodoTexto(doc, nodoSolicitud, "estado", solicitud.getIdEstado());
                agregarNodoTexto(doc, nodoSolicitud, "observaciones", 
                    solicitud.getObservaciones() != null ? solicitud.getObservaciones() : "");
                
                // Otros servicios
                Element otrosServicios = doc.createElement("otros_servicios");
                if (solicitud.getOtrosServicios() != null) {
                    for (String idServicio : solicitud.getOtrosServicios()) {
                        agregarNodoTexto(doc, otrosServicios, "id", idServicio);
                    }
                }
                nodoSolicitud.appendChild(otrosServicios);
                
                root.appendChild(nodoSolicitud);
            }
            escribirDocumento(doc, RUTA_SOLICITUDES);
            
        } catch (ParserConfigurationException | TransformerException ex) {
            throw new IllegalStateException("Error al guardar solicitudes", ex);
        }
    }
    
    // ==================== MÉTODOS AUXILIARES ====================
    
    /**
     * Crea un nuevo documento XML vacío
     * Documento XML
     * ParserConfigurationException Si hay error en la configuración
     */
    private static Document crearDocumento() throws ParserConfigurationException {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        return builder.newDocument();
    }
    
    /**
     * Agrega un nodo de texto a un elemento padre
     * Documento XML
     * Elemento padre
     * Nombre del nodo
     * Valor del nodo
     */
    private static void agregarNodoTexto(Document doc, Element padre, String nombre, String valor) {
        Element nodo = doc.createElement(nombre);
        nodo.appendChild(doc.createTextNode(valor == null ? "" : valor));
        padre.appendChild(nodo);
    }
    
    /**
     * Escribe el documento XML en un archivo
     * Documento XML
     * Ruta del archivo
     * TransformerException Si hay error al escribir
     */
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