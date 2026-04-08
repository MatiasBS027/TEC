/* ===================================================
PANTALLAS DE ADMINISTRADOR
=================================================== */
// Función para renderizar el panel principal del administrador con estadísticas clave y accesos rápidos a las secciones de gestión.
function renderAdminHome() {
// En un caso real, los datos de eventos y usuarios se obtendrían dinámicamente desde el backend.
    return `<div class="screen">
    <h1 style="font-size:28px;margin-bottom:8px;">Panel de Administrador</h1>
    <p style="color:var(--tec-gray);margin-bottom:24px;">Gestión completa de la plataforma</p>
    <div class="stats-row">
        <div class="stat-card">
        <div class="stat-label">Total de Eventos</div>
        <div class="stat-value">${state.events.length}</div>
        </div>
        <div class="stat-card gold">
        <div class="stat-label">Usuarios Registrados</div>
        <div class="stat-value">342</div>
        </div>
        <div class="stat-card green">
            <div class="stat-label">Eventos Activos</div>
        <div class="stat-value">${state.events.filter(e=>e.status==='Activo').length}</div>
        </div>
        <div class="stat-card purple">
        <div class="stat-label">Pendientes Aprobación</div>
        <div class="stat-value">${state.events.filter(e=>e.status==='Pendiente').length}</div>
        </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:24px;">
        <div class="card" onclick="navigate('admin-approvals')" style="cursor:pointer;">
        <div style="font-size:32px;margin-bottom:8px;">✅</div>
        <h3 style="font-weight:700;margin-bottom:4px;">Aprobación de Eventos</h3>
        <p style="color:var(--tec-gray);font-size:13px;">Revisar y aprobar eventos pendientes</p>
        </div>
        <div class="card" onclick="navigate('admin-moderation')" style="cursor:pointer;">
        <div style="font-size:32px;margin-bottom:8px;">🛡️</div>
        <h3 style="font-weight:700;margin-bottom:4px;">Moderación</h3>
        <p style="color:var(--tec-gray);font-size:13px;">Moderar contenido y eventos</p>
        </div>
        <div class="card" onclick="navigate('admin-reports')" style="cursor:pointer;">
        <div style="font-size:32px;margin-bottom:8px;">📊</div>
        <h3 style="font-weight:700;margin-bottom:4px;">Reportes</h3>
        <p style="color:var(--tec-gray);font-size:13px;">Ver estadísticas y reportes</p>
        </div>
    </div>
    </div>`;
}   

// Función para renderizar la pantalla de aprobación de eventos, mostrando una lista de eventos pendientes con opciones para aprobar o rechazar cada evento.
function renderAdminApprovals() {
// En un caso real, esta lista se obtendría dinámicamente desde el backend con los eventos que requieren aprobación.
    const pending = state.events.filter(e=>e.status==='Pendiente');
    return `<div class="screen">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Aprobación de Eventos</h2>
    <div class="approval-list">
        ${pending.length > 0 ? pending.map(e=>`
        <div class="approval-card">
        <div class="approval-icon">📅</div>
        <div class="approval-info">
            <div class="approval-title">${e.title}</div>
            <div class="approval-meta">Categoría: ${e.category} • Fecha: ${e.date} • Cupos: ${e.cupos}</div>
        </div>
        <div class="approval-actions">
            <button class="btn btn-sm btn-success" onclick="approveEvent(${e.id})">✅ Aprobar</button>
            <button class="btn btn-sm btn-danger" onclick="rejectEvent(${e.id})">❌ Rechazar</button>
        </div>
        </div>`).join('') : '<p style="color:var(--tec-gray);">No hay eventos pendientes de aprobación.</p>'}
    </div>
    </div>`;
}

// Cambia estado del evento y fuerza re-render para reflejar aprobación.
function approveEvent(id) { 
    const e=state.events.find(x=>x.id===id); 
    if(e){e.status='Activo';} 
    render(); 
}

// Cambia estado del evento y fuerza re-render para reflejar rechazo.
function rejectEvent(id) { 
    const e=state.events.find(x=>x.id===id); 
    if(e){e.status='Rechazado';} 
    render(); }

function renderAdminOrganizers() {
// En un caso real, esta lista se obtendría dinámicamente desde el backend con los organizadores registrados.
    const orgs = [
    {id:1, name:'Juan García', email:'juan@tec.ac.cr', events:5, status:'Activo'},
    {id:2, name:'María López', email:'maria@tec.ac.cr', events:3, status:'Activo'},
    {id:3, name:'Carlos Pérez', email:'carlos@tec.ac.cr', events:2, status:'Suspendido'},
    ];
// Agrega más organizadores según sea necesario para simular la tabla.
    return `<div class="screen">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Gestionar Organizadores</h2>
    <div class="card">
        <div class="table-wrap">
        <table>
            <thead>
            <tr>
                <th>Nombre</th>
                <th>Email</th>
                <th>Eventos Creados</th>
                <th>Estado</th>
                <th>Acciones</th>
            </tr>
            </thead>
            <tbody>
            ${orgs.map(o=>`
            <tr>
                <td>${o.name}</td>
                <td>${o.email}</td>
                <td>${o.events}</td>
                <td><span class="badge ${o.status==='Activo'?'badge-success':'badge-danger'}">${o.status}</span></td>
                <td class="actions-cell">
                <button class="btn btn-sm btn-outline" onclick="alert('Ver perfil de ${o.name}')">Ver</button>
                <button class="btn btn-sm btn-outline" onclick="alert('${o.status==='Activo'?'Suspender':'Activar'} a ${o.name}')">${o.status==='Activo'?'Suspender':'Activar'}</button>
                </td>
            </tr>`).join('')}
            </tbody>
        </table>
        </div>
    </div>
    </div>`;
}

// Función para obtener el nombre del rol actual del usuario para mostrar en el perfil o en la barra superior.
function renderAdminReports() {
// En un caso real, los datos para los reportes se obtendrían dinámicamente desde el backend con estadísticas reales.
    return `<div class="screen">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Reportes e Informes</h2>
    <div class="card">
        <h3 class="card-title">Resumen General</h3>
        <div class="chart-placeholder">📊 Gráfico de eventos por mes</div>
        <div style="margin-top:24px;">
        <h4 style="font-weight:700;margin-bottom:12px;">Estadísticas Generales</h4>
        <table style="width:100%;">
            <tr>
            <td style="padding:8px;">Total de Eventos:</td>
            <td style="padding:8px;text-align:right;font-weight:700;">${state.events.length}</td>
            </tr>
            <tr>
            <td style="padding:8px;">Participantes Totales:</td>
            <td style="padding:8px;text-align:right;font-weight:700;">${state.events.reduce((a,b)=>a+b.taken,0)}</td>
            </tr>
            <tr>
            <td style="padding:8px;">Tasa de Asistencia Promedio:</td>
            <td style="padding:8px;text-align:right;font-weight:700;">87%</td>
            </tr>
        </table>
        </div>
    </div>
    </div>`;
}

// Función para renderizar la pantalla de moderación de eventos, mostrando una lista de eventos con opciones para ver detalles o eliminar cada evento.
function renderAdminModeration() {
// En un caso real, esta lista se obtendría dinámicamente desde el backend con todos los eventos para moderar.
    return `<div class="screen">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Moderación de Eventos</h2>
        <div class="card">
        <div class="table-wrap">
        <table>
            <thead>
            <tr>
                <th>Evento</th>
                <th>Organizador</th>
                <th>Categoría</th>
                <th>Estado</th>
                <th>Acciones</th>
            </tr>
            </thead>
            <tbody>
            ${state.events.map((e,i)=>`
            <tr>
                <td>${e.title}</td>
                <td>Organizador ${i+1}</td>
                <td><span class="badge badge-blue">${e.category}</span></td>
                <td><span class="badge ${getStatusBadge(e.status)}">${e.status}</span></td>
                <td class="actions-cell">
                <button class="btn btn-sm btn-primary" onclick="viewEvent(${e.id}, 'admin')">Ver</button>
                <button class="btn btn-sm btn-danger" onclick="confirmDeleteMod(${e.id})">🗑️ Eliminar</button>
                </td>
            </tr>`).join('')}
            </tbody>
        </table>
        </div>
    </div>
    </div>`;
}

// Elimina un evento desde moderación; la tabla se recalcula al re-renderizar.
function confirmDeleteMod(id){if(confirm('¿Eliminar este evento?')){state.events=state.events.filter(e=>e.id!==id);render();}}

// Función para renderizar la pantalla de anuncios del sistema, con formulario para publicar nuevos anuncios y lista de anuncios recientes.
function renderAdminAnnouncements() {
// En un caso real, los anuncios se obtendrían dinámicamente desde el backend y el formulario enviaría datos al backend para crear nuevos anuncios.
    return `<div class="screen">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:20px;">Anuncios del Sistema</h2>
    <div class="card announce-compose">
        <h3 class="card-title">Publicar nuevo anuncio</h3>
        <div class="form-group">
        <label>Título del Anuncio</label>
        <input class="form-control" placeholder="Ingrese el título">
        </div>
        <div class="form-group">
        <label>Destinatarios</label>
        <select class="form-control">
            <option>Todos</option>
            <option>Solo Estudiantes</option>
            <option>Solo Organizadores</option>
        </select>
        </div>
        <div class="form-group">
        <label>Mensaje</label>
        <textarea class="form-control textarea" id="new-announce" placeholder="Escribe tu anuncio aquí..."></textarea>
        </div>
        <button class="btn btn-primary" onclick="publishAnnounce()">📢 Publicar Anuncio</button>
    </div>
    <div style="margin-top:24px;">
        <h3 class="card-title">Anuncios Publicados</h3>
        <div class="msg-list">
        ${state.messages.slice(0,3).map(m=>`
        <div class="msg-item">
            <div class="msg-avatar">📢</div>
            <div class="msg-body">
            <div class="msg-sender">${m.subject}</div>
            <div class="msg-preview">${m.text}</div>
            <div class="msg-time">${m.time}</div>
            </div>
        </div>`).join('')}
        </div>
    </div>
    </div>`;
}

// Función para obtener el nombre del rol actual del usuario para mostrar en el perfil o en la barra superior.
function publishAnnounce() {
// En un caso real, esta función enviaría el nuevo anuncio al backend para ser guardado y luego se re-renderizaría la lista de anuncios.
    const ta = document.getElementById('new-announce');
    if(ta && ta.value.trim()) {  // Simula publicación exitosa del anuncio.
    alert('Anuncio publicado exitosamente.');
    ta.value = '';
    render();
    } else {
    alert('Por favor, ingrese un mensaje.');
    }
}
