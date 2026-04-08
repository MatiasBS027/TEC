/* ===================================================
PANTALLAS DE ORGANIZADOR
=================================================== */


// Función para renderizar la barra lateral con navegación dinámica según el rol del usuario.
function renderOrgHome() {
    const myEvs = state.events.slice(0,3);
    return `<div class="screen">
    <div class="stats-row">
        <div class="stat-card gold">
        <div class="stat-label">Mis Eventos</div>
        <div class="stat-value">${state.events.length}</div>
        </div>
        <div class="stat-card green">
        <div class="stat-label">Total Participantes</div>
        <div class="stat-value">${state.events.reduce((a,b)=>a+b.taken,0)}</div>
        </div>
        <div class="stat-card purple">
        <div class="stat-label">Eventos Activos</div>
        <div class="stat-value">${state.events.filter(e=>e.status==='Activo').length}</div>
        </div>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
        <h3 class="card-title">Mis Eventos Recientes</h3>
        <button class="btn btn-primary" onclick="navigate('create-event')">➕ Nuevo Evento</button>
    </div>
    <div class="search-bar"><input class="search-input" placeholder="Buscar eventos..."><button class="btn btn-primary">Buscar</button></div>
    <div class="events-grid">${myEvs.map(e=>renderEventCard(e,'organizer')).join('')}</div>
    </div>`;
}


// Función para renderizar la pantalla de eventos del organizador con tabla detallada y acciones para cada evento.
function renderMyEvents() {
    return `<div class="screen">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
        <h2 style="font-size:24px;font-weight:700;">Mis Eventos</h2>
        <button class="btn btn-primary" onclick="navigate('create-event')">➕ Crear Evento</button>
    </div>
    <div class="card">
        <div class="table-wrap">
        <table>
            <thead>
            <tr>
                <th>Nombre del Evento</th>
                <th>Categoría</th>
                <th>Fecha</th>
                <th>Participantes</th>
                <th>Estado</th>
                <th>Acciones</th>
            </tr>
            </thead>
            <tbody>
            ${state.events.map(e=>`
            <tr>
                <td>${e.title}</td>
                <td><span class="badge badge-blue">${e.category}</span></td>
                <td>${e.date}</td>
                <td>${e.taken}/${e.cupos}</td>
                <td><span class="badge ${getStatusBadge(e.status)}">${e.status}</span></td>
                <td class="actions-cell">
                <button class="btn btn-sm btn-primary" onclick="viewEvent(${e.id}, 'organizer')">Ver</button>
                <button class="btn btn-sm btn-gold" onclick="navigate('edit-event')">Editar</button>
                <button class="btn btn-sm btn-outline" onclick="navigate('participants')">Participantes</button>
                </td>
            </tr>`).join('')}
            </tbody>
        </table>
        </div>
    </div>
    </div>`;
}

/**
* Formulario reutilizable para crear/editar.
* También lo consume administrador en modo edición para evitar duplicar plantilla.
* @param {boolean} [editing=false] Define si está en modo edición.
* @param {boolean} [admin=false] Bandera reservada para contexto admin.
*/
function renderEventForm(editing=false, admin=false) {
    return `<div class="screen">
    <div class="card">
        <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">
        ${editing ? '✏️ Modificar Evento' : '➕ Crear Nuevo Evento'}
        </h2>
        <div class="form-section-title">Información Básica</div>
        <div class="form-group">
        <label>Título del Evento</label>
        <input class="form-control" placeholder="Ingrese el título del evento">
        </div>
        <div class="form-row">
        <div class="form-group">
            <label>Categoría</label>
            <select class="form-control">
            <option>Académico</option>
            <option>Deportivo</option>
            <option>Cultural</option>
            <option>Tecnología</option>
            </select>
        </div>
        <div class="form-group">
            <label>Fecha</label>
            <input class="form-control" type="date">
        </div>
        </div>
        <div class="form-group">
        <label>Ubicación</label>
        <input class="form-control" placeholder="Ingrese la ubicación del evento">
        </div>
        <div class="form-section-title">Detalles</div>
        <div class="form-row">
        <div class="form-group">
            <label>Cupos Disponibles</label>
            <input class="form-control" type="number" placeholder="Número de cupos">
        </div>
        <div class="form-group">
            <label>Hora del Evento</label>
            <input class="form-control" type="time">
        </div>
        </div>
        <div class="form-group">
        <label>Descripción</label>
        <textarea class="form-control textarea" placeholder="Describe tu evento..."></textarea>
        </div>
        <div class="form-group">
        <label>Imagen del Evento</label>
        <div class="img-upload">📸 Arrastra la imagen aquí o haz clic</div>
        </div>
        <div class="form-actions">
        <button class="btn btn-primary" onclick="submitEvent()">📤 Enviar para Aprobación</button>
        ${editing ? '<button class="btn btn-danger" onclick="confirmDelete()">🗑️ Eliminar</button>' : ''}
        <button class="btn btn-outline" onclick="goBack()">Cancelar</button>
        </div>
    </div>
    </div>`;
}


// Función para manejar el envío del formulario de creación/edición de evento (simulado).
function submitEvent() {
    alert('✅ Evento enviado para aprobación exitosamente.');
    goBack();
}

// Función para confirmar eliminación de evento (simulado).
function confirmDelete() {
    if(confirm('¿Está seguro de que desea eliminar este evento?')) { alert('Evento eliminado.'); navigate('admin-moderation'); }
}


// Función para renderizar la pantalla de participantes del evento con tabla detallada y acciones para contactar a los participantes.
function renderParticipants() {
    const pList = [
    {name:'Juan Pérez', email:'juan.perez@tec.ac.cr', attended:true},
    {name:'María García', email:'maria.garcia@tec.ac.cr', attended:false},
    {name:'Carlos López', email:'carlos.lopez@tec.ac.cr', attended:true},
    ];
// En un caso real, esta lista se obtendría dinámicamente según el evento seleccionado.
    return `<div class="screen">
    <div class="card">
        <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Participantes del Evento</h2>
        <div class="table-wrap">
        <table>
            <thead>
            <tr>
                <th>Nombre</th>
                <th>Email</th>
                <th>Estado de Asistencia</th>
                <th>Acciones</th>
            </tr>
            </thead>
            <tbody>
            ${pList.map(p=>`
            <tr>
                <td>${p.name}</td>
                <td>${p.email}</td>
                <td><span class="badge ${p.attended?'badge-success':'badge-warning'}">${p.attended?'Asistió':'No Asistió'}</span></td>
                <td class="actions-cell">
                <button class="btn btn-sm btn-outline" onclick="alert('Enviando email a ${p.email}')">📧 Contactar</button>
                </td>
            </tr>`).join('')}
            </tbody>
        </table>
        </div>
        <button class="btn btn-outline" onclick="goBack()" style="margin-top:16px;">← Volver</button>
    </div>
    </div>`;
}

// Función para renderizar la pantalla de mensajes del organizador con lista de mensajes y formulario para enviar nuevos mensajes a los participantes.
function renderOrgMessages() {
    return `<div class="screen">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;">
        <h2 style="font-size:20px;font-weight:700;">Mis Mensajes</h2>
    </div>
    <div class="msg-list">
        ${state.messages.map(m=>`
        <div class="msg-item">
        <div class="msg-avatar">${m.from.charAt(0)}</div>
        <div class="msg-body">
            <div style="display:flex;align-items:center;justify-content:space-between;">
            <div>
                <div class="msg-sender">${m.from}</div>
                <div class="msg-time">${m.time}</div>
            </div>
            <button class="btn btn-sm btn-outline" onclick="viewMsg(${m.id})">Ver</button>
            </div>
            <div class="msg-preview">${m.text}</div>
        </div>
        </div>`).join('')}
    </div>
    ${renderSendMsgForm()}
    </div>`;
}

// Función para renderizar el formulario de envío de mensajes a los participantes del evento, con selección de evento, asunto y cuerpo del mensaje.
function renderSendMsgForm() {
    return `
    <div class="card" style="margin-top:24px;">
    <h3 class="card-title">Enviar Mensaje a Participantes</h3>
    <div class="form-group"><label>Seleccionar Evento</label>
        <select class="form-control">
        ${state.events.map(e=>`<option>${e.title}</option>`).join('')}
        </select>
    </div>
    <div class="form-group"><label>Asunto</label><input class="form-control" placeholder="Ingrese el asunto del mensaje"></div>
    <div class="form-group"><label>Mensaje</label><textarea class="form-control textarea" placeholder="Escribe tu mensaje aquí..."></textarea></div>
    <button class="btn btn-primary" onclick="alert('Mensaje enviado exitosamente.')">📤 Enviar Mensaje</button>
    </div>`;
}
