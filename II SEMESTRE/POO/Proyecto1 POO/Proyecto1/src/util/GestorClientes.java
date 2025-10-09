/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package util;

import conceptos.Cliente;
import java.io.InputStream;
import java.util.ArrayList;

/**
 * Gestor para operaciones CRUD de Clientes
 * Maneja la carga y guardado de datos en XML
 * @author Matias
 */
public class GestorClientes {
    
    private ArrayList<Cliente> clientes;
    private final String RUTA_XML = "data/clientes.xml";
    
    /**
     * Constructor que carga automáticamente los clientes del XML
     */
    public GestorClientes() {
        cargarDatos();
    }
    
    /**
     * Carga los clientes desde el archivo XML usando SAX
     */
    private void cargarDatos() {
        try {
            InputStream is = getClass().getClassLoader().getResourceAsStream(RUTA_XML);
            if (is == null) {
                throw new RuntimeException("No se encontró el archivo: " + RUTA_XML);
            }
            clientes = (ArrayList<Cliente>) cargadorXML.Cargar(is, "cliente");
            System.out.println("Clientes cargados: " + clientes.size());
        } catch (Exception e) {
            e.printStackTrace();
            clientes = new ArrayList<>();
        }
    }
    
    /**
     * Guarda los clientes en el archivo XML usando DOM
     */
    private void guardarDatos() {
        try {
            EscritorXML.guardarClientes(clientes, RUTA_XML);
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Error al guardar los datos: " + e.getMessage());
        }
    }
    
    /**
     * Obtiene todos los clientes
     * @return Lista de todos los clientes
     */
    public ArrayList<Cliente> obtenerTodos() {
        return new ArrayList<>(clientes); // Retorna copia para seguridad
    }
    
    /**
     * Busca un cliente por su ID
     * @param id ID del cliente a buscar
     * @return Cliente encontrado o null si no existe
     */
    public Cliente buscarPorId(String id) {
        for (Cliente c : clientes) {
            if (c.getId().equals(id)) {
                return c;
            }
        }
        return null;
    }
    
    /**
     * Verifica si existe un cliente con el ID dado
     * @param id ID a verificar
     * @return true si existe, false si no
     */
    public boolean existe(String id) {
        return buscarPorId(id) != null;
    }
    
    /**
     * Agrega un nuevo cliente
     * @param cliente Cliente a agregar
     * @return true si se agregó exitosamente, false si ya existe
     */
    public boolean agregar(Cliente cliente) {
        // Verificar que no exista ya
        if (existe(cliente.getId())) {
            System.out.println("Error: Ya existe un cliente con el ID " + cliente.getId());
            return false;
        }
        
        clientes.add(cliente);
        guardarDatos();
        System.out.println("Cliente agregado: " + cliente.getNombre());
        return true;
    }
    
    /**
     * Modifica un cliente existente
     * @param id ID del cliente a modificar
     * @param clienteModificado Cliente con los nuevos datos
     * @return true si se modificó exitosamente, false si no existe
     */
    public boolean modificar(String id, Cliente clienteModificado) {
        for (int i = 0; i < clientes.size(); i++) {
            if (clientes.get(i).getId().equals(id)) {
                clientes.set(i, clienteModificado);
                guardarDatos();
                System.out.println("Cliente modificado: " + clienteModificado.getNombre());
                return true;
            }
        }
        System.out.println("Error: No se encontró el cliente con ID " + id);
        return false;
    }
    
    /**
     * Elimina un cliente por su ID
     * @param id ID del cliente a eliminar
     * @return true si se eliminó exitosamente, false si no existe
     */
    public boolean eliminar(String id) {
        for (int i = 0; i < clientes.size(); i++) {
            if (clientes.get(i).getId().equals(id)) {
                Cliente eliminado = clientes.remove(i);
                guardarDatos();
                System.out.println("Cliente eliminado: " + eliminado.getNombre());
                return true;
            }
        }
        System.out.println("Error: No se encontró el cliente con ID " + id);
        return false;
    }
    
    /**
     * Busca clientes por nombre (búsqueda parcial)
     * @param nombre Nombre o parte del nombre a buscar
     * @return Lista de clientes que coinciden
     */
    public ArrayList<Cliente> buscarPorNombre(String nombre) {
        ArrayList<Cliente> resultado = new ArrayList<>();
        String nombreBusqueda = nombre.toLowerCase();
        
        for (Cliente c : clientes) {
            if (c.getNombre().toLowerCase().contains(nombreBusqueda)) {
                resultado.add(c);
            }
        }
        return resultado;
    }
    
    /**
     * Busca clientes por placa
     * @param placa Placa a buscar
     * @return Cliente encontrado o null
     */
    public Cliente buscarPorPlaca(String placa) {
        for (Cliente c : clientes) {
            if (c.getPlaca().equalsIgnoreCase(placa)) {
                return c;
            }
        }
        return null;
    }
    
    /**
     * Recarga los datos desde el XML (útil si el archivo cambió externamente)
     */
    public void recargar() {
        cargarDatos();
        System.out.println("Datos recargados desde XML");
    }
}
