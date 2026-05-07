# DESIGN.md - Ingenieria inversa UX/UI del frontend de referencia

## Alcance y criterio de analisis
- Proyecto analizado: FrontEnd-Sistema-Administrador-Eventos-TEC.
- Enfoque exclusivo: frontend visual, UX, navegacion, estructura de pantallas, componentes e interaccion.
- Exclusiones intencionales: backend, arquitectura de servicios, contratos API, persistencia y seguridad de servidor.
- Objetivo de este documento: permitir a agentes IA reproducir una experiencia visual y de uso muy similar en un prototipo Android nativo en Pencil, sin clonar literalmente el frontend web.

---

## 1) Descripcion general del frontend
### 1.1 Perfil visual y tono
- Estilo predominante: corporativo-funcional, sobrio, de alta legibilidad.
- Sensacion de uso: herramienta administrativa antes que producto aspiracional.
- Nivel visual: medio-bajo en decoracion; alto en estructura y jerarquia operativa.
- Personalidad: utilitaria, directa, orientada a tareas, con foco en control y gestion.

### 1.2 Rasgos de identidad visual
- Base cromatica fria y neutral: fondos grises claros + tarjetas blancas.
- Color de accion dominante: azul oscuro institucional.
- Color semantico fuerte para acciones criticas: rojo (eliminar/cancelar), verde (confirmar/aprobar), gris (volver/secundario).
- Uso extensivo de bordes visibles (1px-2px) para delimitar bloques.
- Radius moderado y consistente (esquinas redondeadas sin estilo pill extremo).

### 1.3 Enfoque UX
- UX centrada en productividad:
  - filtrar,
  - buscar,
  - revisar listas,
  - ejecutar acciones por item.
- Patrones repetitivos entre roles para reducir curva de aprendizaje.
- Priorizacion de densidad de informacion sobre expresividad visual.

---

## 2) Filosofia de diseno
### 2.1 Principios implicitos detectados
- Claridad por bloques: cada modulo funcional vive en una tarjeta o panel delimitado.
- Navegacion estable: header fijo conceptual + sidebar persistente en areas autenticadas.
- Repeticion consciente: mismos patrones de tabla/card/form en admin, organizer y student.
- Semantica cromatica estable:
  - Azul = accion primaria y navegacion,
  - Verde = confirmar/ver detalle positivo,
  - Rojo = riesgo/eliminar/rechazar,
  - Gris = retroceso o estado neutro.

### 2.2 Priorizaciones UX
- Primero contexto de pagina (titulo grande).
- Luego controles de filtro/busqueda.
- Luego contenido principal (cards/tabla/lista).
- Finalmente acciones secundarias (volver, eliminar, acciones de mantenimiento).

### 2.3 Gestion del espacio
- Espaciado vertical generoso entre secciones (mb-6, mb-8).
- Espaciado interno uniforme en contenedores (p-6, p-8).
- Distribucion por grillas:
  - stats: 3-4 columnas,
  - filtros: 3 columnas,
  - eventos: 3 columnas,
  - formularios: 1-2 columnas segun campo.

---

## 3) Arquitectura visual del frontend
### 3.1 Macroestructura global (zona autenticada)
- Header superior:
  - titulo plataforma,
  - acceso rapido a anuncios,
  - avatar placeholder,
  - boton salir.
- Sidebar izquierdo:
  - menu contextual por rol,
  - items con icono + etiqueta,
  - estado activo por ruta exacta.
- Main content:
  - superficie principal de trabajo con padding amplio,
  - contenido modular por pagina.

### 3.2 Jerarquia visual comun
1. Titulo de pantalla (text-2xl/text-3xl).
2. Bloque de filtros/acciones primarias.
3. Bloque de resultados (cards o tabla).
4. Acciones por fila/item.
5. Acciones de retorno/cierre.

### 3.3 Tipos de layout recurrentes
- Layout A: Dashboard con KPIs + lista breve destacada.
- Layout B: Exploracion con filtros arriba + grid de cards.
- Layout C: Gestion tabular (thead oscuro o gris + acciones por fila).
- Layout D: Formulario largo en tarjeta (crear/editar).
- Layout E: Detalle en tarjeta grande + metadata en grid 2 columnas + CTA al pie.
- Layout F: Mensajeria tipo listado de tarjetas con zona inferior de acciones.

---

## 4) Sistema de navegacion
### 4.1 Estructura de rutas por rol
- Publicas:
  - / (login)
  - /register
- Student:
  - dashboard, explore, registrations, messages, announcements, announcement/:id, event/:id, profile.
- Organizer:
  - dashboard, explore, my-events, registrations, messages, announcements, announcement/:id,
  - send-message,
  - event/:id,
  - event/:id/participants,
  - create-event,
  - edit-event/:id,
  - event/past/:id,
  - registration/past/:id,
  - profile.
- Admin:
  - dashboard, explore (aprobacion), registrations (moderacion), organizers, reports,
  - announcements, announcement/:id, create-announcement,
  - event/:id, messages, send-message, edit-event/:id,
  - catalogs, promotions.

### 4.2 Patron de control de acceso
- Guard por rol en rutas protegidas.
- Si no autenticado: redireccion a login.
- Si rol incorrecto: redireccion automatica al home del rol activo.

### 4.3 Patron de navegacion in-page
- Predominio de navegacion por boton explicito (Ver detalles, Volver, Editar, etc.).
- Uso frecuente de navegacion relativa (-1) para regreso contextual.
- Navegacion cross-modulo por IDs de entidad (event/:id, announcement/:id).

### 4.4 Traduccion a patron Android
- Recomendacion para prototipo:
  - TopAppBar fija.
  - NavigationRail en tablet y Drawer modal en movil.
  - Bottom navigation opcional solo para Student (max 4-5 destinos).
- Mantener profundidad de flujo y jerarquia rol->modulo->detalle.

---

## 5) Analisis completo de pantallas
## 5.1 Pantallas transversales
### Login
- Proposito: acceso y redireccion por rol.
- Estructura:
  - fondo gris,
  - contenedor blanco grande,
  - panel central con borde azul grueso,
  - 2 campos,
  - CTA primario + CTA secundario.
- Interaccion:
  - validacion de email institucional y password fuerte,
  - toast de exito/error,
  - redireccion diferida (~1200ms).

### Register
- Proposito: alta de usuario.
- Estructura:
  - bloque datos personales + bloque institucional,
  - campos verticales,
  - select de campus,
  - boton primario full width,
  - boton volver rojo.
- UX:
  - validaciones estrictas en cliente,
  - lenguaje directo de error.

### Profile
- Proposito: mantenimiento de cuenta y credenciales.
- Estructura:
  - tarjeta grande,
  - campos readonly y editables,
  - seccion password con confirmacion,
  - CTA actualizar,
  - CTA extra para promocion (solo student).
- Patron:
  - mezcla de estados disabled/readwrite,
  - enfoque de formulario administrativo.

## 5.2 Student
### Dashboard
- KPIs no numericos; enfoque en busqueda + anuncios destacados + eventos filtrables.
- Filtros en grid 4 columnas (texto, categoria, fecha, ubicacion).
- Cards de evento con metadata compacta y CTA Ver detalles.

### Explore
- Muy similar a Dashboard, pero orientado 100% a descubrimiento.
- Agrega imagen en card (h-40 object-cover).

### Event Details
- Tarjeta de detalle con hero image.
- Metadata en grid 2 columnas.
- CTA condicionales por estado:
  - registrarse,
  - desregistrarse,
  - volver,
  - volver a registros.

### Registrations
- Separa eventos proximos y pasados.
- Card por registro + acciones segun estado temporal.

### Messages / Announcements / AnnouncementDetails
- Lista estilo inbox con avatar placeholder circular.
- Barra inferior de accion por item (ver detalle, marcar leido, eliminar).
- Detalle con asunto + mensaje en bloques readonly.

## 5.3 Organizer
### Dashboard
- KPIs: eventos creados, participantes, mensajes nuevos.
- Lista de eventos propios con accion contextual (modificar o ver).

### My Events
- Vista tabular central del rol organizer.
- Acciones por fila:
  - ver detalle,
  - cancelar,
  - ver historial,
  - ver participantes.
- Dialogo modal custom para cancelar con motivo obligatorio.

### Create/Edit Event
- Formularios largos en una tarjeta.
- Campos: titulo, descripcion, categoria, modalidad, unidad, fecha, hora, ubicacion, cupo, imagen.
- Boton principal azul, cancelar gris.

### Event Details / Participants / Registrations / Past*
- Detalle con comportamiento segun contexto (propio, externo, registrado).
- Participantes en tabla con checkbox de asistencia.
- Registrations separa proximos y pasados.

### Messages / SendMessage / Announcements
- Patron casi identico a student, con endpoints y flujos del rol.

## 5.4 Admin
### Dashboard
- KPIs de estado del sistema (activos, usuarios, pendientes, organizadores).
- Bloque de anuncios destacados.

### Explore (Aprobacion)
- Lista de eventos pendientes con acciones Aprobar/Rechazar.
- Alta orientacion a decision rapida.

### Registrations (Moderacion)
- Tabla de eventos con estado + acciones Editar/Eliminar.

### Organizers
- Tabla de organizadores con toggle activo/inactivo.
- Filtro por estado + buscador.

### Reports
- Pantalla de mayor densidad.
- 3 paneles de filtros paralelos + KPIs + listado de reportes recientes + descarga CSV.

### Catalogs
- CRUD liviano por bloques (categorias, modalidades, unidades).
- Formulario a la izquierda + listado existente a la derecha.

### PromotionRequests
- Tabla de solicitudes + acciones Aprobar/Rechazar.
- Dialog (Radix) para confirmar y registrar detalle.

### Messaging/Announcements
- Mismos patrones de listado + detalle + redaccion.

---

## 6) Componentes reutilizables
## 6.1 Shell y navegacion
- App Header:
  - altura aprox 64px,
  - fondo azul oscuro,
  - texto blanco,
  - CTA anuncio + salir.
- Sidebar Nav:
  - ancho fijo aprox 256px,
  - fondo gris claro,
  - botones rectangulares con icono,
  - activo con fondo azul muy claro y borde azul.

## 6.2 Botones
- Primario: azul oscuro, texto blanco, hover azul ligeramente mas claro.
- Exito/confirmacion: verde 700.
- Peligro: rojo 600/700.
- Secundario neutral: gris 400-600.
- Outline (auth/register): borde negro, fondo blanco.
- Tamano dominante:
  - altura visual media (py-2/py-3),
  - anchura variable (full width en formularios, auto en listas).

## 6.3 Campos de entrada
- Input y Select:
  - borde gris,
  - radio redondeado medio,
  - alto compacto,
  - sin decoracion excesiva.
- Textarea:
  - altura minima clara (120-200px segun caso).
- Validacion:
  - mayormente via toast,
  - poca indicacion inline persistente.

## 6.4 Cards y contenedores
- Tarjeta base:
  - fondo blanco,
  - borde 2px gris,
  - radius lg,
  - padding 20-32px.
- Variante inbox:
  - borde negro,
  - bloque superior contenido + bloque inferior acciones separado por border top.

## 6.5 Tablas
- Header oscuro (negro o gris claro segun modulo).
- Celdas con padding comodo.
- Acciones inline con botones pequenos de alto contraste.

## 6.6 Dialogos y overlays
- Dos patrones:
  - modal custom con overlay oscuro semitransparente,
  - dialogo Radix estandar (PromotionRequests).

## 6.7 Feedback
- Toasts globales (sonner) para exito/error.
- Mensajes de carga en texto simple dentro de layout.

## 6.8 Iconografia
- Lucide React en menu y acciones.
- Iconos funcionales (home, calendar, users, file, etc.) sin expresividad ornamental.

---

## 7) Sistema visual
## 7.1 Paleta cromatica detectada (dominante)
- Fondo app: gray-100 (#f3f4f6 aprox).
- Superficie primaria: white (#ffffff).
- Primario de marca/interaccion: blue-900 (#1e3a8a aprox).
- Primario hover: blue-800 (#1e40af aprox).
- Exito: green-700 (#15803d aprox).
- Error/destructivo: red-600/red-700 (#dc2626/#b91c1c aprox).
- Neutral de vuelta/estado: gray-400 a gray-700.
- Bordes:
  - gris (#d1d5db aprox) en la mayoria,
  - negro en inbox/mensajeria.

## 7.2 Variables de tema (base CSS)
- Existe set de tokens en theme.css:
  - background, foreground, primary, secondary, muted, destructive, border, radius.
- Se declara modo dark, pero el UI operativo principal se consume en esquema claro.

## 7.3 Tipografia
- Sin familia custom declarada en fonts.css (archivo vacio).
- Se hereda tipografia por defecto del stack del navegador.
- Escala observada:
  - h1 principal: text-3xl,
  - subtitulo seccion: text-xl/text-2xl,
  - cuerpo: text-sm/text-base,
  - KPI numerico: hasta text-4xl.

## 7.4 Espaciado y densidad
- Densidad media-alta (mucho contenido por pantalla).
- Escala repetida:
  - margenes externos: mb-6/mb-8,
  - paddings internos: p-4/p-6/p-8,
  - gaps: gap-2/gap-4/gap-6.

## 7.5 Bordes, radios y sombras
- Bordes muy presentes y funcionales.
- Radius: rounded / rounded-lg predominante.
- Sombra: casi nula salvo auth container inicial.

---

## 8) Patrones UX/UI recurrentes
## 8.1 Busqueda y filtrado
- Buscador al inicio de modulo.
- Filtros en paralelo (texto, categoria, fecha, ubicacion).
- En varias pantallas el boton Buscar es decorativo; el filtrado ya ocurre en tiempo real.

## 8.2 CRUD y acciones por item
- Listado + acciones contextuales por fila/card.
- Confirmaciones generalmente inmediatas por toast.
- Acciones destructivas expuestas de forma visible (sin confirmacion adicional consistente).

## 8.3 Formularios
- Etiqueta arriba + campo debajo.
- Agrupacion por semantica (datos personales/institucionales).
- Validacion:
  - fuerte en auth,
  - media en formularios de eventos,
  - feedback en toast.

## 8.4 Estados y feedback
- Loading: texto simple ("Cargando...").
- Error: toast y, en algunos casos, vista fallback de "no encontrado".
- Empty states: limitados; en varias listas puede quedar vacio sin mensaje robusto.

## 8.5 Detalle de entidad
- Patroneado:
  - titulo,
  - descripcion,
  - metadata en grid 2 columnas,
  - CTA al pie.

---

## 9) Comportamiento Android nativo
### 9.1 Elementos alineables con Material/Android
- Top bar con acciones de alto nivel.
- Lista de cards para entidades (eventos/anuncios).
- Tablas administrativas traducibles a listas agrupadas o DataTable simplificada.
- Dialogos de confirmacion y formularios secuenciales.

### 9.2 Adaptacion recomendada a Android
- Sidebar web -> NavigationDrawer / NavigationRail.
- Header web -> TopAppBar con acciones (anuncios, perfil, logout).
- Grid 3 columnas web -> en movil:
  - 1 columna en vertical,
  - 2 columnas solo en tablets grandes.
- Botones de accion por card -> boton primario + menu overflow para secundarios.
- Toast web -> Snackbar Android.

### 9.3 Patrones Android a respetar
- Back navigation consistente con historial real.
- Jerarquia visual de CTA:
  - 1 accion primaria por pantalla,
  - secundarios en tonos neutrales.
- Dialogos para acciones irreversibles.

---

## 10) Flujos de usuario
## 10.1 Flujo principal Student
1. Login
2. Dashboard
3. Filtrar/Explorar eventos
4. Ver detalle
5. Registrarse o desregistrarse
6. Revisar Mis Registros
7. Consultar Anuncios/Mensajes

## 10.2 Flujo principal Organizer
1. Login
2. Dashboard organizer
3. Crear evento o gestionar My Events
4. Editar evento o revisar detalle
5. Gestionar participantes
6. Enviar mensajes a participantes
7. Revisar registros pasados

## 10.3 Flujo principal Admin
1. Login
2. Dashboard admin
3. Aprobar/Rechazar eventos pendientes
4. Moderar eventos existentes
5. Gestionar organizadores/promociones
6. Revisar reportes y exportar CSV
7. Publicar anuncios y enviar mensajes

## 10.4 Caminos criticos
- Aprobacion de eventos (admin).
- Gestion de participantes y asistencia (organizer).
- Registro y desregistro de eventos (student/organizer externo).
- Publicacion y consumo de anuncios (todos los roles).

---

## 11) Consistencia visual
### 11.1 Invariantes fuertes
- Misma estructura shell en todas las zonas autenticadas.
- Misma semantica de color para acciones.
- Misma familia de componentes base (cards, inputs, botones, tablas).
- Misma logica de titulos y separacion por bloques.

### 11.2 Reglas implicitas que no deben romperse
- Toda pantalla inicia con titulo claro.
- Toda accion importante tiene boton explicito visible.
- Todo bloque de datos vive dentro de contenedor blanco bordeado.
- La navegacion lateral siempre refleja el rol y el estado activo.

---

## 12) Reglas obligatorias para replicar el diseno
1. Mantener jerarquia visual: titulo -> filtros -> contenido -> acciones.
2. Mantener shell de navegacion con top bar + navegacion lateral (adaptada a Android).
3. Mantener semantica cromatica:
   - azul primario,
   - verde confirmacion,
   - rojo destructivo,
   - gris secundario.
4. Mantener densidad visual media-alta (no convertir a UI vacia minimal extrema).
5. Mantener componentes con bordes visibles y radios moderados.
6. Mantener patron de tarjetas y tablas segun el tipo de tarea.
7. Mantener consistencia de labels y CTAs en idioma y tono funcional.
8. Mantener feedback inmediato con snackbar/toast ante acciones clave.
9. Mantener rutas/flujo conceptual por rol (student, organizer, admin).
10. Mantener comportamiento esperado de botones Volver y detalles contextuales.
11. Priorizar claridad operativa sobre efectos visuales decorativos.
12. Evitar cambios de estilo incompatibles (glassmorphism, neon, skeuomorphism, etc.).

---

## 13) Que NO replicar
1. Inconsistencias de copy:
   - "Mis Mensajes Enviados" usado tambien para bandejas no enviadas.
2. Botones visualmente decorativos sin impacto real (Buscar/Aplicar en algunas vistas).
3. Acciones destructivas sin confirmacion en ciertos contextos.
4. Uso irregular de bordes negros vs grises sin razon funcional clara.
5. Avatares placeholder vacios sin significado.
6. Iconos de respuesta no funcionales (ej. Reply sin accion real).
7. Falta de empty states robustos en listas.
8. Mezcla parcial de componentes custom y direct HTML sin una capa de diseno unificada.
9. Uso puntual de color morado para accion (ver participantes) sin coherencia global de semantica.

---

## 14) Traduccion al nuevo prototipo Pencil (Android nativo)
## 14.1 Principio de transformacion
- No clonar layout web 1:1.
- Traducir patrones funcionales a convenciones Android manteniendo ADN visual.

## 14.2 Mapeo de estructura
- Header web -> TopAppBar con titulo de modulo y acciones contextuales.
- Sidebar web -> Drawer modal (movil) y Rail (tablet).
- Grids web de 3-4 columnas -> listas o grids responsivos Android:
  - movil: 1 columna,
  - tablet: 2 columnas para cards.

## 14.3 Mapeo de componentes a Pencil
- Button primario/secondary/destructive -> 3 estilos reutilizables con tokens.
- EventCard -> componente maestro con variantes (con imagen/sin imagen, estado pasado/proximo).
- MessageCard -> componente con header + body + action bar.
- DataTable admin -> lista de filas con columnas simuladas y acciones inline.
- FormSection -> bloque reusable con titulo, campos y CTA final.
- Modal confirm -> componente overlay reusable.

## 14.4 Grid y spacing recomendados para Android prototipo
- Basar espaciado en unidad 8dp.
- Margen de pantalla: 16dp.
- Gap interno de cards: 12dp-16dp.
- Radius: 8dp-12dp.
- Altura botones principales: 44dp-48dp.

---

## 15) Guia para agentes IA futuros
### 15.1 Como usar este documento
1. Identificar rol objetivo (student/organizer/admin).
2. Seleccionar layout patron correspondiente (Dashboard, Tabla, Form, Detalle, Mensajeria).
3. Aplicar tokens visuales obligatorios (color, borde, radius, spacing).
4. Construir pantalla respetando jerarquia de bloques.
5. Validar con checklist del apartado 16.

### 15.2 Reglas para extender el sistema
- Si se crea una pantalla nueva, debe encajar en uno de los 6 layouts recurrentes.
- Si se crea un componente nuevo, heredar:
  - bordes,
  - radio,
  - escala de tipografia,
  - semantica de color.
- Si se agrega un nuevo estado de flujo, incluir feedback visual inmediato y ruta de retorno clara.

### 15.3 Politica de decisiones ambiguas
- Priorizar coherencia con patrones ya repetidos.
- Preferir simplicidad operativa frente a creatividad visual.
- Cuando existan dos opciones validas, elegir la que mantenga mas similitud con:
  - estructura,
  - densidad,
  - semantica de acciones del frontend original.

---

## 16) Checklist obligatorio de validacion
- [ ] La pantalla mantiene el lenguaje visual original (corporativo-funcional).
- [ ] La navegacion respeta patron por rol y jerarquia detectada.
- [ ] El shell (top bar + nav lateral adaptada) es consistente.
- [ ] Los componentes reutilizados conservan forma, bordes y semantica.
- [ ] La jerarquia visual coincide (titulo -> filtros -> contenido -> acciones).
- [ ] La experiencia se percibe equivalente al frontend de referencia.
- [ ] Se respetan patrones Android de navegacion y feedback.
- [ ] El spacing sigue la grilla de 8dp y densidad media-alta.
- [ ] Las acciones primarias/criticas usan colores semanticos correctos.
- [ ] Los estados de carga, error y vacio estan resueltos claramente.
- [ ] Los flujos criticos (aprobar, registrar, editar, enviar mensaje) son completos.
- [ ] No se introdujeron estilos incompatibles con el sistema base.

---

## 17) Formato y uso operativo del documento
### 17.1 Normas de consumo para agentes
- Tratar este archivo como especificacion normativa, no como sugerencia.
- Antes de generar una pantalla:
  1) mapear rol,
  2) elegir layout base,
  3) instanciar componentes reutilizables,
  4) validar checklist.
- Evitar decisiones esteticas no justificadas por patrones detectados.

### 17.2 Prioridades en caso de conflicto
1. Consistencia de navegacion y flujo.
2. Jerarquia visual y densidad.
3. Semantica cromatica.
4. Detalle estetico fino.

### 17.3 Resultado esperado
- Prototipo Android en Pencil que:
  - se sienta inmediatamente familiar respecto al frontend original,
  - preserve su logica operativa,
  - mejore pequenas debilidades de UX sin romper identidad,
  - y permita escalar nuevas pantallas sin perder coherencia.
