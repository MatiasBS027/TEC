/* ===================================================
COMPONENTES - Elementos de UI reutilizables
=================================================== */

/* BARRA LATERAL */
function renderSidebar() {
    const navs = getNavItems();
    return `
    <aside class="sidebar" id="sidebar">
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">📅</div>
        <div class="sidebar-logo-text">TEC Eventos<span>v1.0</span></div>
    </div>
    <nav class="sidebar-nav">
        ${navs.map(n=>`
        <div class="nav-item" onclick="navigate('${n.screen}')">
        <span class="nav-icon">${n.icon}</span>
        <span>${n.label}</span>
        </div>`).join('')}
    </nav>
    <div class="sidebar-footer">
        <div class="sidebar-user">
        <div class="sidebar-avatar">${getInitials()}</div>
        <div class="sidebar-user-info">
            <div class="sidebar-user-name">Usuario</div>
            <div class="sidebar-user-role">${getRoleLabel()}</div>
        </div>
        </div>
    </div>
    </aside>`;
}

/* BARRA SUPERIOR */
function renderTopbar() {
    const titles = {
    'student-home':'Panel de Estudiante','explore-events':'Explorar Eventos',
    'my-registrations':'Mis Registros','profile':'Perfil','event-detail':'Detalle del Evento',
    'announcements':'Anuncios','msg-detail':'Detalle de Mensaje',
    'org-home':'Panel de Organizador','my-events':'Mis Eventos','org-registrations':'Mis Registros',
    'org-messages':'Mensajes','org-profile':'Perfil','create-event':'Crear Evento',
    'edit-event':'Modificar Evento','event-detail-org':'Detalle del Evento','participants':'Participantes',
    'admin-home':'Panel de Administrador','admin-organizers':'Gestionar Organizadores',
    'admin-reports':'Informes','admin-moderation':'Moderación de Eventos',
    'admin-announcements':'Anuncios del Sistema','admin-approvals':'Aprobación de Eventos',
    'admin-messages':'Mensajes','admin-edit-event':'Modificar Evento',
    };
    return `
    <header class="topbar">
    <div class="topbar-title">${titles[state.screen]||'Plataforma de Eventos TEC'}</div>
    <div class="topbar-right">
        <button class="notif-btn" onclick="toggleNotif()">🔔${state.messages.length>0?'<div class="notif-dot"></div>':''}</button>
    </div>
    </header>`;
}

/* PANEL DE NOTIFICACIONES */
function renderNotifPanel() {
    return `
    <div class="notif-panel ${state.notifOpen?'open':''}" id="notif-panel">
    <div class="notif-panel-title">Anuncios <button class="notif-close" onclick="toggleNotif()">✕</button></div>
    ${state.messages.map(m=>`
    <div class="notif-item">
        <div class="notif-item-title">${m.subject}</div>
        <div class="notif-item-text">${m.text}</div>
        <div class="notif-item-time">${m.time}</div>
    </div>`).join('')}
    </div>`;
}

function toggleNotif() {
    state.notifOpen = !state.notifOpen;
    const panel = document.getElementById('notif-panel');
    if(panel) panel.classList.toggle('open', state.notifOpen);
}

/**
* Renderiza una tarjeta de evento reutilizable para distintos contextos.
* @param {object} event Datos del evento.
* @param {'student'|'organizer'|'admin'} [ctx='student'] Contexto de navegación al detalle.
* @returns {string} HTML de tarjeta.
*/
function renderEventCard(event, ctx='student') {
    const icons = {Académico:'📚',Deportivo:'⚽',Cultural:'🎵',Tecnología:'💻',Desarrollo:'🖥️',Negocios:'💼'};
    const icon = icons[event.category]||'📅';
    return `
    <div class="event-card">
    <div class="event-card-img" style="background:linear-gradient(135deg,${getCatColor(event.category)});">${icon}</div>
    <div class="event-card-body">
        <div class="event-card-title">${event.title}</div>
        <div class="event-card-meta">
        <span>📅 ${event.date}</span>
        <span>📍 ${event.location}</span>
        <span class="badge ${getStatusBadge(event.status)}">${event.status}</span>
        </div>
    </div>
    <div class="event-card-footer">
        <div class="event-cupos">${event.taken}/${event.cupos} inscritos</div>
        <button class="btn btn-sm btn-primary" onclick="viewEvent(${event.id}, '${ctx}')">Ver →</button>
    </div>
    </div>`;
}
