# Guía de Trabajo para el Proyecto "Taller Mecánico"

## 1. Contexto y entregables
- **Objetivo general:** modelar la información del ambiente de un taller de mecánica automotriz mediante clases Java, un diagrama de clases en Drawio y archivos XML de ejemplo.
- **Entregables clave:**
  1. Diagrama de clases (`.drawio`) que describa Clientes, Servicios y Mecánicos, junto con sus relaciones.
  2. Código fuente Java que replique la estructura del diagrama y respete la especificación XML provista.
  3. Archivos XML de ejemplo (uno por concepto) para validar la estructura.
  4. Documentación técnica y funcional breve para cada componente.

## 2. División sugerida del trabajo
| Tarea | Responsable (ejemplo) | Descripción | Dependencias |
| --- | --- | --- | --- |
| Investigación y levantamiento de requisitos | Persona A | Profundizar en la estructura solicitada, validar atributos y relaciones. | Ninguna |
| Diseño del diagrama en Drawio | Persona A (principal) + Persona B (revisión) | Elaborar el diagrama de clases con relaciones, multiplicidades y tipos de datos. | Requisitos definidos |
| Implementación de clases Java | Persona B (principal) + Persona A (revisión) | Crear las clases `Cliente`, `Servicio`, `Mecanico` y las asociaciones necesarias. | Diagrama validado |
| Generación de XML de ejemplo | Persona A (principal) + Persona B (revisión) | Crear los archivos XML siguiendo la estructura de la especificación. | Clases Java definidas |
| Documentación (manual de uso y técnica) | Persona B (principal) + Persona A (revisión) | Redactar README del proyecto, explicar cómo ejecutar/validar. | Todo lo anterior |
| Integración y pruebas | Ambos | Revisar consistencia entre diagrama, código y XML. | Todo lo anterior |

> **Nota:** Ajusten los responsables según la disponibilidad real del equipo. La clave es mantener siempre una persona principal y otra revisora para cada tarea.

## 3. Documentación esperada por componente
### 3.1 Diagrama de clases (Drawio)
- Ubicar el archivo en `docs/diagramas/` (crear carpeta si es necesario).
- Incluir una captura exportada en PNG o PDF para consulta rápida.
- Documentar en un breve apartado del README:
  - Herramienta utilizada (Draw.io / diagrams.net).
  - Descripción de cada relación (ej. "Un mecánico puede validar múltiples servicios").
  - Supuestos tomados (por ejemplo, si las placas son únicas, si el precio está en moneda local, etc.).

### 3.2 Clases Java
- Crear un paquete dedicado, por ejemplo `com.taller.modelo`.
- Estructurar las clases con atributos privados, constructores, getters/setters y métodos auxiliares necesarios.
- Documentar cada clase con comentarios JavaDoc breves: propósito, atributos y relaciones.
- Mantener coherencia con el diagrama Drawio (nombres, tipos y asociaciones).
- Si se agregan listas (ej. servicios validados por un mecánico), indicar el tipo (`List<Servicio>`).

### 3.3 Archivos XML
- Crear una carpeta `data/xml/` para almacenar los archivos `clientes.xml`, `servicios.xml` y `mecanicos.xml`.
- Seguir la estructura proporcionada en la imagen:
  - Clientes: `<cliente id="...">` con sub-etiquetas `<nombre>`, `<placa>`, `<telefono>`, `<email>`.
  - Servicios: `<servicio id="...">` con `<nombre>` y `<precio>`.
  - Mecánicos: `<mecanico id="...">`, `<nombre>`, `<puesto>`, y lista de `<servicios>` con `<id>` que referencien a los servicios existentes.
- Documentar en el README cómo se relacionan los IDs entre los XML (ej. el `<id>` del servicio en el XML de mecánicos debe existir en `servicios.xml`).

### 3.4 Pruebas y validación
- Definir un checklist simple para validar:
  - Atributos obligatorios presentes.
  - Coherencia entre el diagrama y el código.
  - Coherencia entre el XML y las clases (nombres de campos).
  - Opcional: crear una clase `Main` o pruebas unitarias simples que carguen datos de ejemplo.

## 4. Flujo de trabajo con Git
### 4.1 Estructura de ramas sugerida
- `main`: rama estable con entregables revisados.
- `docs/*`: ramas para cambios de documentación (ej. `docs/readme`, `docs/diagramas`).
- `feature/*`: ramas para nuevas funcionalidades o componentes (ej. `feature/modelo-clases`, `feature/xml-data`).
- `hotfix/*`: usar solo si se requiere corregir algo urgente en `main`.

### 4.2 Proceso recomendado
1. **Crear una rama por tarea** desde `main`: `git checkout -b feature/modelo-clases`.
2. **Realizar los cambios** locales correspondientes.
3. **Agregar y commitear** cambios con mensajes claros: `git commit -m "Implementa clases modelo"`.
4. **Sincronizar con remoto** si hay más personas:
   - `git fetch origin`
   - `git merge origin/main` (o `git rebase origin/main`) para mantener la rama actualizada.
5. **Subir la rama**: `git push origin feature/modelo-clases`.
6. **Crear Pull Request (PR)** en GitHub/Bitbucket:
   - Resumen de cambios.
   - Evidencia de pruebas (capturas, comandos ejecutados).
   - Solicitar revisión al compañero.
7. **Revisar comentarios** y aplicar correcciones en la misma rama.
8. **Aprobar y fusionar** (merge) a `main` solo cuando ambos estén conformes.

### 4.3 Reglas de colaboración
- Nunca commitear directamente en `main`.
- Siempre realizar **code review** cruzado antes de fusionar.
- Mantener el repositorio limpio: una vez mergeado, borrar la rama remota con `git push origin --delete <rama>` y localmente `git branch -d <rama>`.
- Documentar cambios relevantes en el README u otros archivos de documentación.
- Usar issues o tarjetas de seguimiento para cada tarea para mantener visibilidad.

### 4.4 Buenas prácticas adicionales
- Configurar `.gitignore` para excluir archivos temporales (IDE, build, etc.).
- Hacer commits pequeños y frecuentes.
- Describir claramente en los mensajes de commit qué se hizo y por qué.
- Antes de mergear, asegurarse de que el proyecto compile y las estructuras XML sean válidas.

## 5. Siguientes pasos sugeridos
1. Crear la carpeta `docs/diagramas/` y `data/xml/` (cuando corresponda).
2. Definir en un documento compartido (Google Docs, Notion, etc.) el detalle de cada atributo y restricciones.
3. Establecer un calendario de trabajo con fechas límite por entregable.
4. Configurar un canal de comunicación (Slack, WhatsApp) para sincronizar avances y dudas.
5. Revisar al menos una vez por semana el estado general del proyecto y ajustar prioridades.

---
**¡Éxitos en el proyecto!** Recuerden mantener la comunicación clara y los entregables bien versionados para evitar contratiempos.
