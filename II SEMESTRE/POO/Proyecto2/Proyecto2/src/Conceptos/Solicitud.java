/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Conceptos;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * Representa una solicitud de servicio 
 * Contiene información del cliente, servicio principal, mecánico asignado,
 * estado actual y servicios adicionales
 * @author Matias 
 * 
 */
public class Solicitud implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private String id;              // Consecutivo autogenerado
    private String placa;           // Placa del vehículo
    private String idServicio;      // ID del servicio principal
    private String idCliente;       // ID del cliente
    private String idMecanico;      // ID del mecánico (puede ser null al inicio)
    private String idEstado;        // ID del estado (inicia en "000")
    private String observaciones;   // Observaciones del servicio
    private ArrayList<String> otrosServicios; // Lista de IDs de servicios adicionales

    public Solicitud() {
        this.otrosServicios = new ArrayList<>();
        this.idEstado = "000"; // Estado inicial: Nuevo
    }

    // Constructor con parámetros básicos
    public Solicitud(String id, String placa, String idServicio, String idCliente) {
        this();
        this.id = id;
        this.placa = placa;
        this.idServicio = idServicio;
        this.idCliente = idCliente;
    }

    // Getters y Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public String getIdServicio() {
        return idServicio;
    }

    public void setIdServicio(String idServicio) {
        this.idServicio = idServicio;
    }

    public String getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(String idCliente) {
        this.idCliente = idCliente;
    }

    public String getIdMecanico() {
        return idMecanico;
    }

    public void setIdMecanico(String idMecanico) {
        this.idMecanico = idMecanico;
    }

    public String getIdEstado() {
        return idEstado;
    }

    public void setIdEstado(String idEstado) {
        this.idEstado = idEstado;
    }

    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }

    public ArrayList<String> getOtrosServicios() {
        return otrosServicios;
    }

    public void setOtrosServicios(ArrayList<String> otrosServicios) {
        this.otrosServicios = otrosServicios;
    }

    // Método auxiliar para agregar un servicio adicional
    public void addOtroServicio(String idServicio) {
        if (this.otrosServicios == null) {
            this.otrosServicios = new ArrayList<>();
        }
        if (!this.otrosServicios.contains(idServicio)) {
            this.otrosServicios.add(idServicio);
        }
    }

    // Método auxiliar para remover un servicio adicional
    public void removeOtroServicio(String idServicio) {
        if (this.otrosServicios != null) {
            this.otrosServicios.remove(idServicio);
        }
    }

    @Override
    public String toString() {
        return "Solicitud{" +
                "id='" + id + '\'' +
                ", placa='" + placa + '\'' +
                ", idCliente='" + idCliente + '\'' +
                ", idEstado='" + idEstado + '\'' +
                '}';
    }
}