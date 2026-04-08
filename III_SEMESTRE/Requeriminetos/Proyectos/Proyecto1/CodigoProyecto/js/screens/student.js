/* ===================================================
PANTALLAS DE ESTUDIANTE
=================================================== */

// Pantalla de inicio del estudiante con eventos destacados y barra de búsqueda.
function renderStudentHome() {
    const events = state.events.filter(e=>e.status!=='Finalizado').slice(0,3);
    return `<div class="screen">
// Banner de bienvenida con título y descripción.
    <div style="margin-bottom:24px;">
        <h1 style="font-size:28px;">¡Bienvenido, Estudiante!</h1>
        <p style="color:var(--tec-gray);margin-top:4px;">Explora y regístrate en los eventos disponibles</p>
    </div>
    <div class="search-bar">
        <input class="search-input" placeholder="Buscar eventos...">
        <select class="filter-select">
        <option>Todas las categorías</option>
        <option>Académico</option>
        <option>Deportivo</option>
        <option>Cultural</option>
        <option>Tecnología</option>
        </select>
        <button class="btn btn-primary">Buscar</button>
    </div>
    <h3 class="card-title">Eventos Destacados</h3>
    <div class="events-grid">
        ${events.map(e=>renderEventCard(e, 'student')).join('')}
    </div>
    </div>`;
}

// Renderiza la barra superior con título dinámico según la pantalla actual y botón de notificaciones.
function renderExploreEvents() {
    return `<div class="screen">
    <div class="search-bar">
        <input class="search-input" placeholder="Buscar eventos...">
        <select class="filter-select">
        <option>Todas las categorías</option>
        <option>Académico</option>
        <option>Deportivo</option>
        <option>Cultural</option>
        </select>
        <button class="btn btn-primary">Buscar</button>
    </div>
    <div class="events-grid">
        ${state.events.map(e=>renderEventCard(e, 'student')).join('')}
    </div>
    </div>`;
}

// Función para renderizar la barra superior con título dinámico y botón de notificaciones.
function viewEvent(id, ctx) {
    state.currentEventId = id;
    if(ctx==='organizer') 
        navigate('event-detail-org', {eventId:id});
    else 
        navigate('event-detail', {eventId:id});
}

/**
* Pantalla de detalle compartida entre estudiante y organizador.
* El contexto define qué acciones se muestran en el bloque final.
* @param {'student'|'organizer'} ctx Contexto de visualización.
*/
function renderEventDetail(ctx) {
    const ev = state.events.find(e=>e.id===state.currentEventId) || state.events[0];
    const icons = {Académico:'📚',Deportivo:'⚽',Cultural:'🎵',Tecnología:'💻',Desarrollo:'🖥️',Negocios:'💼'};
    const icon = icons[ev.category]||'📅';
    const isRegistered = state.myRegistrations.includes(ev.id);

// Acciones condicionales según rol/contexto para reutilizar una sola vista.
    const orgButtons = ctx==='organizer' ? `
    <button class="btn btn-gold" onclick="navigate('edit-event')">✏️ Modificar Evento</button>
    <button class="btn btn-outline" onclick="navigate('participants')">👥 Ver participantes</button>
    <button class="btn btn-outline" onclick="navigate('my-events')">← Volver</button>
    ` : `
    <button class="btn btn-primary" onclick="registerEvent(${ev.id})">${isRegistered?'✓ Registrado':'Registrarse en el evento'}</button>
    <button class="btn btn-outline" onclick="goBack()">← Volver</button>
    `;
// La pantalla de detalle muestra información completa del evento y acciones según el rol.
    return `<div class="screen">
    <div class="detail-banner">${icon}</div>
    <div class="detail-header">
        <h2 class="detail-title">${ev.title}</h2>
        <div class="detail-meta">
        <span>📅 ${ev.date}</span>
        <span>📍 ${ev.location}</span>
        <span>👥 ${ev.taken}/${ev.cupos} participantes</span>
        <span class="badge ${getStatusBadge(ev.status)}">${ev.status}</span>
        </div>
    </div>
    <div class="card">
        <p class="detail-desc">Descripción del evento: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <div class="detail-stats">
        <div class="detail-stat">
            <div class="detail-stat-val">${ev.taken}</div>
            <div class="detail-stat-label">Inscritos</div>
        </div>
        <div class="detail-stat">
            <div class="detail-stat-val">${ev.cupos}</div>
            <div class="detail-stat-label">Cupos</div>
        </div>
        <div class="detail-stat">
            <div class="detail-stat-val">${ev.attendance}</div>
            <div class="detail-stat-label">Asistencia</div>
        </div>
        </div>
        <div class="detail-actions">
        ${orgButtons}
        </div>
    </div>
    </div>`;
}

// Función para registrar al estudiante en un evento y actualizar la vista.
function registerEvent(id) {
    if (!state.myRegistrations.includes(id)) {
    state.myRegistrations.push(id);
    render();
    }
}

// Pantalla para mostrar los eventos en los que el estudiante está registrado, separados por próximos y pasados.
function renderMyRegistrations() {
    const upcoming = state.events.filter(e=>state.myRegistrations.includes(e.id)&&e.status!=='Finalizado');
    const past = state.events.filter(e=>state.myRegistrations.includes(e.id)&&e.status==='Finalizado');
// Permite reutilizar la misma pantalla para estudiante y organizador.
    const ctx = state.role==='organizer'?'organizer':'student';
    return `<div class="screen">
    <h3 class="card-title">Eventos Próximos</h3>
    <div class="events-grid">${upcoming.map(e=>renderEventCard(e,ctx)).join('')||'<p style="color:var(--tec-gray)">No tienes eventos próximos.</p>'}</div>
    <h3 class="card-title" style="margin-top:28px;">Eventos Pasados</h3>
    <div class="events-grid">${past.map(e=>renderEventCard(e,ctx)).join('')||'<p style="color:var(--tec-gray)">No tienes eventos pasados.</p>'}</div>
    </div>`;
}

// Función para renderizar la barra superior con título dinámico según la pantalla actual y botón de notificaciones.
function renderAnnouncements(ctx) {
    return `<div class="screen">
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
    <div style="margin-top:16px;"><button class="btn btn-outline" onclick="goBack()">← Volver</button></div>
    </div>`;
}

// Pantalla de perfil del estudiante con opción para editar información personal.
function viewMsg(id) {
    state.currentMsgId = id;
    navigate('msg-detail');
}

// Renderiza la pantalla de detalle del mensaje con opción para eliminar o volver.
function deleteMsg(id) {
    state.messages = state.messages.filter(m=>m.id!==id);
    render();
}


// Función para renderizar la pantalla de perfil del estudiante con opción para editar información personal.
function renderMsgDetail() {
    const msg = state.messages.find(m=>m.id===state.currentMsgId)||state.messages[0];
    return `<div class="screen">
    <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <div>
            <h3 style="font-size:18px;font-weight:700;margin-bottom:4px;">${msg.subject}</h3>
            <p style="color:var(--tec-gray);font-size:13px;">De: ${msg.from}</p>
        </div>
        <span style="color:var(--tec-gray);font-size:12px;">${msg.time}</span>
        </div>
        <hr style="border:none;border-top:1px solid var(--tec-border);margin:16px 0;">
        <p style="line-height:1.6;color:#374151;">${msg.text}</p>
        <div style="margin-top:16px;display:flex;gap:8px;">
        <button class="btn btn-outline btn-sm" onclick="deleteMsg(${msg.id})">🗑️ Eliminar</button>
        <button class="btn btn-outline btn-sm" onclick="goBack()">← Volver</button>
        </div>
    </div>
    </div>`;
}

// Función para renderizar la pantalla de perfil del estudiante con opción para editar información personal.
function renderProfile(editing) {
    return `<div class="screen">
    <div class="card">
        <div class="profile-header">
        <div class="profile-pic">👤</div>
        <div>
            <h3>Nombre del Usuario</h3>
            <p>usuario@tec.ac.cr</p>
            <p style="font-size:11px;color:var(--tec-gray);margin-top:4px;">Miembro desde 2024</p>
        </div>
        </div>
        <hr style="border:none;border-top:1px solid var(--tec-border);margin:16px 0;">
        <div class="form-group">
        <label>Nombre Completo</label>
        <input class="form-control" value="Nombre del Usuario" ${editing?'':'disabled'}>
        </div>
        <div class="form-group">
        <label>Email</label>
        <input class="form-control" type="email" value="usuario@tec.ac.cr" ${editing?'':'disabled'}>
        </div>
        <div class="form-group">
        <label>Teléfono</label>
        <input class="form-control" value="+506 8765 4321" ${editing?'':'disabled'}>
        </div>
        <div class="form-actions">
        ${editing ? `
            <button class="btn btn-primary" onclick="saveProfile()">💾 Guardar</button>
            <button class="btn btn-outline" onclick="render()">Cancelar</button>
        ` : `
            <button class="btn btn-gold" onclick="editProfile()">✏️ Editar Perfil</button>
        `}
        </div>
    </div>
    </div>`;
}

// Funciones para manejar el modo de edición del perfil.
function editProfile() {
    state.editingProfile = true;
    render();
}

// Función para guardar los cambios del perfil (simulado) y volver al modo de visualización.
function saveProfile() {
    state.editingProfile = false;
    render();
}
