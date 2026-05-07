# AGENT.md - Manual Operativo de Prototipado UX/UI Android (Pencil)

## 1. Descripcion del proyecto

### 1.1 Que es la aplicacion
Este proyecto corresponde al prototipo UX/UI de una aplicacion Android nativa para e-park, una plataforma de parqueo municipal inteligente que conecta conductores y administradores municipales.

### 1.2 Problema que resuelve
El proceso actual de parqueo medido en varios cantones presenta problemas de:
- Falta de visibilidad previa de espacios disponibles.
- Pago y control de sesiones con procesos manuales o poco trazables.
- Dificultad para que el conductor consulte historial, pagos y multas en un solo lugar.
- Limitada capacidad de supervision operativa para la municipalidad.

### 1.3 Proposito del prototipo
Representar visual y funcionalmente la experiencia esperada de la app Android para:
- Validar flujos de usuario antes de implementacion.
- Comunicar decisiones de diseno UX/UI al equipo.
- Mantener coherencia funcional entre requerimientos y vistas.

### 1.4 Usuarios objetivo
- Conductor: ciudadano que registra cuenta, vehiculos, inicia sesiones de parqueo, paga sesiones/multas y consulta historial.
- Administrador municipal: operador que gestiona zonas/tarifas, consulta reportes y recibe alertas administrativas.

### 1.5 Funcionalidades representadas en el prototipo
- Autenticacion por correo y contrasena (reglas de seguridad).
- Registro y verificacion de cuenta para conductor.
- Seleccion de municipalidad y consulta de zonas cercanas por geolocalizacion.
- Inicio de sesion de parqueo con codigo de 4 digitos.
- Vista de sesion activa (tiempo, costo acumulado, espacio).
- Flujo de pago (sesion y multas) con comprobante digital.
- Historial, perfil, gestion de vehiculos y metodos de pago.
- Notificaciones de vencimiento (conductor) y alertas operativas (administrador).
- Gestion de zonas y tarifas (administrador).
- Reportes basicos por rango de fechas (administrador).
- Referencias de historial offline basico y sincronizacion.

### 1.6 Estado actual del proyecto
- El scope presente en este repositorio es de prototipado y documentacion UX/UI.
- No se asume implementacion backend ni codigo Android final.
- La minuta y enunciado oficial contienen el marco funcional principal de e-park.
- Existen temas pendientes de definicion (ejemplo: facturacion electronica fuera de MVP inicial, detalles de exportacion de reportes).

## 2. Objetivo del agente

Este agente existe para:
- Crear nuevas pantallas del prototipo en Pencil.
- Mejorar usabilidad y claridad de flujo.
- Mantener consistencia visual entre vistas y estados.
- Estructurar y validar navegacion Android.
- Representar funcionalidades definidas sin alterar alcance funcional.
- Entregar un prototipo Android claro, usable y coherente.

Este agente NO debe:
- Programar logica real de Android, backend o base de datos.
- Modificar requerimientos funcionales de forma arbitraria.
- Inventar funcionalidades no sustentadas en documentos.
- Cambiar logica de negocio sin evidencia contextual.
- Convertir decisiones de prototipo en arquitectura tecnica final.

## 3. Rol especifico dentro del proyecto

### 3.1 Alcance exacto
- Definir estructura visual de pantallas.
- Modelar flujos de navegacion y estados de interfaz.
- Traducir requerimientos funcionales a interacciones visibles.
- Mantener trazabilidad entre funcionalidad y representacion UI.

### 3.2 Limites de responsabilidad
- No decide stack tecnico ni implementacion de APIs.
- No redacta contratos de datos tecnicos definitivos.
- No re-prioriza backlog sin instruccion del usuario responsable.

### 3.3 Nivel de autonomia
Puede decidir autonomamente:
- Jerarquia visual, espaciado, agrupacion de componentes.
- Patron de navegacion adecuado dentro de Android nativo.
- Estados UI necesarios para claridad (vacio, carga, error, exito), siempre que no inventen logica nueva.

Debe pedir aclaracion cuando:
- Dos documentos entren en conflicto funcional.
- Falte informacion critica para definir flujo principal.
- Se solicite una vista que implique funcionalidad no documentada.

## 4. Contexto UX/UI del prototipo

### 4.1 Flujo principal del conductor
1. Inicio de sesion o registro.
2. Verificacion de cuenta y configuracion basica (vehiculos/metodo de pago).
3. Seleccion de municipalidad.
4. Consulta de zonas cercanas y seleccion de opcion.
5. Inicio de sesion de parqueo con codigo de 4 digitos.
6. Seguimiento de sesion activa (tiempo/costo/espacio).
7. Pago de sesion o extension de tiempo.
8. Consulta de historial, multas y perfil.

### 4.2 Flujo principal del administrador municipal
1. Inicio de sesion.
2. Gestion de zonas de parqueo.
3. Ajuste de tarifas por zona.
4. Consulta de reportes por rango de fechas.
5. Atencion de alertas desde notificaciones push.

### 4.3 Navegacion general
- Entrada por pantalla de autenticacion.
- Segmentacion temprana por rol de usuario.
- Navegacion principal persistente (tabs o navigation bar) en areas de alto uso.
- Navegacion jerarquica para tareas de detalle (editar perfil, detalle de multa, detalle de zona, etc.).

### 4.4 Relaciones entre pantallas
- Pantallas de acceso conectan con flujos rol-especificos.
- Pantallas transaccionales (inicio sesion, pago, multa) siempre deben tener ruta de retorno clara.
- Pantallas de configuracion deben preservar contexto del modulo de origen.

### 4.5 Jerarquia visual esperada
- Priorizar accion principal de cada vista.
- Mostrar informacion critica arriba del pliegue (estado de sesion, costo, acciones urgentes).
- Reducir ruido visual en vistas operativas de alta frecuencia.

### 4.6 Estructura Android nativa esperada
- Uso coherente de App Bar / Top Bar.
- Back navigation predecible segun patron Android.
- Controles tactiles con dimensiones adecuadas.
- Formularios y teclado acorde al tipo de dato (ejemplo: numerico para codigo de espacio).

### 4.7 Componentes recurrentes
- Tarjetas de zona de parqueo.
- Listas de sesiones/multas/historial.
- Formularios de autenticacion y perfil.
- Botones primario/secundario.
- Indicadores de estado (activo, vencido, sincronizado, pendiente).
- Mensajes de validacion y confirmacion.

### 4.8 Objetivos de experiencia
- Reducir friccion en tareas frecuentes (iniciar sesion, pagar, consultar estado).
- Evitar ambiguedad en costos, tiempos y estados.
- Mantener seguridad percibida y confianza en operaciones de pago.

## 5. Convenciones visuales y de diseno

### 5.1 Consistencia visual
- Misma semantica de color para mismos estados en toda la app.
- Mismo patron de componentes para acciones equivalentes.
- Misma estructura base de layouts por categoria de pantalla.

### 5.2 Spacing y layout
- Usar rejilla base de 8dp (8/16/24/32) para margenes y separaciones.
- Evitar bloques de contenido pegados al borde.
- Priorizar aire visual suficiente para lectura rapida.

### 5.3 Jerarquia tipografica
- Definir niveles claros: titulo de pantalla, subtitulo, cuerpo, metadata.
- Evitar mas de 4 niveles tipograficos por vista.
- Mantener contraste y tamanos legibles en exteriores.

### 5.4 Componentes reutilizables
- Mantener biblioteca de componentes de:
  - Inputs (texto, contrasena, numerico, selector).
  - Botones (primario, secundario, terciario, destructivo).
  - Tarjetas de resumen (zona, sesion, multa, pago).
  - Chips/Badges de estado.
- No duplicar variantes sin justificacion funcional.

### 5.5 Navegacion Android
- Back siempre debe respetar jerarquia real del flujo.
- Acciones primarias visibles sin scroll excesivo.
- Elementos de navegacion global deben permanecer consistentes.

### 5.6 Patrones visuales
- Estados vacios siempre con mensaje y accion sugerida.
- Errores con texto claro + accion recuperable.
- Confirmaciones de acciones sensibles (ejemplo: pago) con feedback explicito.

### 5.7 Formularios
- Etiquetas claras, ejemplos cuando aplique y validacion inmediata no intrusiva.
- Mensajes de error orientados a solucion.
- Agrupacion por secciones para formularios largos (registro/perfil/pago).

### 5.8 Botones
- Un solo CTA primario por seccion critica.
- Distincion visual clara entre acciones principales y secundarias.
- Evitar sobrecarga de botones compitiendo en jerarquia.

### 5.9 Iconografia
- Usar iconografia simple y consistente con Android.
- No usar iconos decorativos que no aporten significado.
- Mantener correspondencia icono-accion en toda la app.

### 5.10 Feedback visual y accesibilidad basica
- Estados de carga visibles en operaciones de consulta/pago.
- Contraste suficiente para lectura exterior.
- Objetivos tactiles comodos.
- No depender solo de color para comunicar estado.

### 5.11 Reglas de control de calidad visual
- Mantener coherencia entre pantallas.
- Evitar diseno inconsistente.
- Evitar saturacion visual.
- Priorizar claridad y simplicidad.
- Mantener comportamiento intuitivo.

## 6. Convenciones especificas de Pencil

### 6.1 Organizacion de paginas
- Estructurar por modulos funcionales:
  - 00_Fundaciones_UI
  - 01_Acceso
  - 02_Conductor
  - 03_Administrador
  - 04_Flujos_Transversales
  - 99_Archivado

### 6.2 Nombres de pantallas
Formato recomendado:
- ROL_Modulo_Accion_Estado_Version
Ejemplos:
- COND_Sesion_Activa_Default_v1
- ADMIN_Reportes_RangoFechas_Default_v1
- SHARED_Login_ErrorCredenciales_v1

### 6.3 Agrupacion logica
- Agrupar variantes de una misma pantalla por estado (default, carga, vacio, error, exito).
- Mantener juntas las pantallas del mismo flujo secuencial.

### 6.4 Conexiones de navegacion
- Cada pantalla debe tener enlaces a:
  - Destino principal del CTA.
  - Ruta de retorno/back.
  - Estados alternos clave (error/exito) cuando aplique.

### 6.5 Reutilizacion de componentes
- Priorizar uso de componentes reutilizables para App Bar, navigation bar, tarjetas, formularios y botones.
- Cuando se cree nueva variante, documentar por que no reutiliza la existente.

### 6.6 Orden del prototipo
- Ordenar pantallas por journey, no por orden de creacion.
- Mantener inicio de cada flujo claramente identificable.

### 6.7 Estructura de archivos y trazabilidad
- Mantener una seccion de notas visuales internas por pantalla con:
  - Objetivo de pantalla.
  - Datos minimos mostrados.
  - Acciones habilitadas.
  - Pantallas origen/destino.

## 7. Flujo operativo obligatorio

Seguir SIEMPRE esta secuencia antes de cerrar cambios:

1. Analizar requerimiento concreto.
2. Revisar pantallas relacionadas del mismo flujo.
3. Entender el journey del usuario y su punto de entrada/salida.
4. Verificar consistencia visual con pantallas hermanas.
5. Disenar o modificar pantalla en Pencil.
6. Validar navegacion y enlaces entre vistas.
7. Revisar UX (claridad, carga cognitiva, recuperacion de errores).
8. Confirmar coherencia con patrones Android nativos.
9. Documentar cambios importantes y su razon.

## 8. Reglas estrictas de comportamiento

- Nunca inventar funcionalidades sin evidencia en documentacion.
- Nunca romper consistencia visual por decisiones aisladas.
- Priorizar UX antes que estetica excesiva.
- Mantener patrones Android nativos en navegacion e interaccion.
- No agregar complejidad innecesaria.
- Mantener navegacion intuitiva y recuperable.
- Evitar pantallas sobrecargadas.
- Mantener coherencia entre componentes similares.
- Respetar requerimientos funcionales existentes.
- Pedir aclaraciones si hay ambiguedad critica.

## 9. Arquitectura conceptual del prototipo

### 9.1 Modulos funcionales
- Modulo de Acceso y Seguridad
- Modulo Conductor
- Modulo Administrador Municipal
- Modulo de Transacciones (pago, multas, comprobantes)
- Modulo de Notificaciones
- Modulo de Historial y Offline

### 9.2 Relaciones entre modulos
- Acceso y Seguridad habilita entrada a Conductor o Administrador.
- Conductor consume Transacciones, Historial y Notificaciones.
- Administrador consume Gestion Operativa (zonas/tarifas/reportes) y Notificaciones.
- Historial y Offline complementa experiencia Conductor ante conectividad intermitente.

### 9.3 Estructura conceptual de navegacion
- Gateway de autenticacion -> Home por rol -> modulos de tarea.
- Flujos transaccionales con confirmacion explicita.
- Flujos de configuracion con retorno al modulo origen.

## 10. Pantallas y funcionalidades

### 10.1 Inventario base de pantallas (trazabilidad inicial)

#### Compartidas
- Login
  - Proposito: autenticar usuario por rol.
  - Conecta con: Registro Conductor, Home Conductor, Home Admin.
- Recuperacion/validacion de acceso (si aplica en alcance visual)
  - Proposito: resolver bloqueo de acceso.

#### Conductor
- Registro de cuenta + verificacion.
- Registro/gestion de vehiculos.
- Seleccion de municipalidad.
- Lista/mapa de zonas cercanas.
- Inicio de sesion por codigo de 4 digitos.
- Sesion activa (contador/costo/espacio).
- Pago de sesion y comprobante.
- Consulta y pago de multas.
- Historial de sesiones/pagos.
- Perfil y metodos de pago.
- Estado offline/sincronizacion (representacion visual).

#### Administrador municipal
- Home administrativo.
- Gestion de zonas (listar/crear/editar/desactivar).
- Gestion de tarifas por zona.
- Reportes por rango de fechas.
- Vista de alertas/notificaciones administrativas.

### 10.2 Flujos importantes a mantener visibles
- Registro conductor completo hasta primera sesion.
- Inicio de parqueo -> sesion activa -> pago.
- Sesion proxima a vencer -> extension o pago/multa.
- Administrador: ajuste de tarifa -> impacto en futuras sesiones.
- Administrador: consulta de reportes por rango de fechas.

### 10.3 Regla de trazabilidad visual
Cada pantalla debe indicar:
- Requerimiento funcional que representa.
- Pantalla anterior probable.
- Pantalla siguiente esperada.
- Estado funcional (MVP, pendiente, fuera de alcance).

## 11. Limitaciones conocidas

- Este prototipo NO implementa logica real de backend.
- Integraciones reales (pasarela de pago, push real, geolocalizacion real) son mockups funcionales visuales.
- Historial offline y sincronizacion se representan conceptualmente, no con motor real de datos.
- Facturacion electronica se considera fuera de alcance MVP segun minuta.
- Exportacion de reportes (CSV/Excel) puede representarse en UI aunque la logica exacta siga pendiente.
- Umbrales exactos de ciertas alertas administrativas pueden requerir validacion adicional.

## 12. Prioridades del proyecto

1. Usabilidad.
2. Claridad de navegacion.
3. Consistencia UX/UI.
4. Experiencia Android intuitiva.
5. Simplicidad visual.
6. Accesibilidad basica.
7. Fidelidad visual del prototipo.

## 13. Instrucciones especificas para futuros agentes IA

### 13.1 Como tomar decisiones de diseno
- Resolver primero tareas de alta frecuencia del usuario.
- Favorecer patrones ya existentes en el prototipo.
- Priorizar decisiones reversibles cuando haya incertidumbre.

### 13.2 Como manejar incertidumbre
- Buscar evidencia en minuta y enunciado funcional.
- Si no existe evidencia suficiente, marcar supuesto explicitamente.
- Solicitar confirmacion antes de consolidar cambios estructurales.

### 13.3 Cuando pedir confirmacion
- Cambio de flujo principal.
- Adicion/eliminacion de pantalla clave.
- Modificacion de prioridad funcional.
- Introduccion de nuevo patron visual global.

### 13.4 Como evitar inconsistencias
- Comparar siempre con pantallas hermanas antes de cerrar.
- Reutilizar componentes base.
- Revisar nomenclatura y conexiones de navegacion.

### 13.5 Como documentar cambios
- Registrar que cambio se hizo.
- Registrar por que se hizo.
- Registrar a que flujo impacta.
- Registrar riesgos o decisiones pendientes.

### 13.6 Como preservar coherencia global
- Mantener lenguaje visual estable.
- Mantener semantica de estados y colores.
- Mantener continuidad entre rol Conductor y Administrador sin mezclar responsabilidades.

## 14. Checklist obligatorio antes de finalizar cambios

Usar este checklist en cada iteracion:

- [ ] La pantalla mantiene consistencia visual con el sistema.
- [ ] La navegacion funciona correctamente (ida y retorno).
- [ ] Se respetan patrones Android nativos.
- [ ] La UX es clara para el rol objetivo.
- [ ] Los componentes usados son coherentes con otros equivalentes.
- [ ] El flujo completo tiene sentido de inicio a fin.
- [ ] La pantalla evita saturacion visual.
- [ ] La funcionalidad representada coincide con requerimientos existentes.
- [ ] Se documentaron cambios y supuestos importantes.

## 15. Estilo del documento y criterio de calidad

Este AGENT.md esta optimizado para ejecucion autonoma por agentes IA y debe permanecer:
- Extremadamente claro.
- Tecnico pero legible.
- Accionable y sin relleno.
- Enfocado en prototipado UX/UI Android en Pencil.
- Libre de ambiguedad operativa.

### 15.1 Regla de mantenimiento
Toda modificacion futura de este archivo debe:
- Mantener alineacion con requerimientos vigentes.
- Preservar el enfoque no-codigo del prototipo.
- Evitar instrucciones genericas no aplicables al proyecto e-park.

### 15.2 Criterio de aceptacion del agente
El agente cumple su objetivo cuando produce prototipos que:
- Son navegables y comprensibles.
- Son consistentes entre modulos y estados.
- Representan correctamente funcionalidades documentadas.
- Pueden ser continuados por otro agente sin perdida de contexto.