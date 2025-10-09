package util;

import conceptos.Cliente;
import conceptos.Mecanico;
import conceptos.Servicio;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;
import java.util.ArrayList;

/**
 * Clase para escribir archivos XML usando DOM
 * @author Matias
 */
public class EscritorXML {

    /**
     * Guarda la lista de clientes en el archivo XML
     * @param clientes Lista de clientes a guardar
     * @param rutaArchivo Ruta del archivo XML
     */
    public static void guardarClientes(ArrayList<Cliente> clientes, String rutaArchivo) {
        try {
            // Crear el documento XML
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            // Crear elemento raíz
            Element root = doc.createElement("clientes");
            doc.appendChild(root);

            // Agregar cada cliente
            for (Cliente c : clientes) {
                Element cliente = doc.createElement("cliente");
                cliente.setAttribute("id", c.getId());

                Element nombre = doc.createElement("nombre");
                nombre.setTextContent(c.getNombre());
                cliente.appendChild(nombre);

                Element placa = doc.createElement("placa");
                placa.setTextContent(c.getPlaca());
                cliente.appendChild(placa);

                Element telefono = doc.createElement("telefono");
                telefono.setTextContent(c.getTelefono());
                cliente.appendChild(telefono);

                Element email = doc.createElement("email");
                email.setTextContent(c.getEmail());
                cliente.appendChild(email);

                root.appendChild(cliente);
            }

            // Escribir el archivo
            escribirArchivo(doc, rutaArchivo);

        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Error al guardar clientes: " + e.getMessage());
        }
    }

    /**
     * Guarda la lista de mecánicos en el archivo XML
     * @param mecanicos Lista de mecánicos a guardar
     * @param rutaArchivo Ruta del archivo XML
     */
    public static void guardarMecanicos(ArrayList<Mecanico> mecanicos, String rutaArchivo) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            Element root = doc.createElement("mecanicos");
            doc.appendChild(root);

            for (Mecanico m : mecanicos) {
                Element mecanico = doc.createElement("mecanico");
                mecanico.setAttribute("id", m.getId());

                Element nombre = doc.createElement("nombre");
                nombre.setTextContent(m.getNombre());
                mecanico.appendChild(nombre);

                Element puesto = doc.createElement("puesto");
                puesto.setTextContent(m.getPuesto());
                mecanico.appendChild(puesto);

                Element servicios = doc.createElement("servicios");
                for (String idServicio : m.getServicios()) {
                    Element id = doc.createElement("id");
                    id.setTextContent(idServicio);
                    servicios.appendChild(id);
                }
                mecanico.appendChild(servicios);

                root.appendChild(mecanico);
            }

            escribirArchivo(doc, rutaArchivo);

        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Error al guardar mecánicos: " + e.getMessage());
        }
    }

    /**
     * Guarda la lista de servicios en el archivo XML
     * @param servicios Lista de servicios a guardar
     * @param rutaArchivo Ruta del archivo XML
     */
    public static void guardarServicios(ArrayList<Servicio> servicios, String rutaArchivo) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            Element root = doc.createElement("servicios");
            doc.appendChild(root);

            for (Servicio s : servicios) {
                Element servicio = doc.createElement("servicio");
                servicio.setAttribute("id", s.getId());

                Element nombre = doc.createElement("nombre");
                nombre.setTextContent(s.getNombre());
                servicio.appendChild(nombre);

                Element precio = doc.createElement("precio");
                precio.setTextContent(s.getPrecio());
                servicio.appendChild(precio);

                root.appendChild(servicio);
            }

            escribirArchivo(doc, rutaArchivo);

        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Error al guardar servicios: " + e.getMessage());
        }
    }

    /**
     * Método auxiliar para escribir el documento XML al archivo
     * @param doc Documento XML a escribir
     * @param rutaArchivo Ruta donde guardar el archivo
     */
    private static void escribirArchivo(Document doc, String rutaArchivo) throws Exception {
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();

        // Configurar formato de salida
        transformer.setOutputProperty(OutputKeys.ENCODING, "UTF-8");
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "4");

        DOMSource source = new DOMSource(doc);

        // Determinar la ruta completa del archivo
        String rutaCompleta = obtenerRutaCompleta(rutaArchivo);
        StreamResult result = new StreamResult(new File(rutaCompleta));

        transformer.transform(source, result);
        System.out.println("Archivo guardado exitosamente en: " + rutaCompleta);
    }

    /**
     * Obtiene la ruta completa del archivo en el directorio src
     * @param rutaRelativa Ruta relativa (ej: "data/clientes.xml")
     * @return Ruta completa del archivo
     */
    private static String obtenerRutaCompleta(String rutaRelativa) {
        // Obtener la ruta del proyecto
        String directorioProyecto = System.getProperty("user.dir");
        return directorioProyecto + "/src/" + rutaRelativa;
    }
}