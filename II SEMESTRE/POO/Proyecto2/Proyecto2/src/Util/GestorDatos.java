/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Util;

import Conceptos.*;
import java.util.ArrayList;

/**
 * Gestiona TODOS los datos del sistema
 * Mantiene los ArrayLists en memoria y coordina la carga/guardado
 * con archivos .DAT
 * 
 * @author Matias Benavides (2025102376)
 */
public class GestorDatos {

    private static GestorDatos instancia;

    // ArrayLists principales (estos viven en memoria)
    private ArrayList<Cliente> clientes;
    private ArrayList<Servicio> servicios;
    private ArrayList<Mecanico> mecanicos;
    private ArrayList<Solicitud> solicitudes;
    private ArrayList<Estado> estados;

    // Nombres de archivos .DAT
    private static final String ARCHIVO_CLIENTES = "CLIENTES.DAT";
    private static final String ARCHIVO_SERVICIOS = "SERVICIOS.DAT";
    private static final String ARCHIVO_MECANICOS = "MECANICOS.DAT";
    private static final String ARCHIVO_SOLICITUDES = "SOLICITUDES.DAT";
    private static final String ARCHIVO_ESTADOS = "ESTADOS.DAT";

    /**
     * Constructor privado (patrón Singleton)
     * Carga los datos desde archivos .DAT al iniciar
     */
    private GestorDatos() {
        asegurarArchivos();
        cargarTodosDatos();
    }

    /**
     * Obtiene la instancia única del GestorDatos
     * 
     * @return Instancia del gestor
     */
    public static GestorDatos getInstancia() {
        if (instancia == null) {
            instancia = new GestorDatos();
        }
        return instancia;
    }

    /**
     * Carga TODOS los datos desde archivos .DAT
     * Si no existen los archivos, crea listas vacías
     */
    private void cargarTodosDatos() {
        clientes = SerializacionUtil.cargarLista(ARCHIVO_CLIENTES);
        servicios = SerializacionUtil.cargarLista(ARCHIVO_SERVICIOS);
        mecanicos = SerializacionUtil.cargarLista(ARCHIVO_MECANICOS);
        solicitudes = SerializacionUtil.cargarLista(ARCHIVO_SOLICITUDES);
        estados = SerializacionUtil.cargarLista(ARCHIVO_ESTADOS);

        System.out.println("Datos cargados desde .DAT:");
        System.out.println("- Clientes: " + clientes.size());
        System.out.println("- Servicios: " + servicios.size());
        System.out.println("- Mecánicos: " + mecanicos.size());
        System.out.println("- Solicitudes: " + solicitudes.size());
        System.out.println("- Estados: " + estados.size());
    }

    private void asegurarArchivos() {
        SerializacionUtil.crearArchivoSiNoExiste(ARCHIVO_CLIENTES);
        SerializacionUtil.crearArchivoSiNoExiste(ARCHIVO_SERVICIOS);
        SerializacionUtil.crearArchivoSiNoExiste(ARCHIVO_MECANICOS);
        SerializacionUtil.crearArchivoSiNoExiste(ARCHIVO_SOLICITUDES);
        SerializacionUtil.crearArchivoSiNoExiste(ARCHIVO_ESTADOS);
    }

    // ==================== GETTERS DE LAS LISTAS ====================

    public ArrayList<Cliente> getClientes() {
        return clientes;
    }

    public ArrayList<Servicio> getServicios() {
        return servicios;
    }

    public ArrayList<Mecanico> getMecanicos() {
        return mecanicos;
    }

    public ArrayList<Solicitud> getSolicitudes() {
        return solicitudes;
    }

    public ArrayList<Estado> getEstados() {
        return estados;
    }

    // ==================== MÉTODOS DE GUARDADO ====================

    /**
     * Guarda TODOS los datos en sus archivos .DAT
     * 
     * @return true si todo se guardó correctamente
     */
    public boolean guardarTodosDatos() {
        boolean exito = true;
        exito &= SerializacionUtil.guardarLista(clientes, ARCHIVO_CLIENTES);
        exito &= SerializacionUtil.guardarLista(servicios, ARCHIVO_SERVICIOS);
        exito &= SerializacionUtil.guardarLista(mecanicos, ARCHIVO_MECANICOS);
        exito &= SerializacionUtil.guardarLista(solicitudes, ARCHIVO_SOLICITUDES);
        exito &= SerializacionUtil.guardarLista(estados, ARCHIVO_ESTADOS);
        return exito;
    }

    /**
     * Guarda solo los clientes
     * 
     * @return true si se guardó correctamente
     */
    public boolean guardarClientes() {
        return SerializacionUtil.guardarLista(clientes, ARCHIVO_CLIENTES);
    }

    /**
     * Guarda solo los servicios
     * 
     * @return true si se guardó correctamente
     */
    public boolean guardarServicios() {
        return SerializacionUtil.guardarLista(servicios, ARCHIVO_SERVICIOS);
    }

    /**
     * Guarda solo los mecánicos
     * 
     * @return true si se guardó correctamente
     */
    public boolean guardarMecanicos() {
        return SerializacionUtil.guardarLista(mecanicos, ARCHIVO_MECANICOS);
    }

    /**
     * Guarda solo las solicitudes
     * 
     * @return true si se guardó correctamente
     */
    public boolean guardarSolicitudes() {
        return SerializacionUtil.guardarLista(solicitudes, ARCHIVO_SOLICITUDES);
    }

    /**
     * Guarda solo los estados
     * 
     * @return true si se guardó correctamente
     */
    public boolean guardarEstados() {
        return SerializacionUtil.guardarLista(estados, ARCHIVO_ESTADOS);
    }

    public void limpiarDatos() {
        clientes.clear();
        servicios.clear();
        mecanicos.clear();
        solicitudes.clear();
        estados.clear();
        guardarTodosDatos();
    }

    public void importarDatos(ArrayList<Cliente> nuevosClientes,
                              ArrayList<Servicio> nuevosServicios,
                              ArrayList<Mecanico> nuevosMecanicos,
                              ArrayList<Solicitud> nuevasSolicitudes,
                              ArrayList<Estado> nuevosEstados) {
        if (nuevosClientes != null) {
            clientes.clear();
            clientes.addAll(nuevosClientes);
        }
        if (nuevosServicios != null) {
            servicios.clear();
            servicios.addAll(nuevosServicios);
        }
        if (nuevosMecanicos != null) {
            mecanicos.clear();
            mecanicos.addAll(nuevosMecanicos);
        }
        if (nuevasSolicitudes != null) {
            solicitudes.clear();
            solicitudes.addAll(nuevasSolicitudes);
        }
        if (nuevosEstados != null) {
            estados.clear();
            estados.addAll(nuevosEstados);
        }
        guardarTodosDatos();
    }

    // ==================== MÉTODOS AUXILIARES ====================

    /**
     * Busca un cliente por su ID
     * 
     * @param id ID del cliente
     * @return Cliente encontrado o null
     */
    public Cliente buscarClientePorId(String id) {
        for (Cliente c : clientes) {
            if (c.getId().equals(id)) {
                return c;
            }
        }
        return null;
    }

    /**
     * Busca un servicio por su ID
     * 
     * @param id ID del servicio
     * @return Servicio encontrado o null
     */
    public Servicio buscarServicioPorId(String id) {
        for (Servicio s : servicios) {
            if (s.getId().equals(id)) {
                return s;
            }
        }
        return null;
    }

    /**
     * Busca un mecánico por su ID
     * 
     * @param id ID del mecánico
     * @return Mecánico encontrado o null
     */
    public Mecanico buscarMecanicoPorId(String id) {
        for (Mecanico m : mecanicos) {
            if (m.getId().equals(id)) {
                return m;
            }
        }
        return null;
    }

    /**
     * Busca un estado por su ID
     * 
     * @param id ID del estado
     * @return Estado encontrado o null
     */
    public Estado buscarEstadoPorId(String id) {
        for (Estado e : estados) {
            if (e.getId().equals(id)) {
                return e;
            }
        }
        return null;
    }

    /**
     * Genera un ID consecutivo para una nueva solicitud
     * 
     * @return ID en formato "000000001", "000000002", etc.
     */
    public String generarIdSolicitud() {
        int maxId = 0;
        for (Solicitud s : solicitudes) {
            try {
                int id = Integer.parseInt(s.getId());
                if (id > maxId) {
                    maxId = id;
                }
            } catch (NumberFormatException e) {
                // Ignorar IDs no numéricos
            }
        }
        return String.format("%09d", maxId + 1);
    }
}