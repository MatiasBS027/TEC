# Escuela Ingeniería en Computación

Curso IC-5821 Requerimientos de Software

## Prof. Dr. Jaime Solano Soto

## Periodo I Semestre, 2026

## Tarea 4

Tarea 4: Modelado de Objetos
Objetivo:  Las personas estudiantes deben dejar de pensar en "pasos de un
algoritmo" y empezar a pensar en "responsabilidades y mensajes.  Modelar no es
dibujar cajitas; es gestionar la complejidad.  Un mal modelo de objetos al inicio
garantiza un sistema imposible de mantener en el futuro.
Realizar:  Programación en java de las HU del punto 7
Actividad: "El Ecosistema de Servicios Urbanos"️

- El Escenario (Diseño de Abstracción)

La Municipalidad de Cartago desea digitalizar la gestión de servicios.  No es solo
una base de datos; es un sistema donde interactúan Parquímetros Inteligentes,
Camiones de Basura con GPS y Cámaras de Tráfico.
El Reto:  Modelar los objetos de este ecosistema,  con la restricción de que no
pueden escribir ni una sola línea de código funcional.  Solo pueden definir la
"interfaz" de sus objetos.

- Fase 1: Identificación de Abstracciones

Cada grupo debe identificar los Objetos Candidatos basándose en tres criterios de
modelación:
1.Estado (Atributos): ¿Qué sabe el objeto de sí mismo?
2.Comportamiento (Métodos): ¿Qué sabe hacer el objeto?
3.Identidad: ¿Cómo se distingue un parquímetro de otro si ambos están en la
misma calle?
Tip de Modelación: Si un objeto se llama ManejadorDeTodo, está mal
modelado.  Debe haber Cohesión (un objeto, una responsabilidad).
IC5821 – Reqs – TC09 – Modelado Objetos 15/04/26

- Fase 2: El Juego de Roles de Mensajería
En lugar de dibujar, los estudiantes actúan como los objetos.
•Estudiante A: Es un SensorDeParqueo.
•Estudiante B: Es el GestorDeCobro.
•Estudiante C: Es la AppDelUsuario.
Dinámica: El profesor lanza un evento: "Un vehículo se estaciona en la Zona 4".
Los estudiantes deben pasarse "papelitos" (mensajes) que representen las
llamadas a métodos:
•Sensor envía mensaje a Gestor: notificarOcupación(idZona, horaInicio).
•Gestor envía mensaje a App: solicitarPago(idUsuario, tarifaActual).
- Fase 3: Ficha de CRC (Clase-Responsabilidad-

## Colaborador)

Llenar la siguiente ficha para cada objeto clave:
Clase: VehículoEmergencia
ResponsabilidadesColaboradores

- Notificar ubicación actual.

ServicioEmergencias911

- Solicitar prioridad en semáforos.

ControladorSemáforos

- Registrar consumo de combustible.

GestorFlota

- Fase 4: Diagrama de Clases y Relaciones

La interacción entre ellos se debe formalizar en un Diagrama de Clases UML.
Aquí se evalúan los conceptos técnicos de modelación:
•Herencia vs. Composición: ¿Un CamionDeBasura es un Vehiculo
(Herencia) o tiene un Motor (Composición)?
IC5821 – Reqs – TC09 – Modelado Objetos 15/04/26

•Encapsulamiento: ¿Los atributos son privados? ¿Existen métodos
públicos (getters/setters) para acceder a la información de forma segura?
•Polimorfismo: Si el GestorDeCobro envía el mensaje aplicarTarifa(), ¿el
sistema sabe distinguir si es la tarifa de un carro o de una motocicleta sin
usar un “if” gigante?

- Fase 5: Inclusión de nuevo objeto

La Municipalidad decide incluir Scooters Eléctricos, ¿Cómo lo manejará su
modelo?  ¿Tiene que reprogramar todo el sistema o su modelo de objetos es lo
suficientemente flexible para 'enchufar' una nueva clase?

- Dibujar los objetos específicos de ePark

En UML dibujar el diagrama de clases de los objetos contenidos en ePark.
Además dibujar los diagramas de secuencia de las siguientes HU Historias de

## Usuario

7.1-Estacionar un vehículo en la calle
7.2-Enviar mensaje al usuario de que su parquímetro está próximo a vencer, le
faltan 5 min.
7.3-Visualizar todos los pagos realizados por tarjeta de crédito, en un día, para un
cliente específico , debido a estacionamiento en parquímetros

IC5821 – Reqs – TC09 – Modelado Objetos 15/04/26
