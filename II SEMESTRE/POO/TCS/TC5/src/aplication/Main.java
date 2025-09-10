/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aplication;

import conceptos.*;

import java.util.Date;
/**
 *
 * @author Matias
 * carnee: 2025102376
 *
 */
public class Main {
    public static void main(String[] args) {
        // PersonaFisica
        PersonaFisica personaFisica = new PersonaFisica("correo@ejemplo.com", "Calle 123", "1234-6789", "12345678A");
        personaFisica.setDireccion("Cartago");
        System.out.println("Persona Fisica \nDirección: " + personaFisica.getDireccion());
        System.out.println("Email: " + personaFisica.getEmail());
        System.out.println("Teléfono: " + personaFisica.getTelefono());
        System.out.println("Cédula: " + personaFisica.getCedula());

        // PersonaJuridica
        PersonaJuridica personaJuridica = new PersonaJuridica("empresa@ejemplo.com", "Avenida 456", "2222-3333", "CIF123");
        personaJuridica.setCedulaJuridica("CIF999");
        System.out.println("\nPersona Juridica \nCIF: " + personaJuridica.getCedulaJuridica());
        System.out.println("Email: " + personaJuridica.getEmail());
        System.out.println("Teléfono: " + personaJuridica.getTelefono());
        System.out.println("Dirección: " + personaJuridica.getDireccion());

        // Animal
        Animal animal = new Animal("Perro", "Oreo", 5);
        animal.setEdad(6);
        System.out.println("Animal: " + animal.getNombre());
        System.out.println("Edad: " + animal.getEdad());

        // Antecedente
        Antecedente antecedente = new Antecedente(1, "Vacunación completa");
        antecedente.setDescripcion("Vacunación y desparasitación");
        System.out.println("\nID Antecedente: " + antecedente.getIdentificador());
        System.out.println("Antecedente: " + antecedente.getDescripcion());

        // Expediente
        Expediente expediente = new Expediente("EXP001", animal);
        expediente.agregarAntecedente(antecedente);
        System.out.println("\nExpediente creado para el animal: " + expediente.getMascota().getNombre());
        System.out.println("Expediente referencia: " + expediente.getReferencia());

        // Personal
        Personal personal = new Personal("Juan", "Pérez Sanchez", new Date());
        personal.setApellidos("Gómez");
        System.out.println("\nPersonal \nNombre: " + personal.getNombre());
        System.out.println("Apellidos: " + personal.getApellidos());
        System.out.println("Fecha de contratación: " + personal.getFechaContratacion());

        // Veterinario
        Veterinario veterinario = new Veterinario("Ana", "López", new Date());
        veterinario.setCodigo("VET123");
        System.out.println("\nVeterinario \nCódigo: " + veterinario.getCodigo());
        System.out.println("Nombre: " + veterinario.getNombre());
        System.out.println("Apellidos: " + veterinario.getApellidos());
        System.out.println("Fecha de contratación: " + veterinario.getFechaContratacion());

        // Auxiliar
        Auxiliar auxiliar = new Auxiliar("Luis", "Martínez", new Date());
        auxiliar.setFuncion("Asistente de consulta");
        System.out.println("\nAuxiliar \nFunción: " + auxiliar.getFuncion());
        System.out.println("Nombre: " + auxiliar.getNombre());
        System.out.println("Apellidos: " + auxiliar.getApellidos());
        System.out.println("Fecha de contratación: " + auxiliar.getFechaContratacion());

        //Diagnostico
        Diagnostico diagnostico = new Diagnostico(new Date(), "Tratamiento con antibióticos", new Animal("Gato", "Manchas", 3), new Personal("Jose", "Murillo Torres", new Date()));
        diagnostico.setDescripcion("Reposo y medicación");
        System.out.println("\nDiagnóstico tratamiento: " + diagnostico.getDescripcion());
        System.out.println("Fecha del diagnóstico: " + diagnostico.getFecha());
        System.out.println("Mascota: " + diagnostico.getMascota().getNombre());
        System.out.println("Realizado por: " + diagnostico.getPersonal().getNombre());

        //factura
        Factura factura = new Factura("FAC001", diagnostico);
        factura.agregarItem(new ElementoFactura(1, 100.0f, 1.0f));
        System.out.println("\nFactura \nTotal: " + factura.totalizar());
        System.out.println("Referencia: " + factura.referencia);

        //ElementoFactura
        ElementoFactura elementoFactura = new ElementoFactura(1, 50.0f, 2.0f);
        elementoFactura.setCantidad(2.0f);
        System.out.println("\nElementoFactura \nCantidad: " + elementoFactura.getCantidad());
        System.out.println("Precio: " + elementoFactura.getPrecio());

    }
    
}
