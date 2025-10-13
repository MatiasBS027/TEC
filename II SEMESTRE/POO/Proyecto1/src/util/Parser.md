Sistema de Gestión de Taller Mecánico

¿Por qué usamos SAX y DOM?

SAX (Simple API for XML) - Para Lectura

¿Por qué lo usamos?
- Consume poca memoria al leer los XML
- Es rápido para cargar los datos al iniciar
- Ya teníamos los handlers implementados

Ventajas:
- Eficiente en memoria
- Lectura rápida
Desventajas:
- Solo sirve para leer, no para escribir
- Código más complejo

-----------------------

DOM (Document Object Model) - Para Escritura

¿Por qué lo usamos?
- Permite modificar el XML fácilmente (agregar, editar, eliminar)
- Código simple e intuitivo para guardar

Ventajas:
- Fácil de usar para escribir y modificar
- Control total del formato del XML
Desventajas:
- Consume más memoria
- Más lento con archivos grandes

---
Conclusión:
Usamos SAX para leer (rápido y eficiente) y DOM para escribir (fácil y práctico). Así aprovechamos lo mejor de ambos.