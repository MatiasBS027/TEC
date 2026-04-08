/* ===================================================
UTILIDADES - Funciones de apoyo
=================================================== */

function getRoleLabel(){
    if(state.role==='student') 
    return 'Estudiante';
    if(state.role==='organizer') 
    return 'Organizador';
    if(state.role==='admin') 
    return 'Administrador';
    return 'Usuario';
}

function getInitials(){
    return 'UT';
}

function getCatColor(cat) {
// Mantiene centralizada la paleta por categoría para gradientes de tarjetas.
    const map = {
    Académico:'#003B8E,#0060e6',
    Deportivo:'#065F46,#10B981',
    Cultural:'#7C3AED,#A78BFA',
    Tecnología:'#0F766E,#14B8A6',
    Desarrollo:'#1D4ED8,#60A5FA',
    Negocios:'#92400E,#F59E0B'
    };
    return map[cat]||'#003B8E,#0060e6';
}

function getStatusBadge(s){
// Centraliza colores de estado para consistencia visual.
    return s==='Activo'?'badge-success':s==='Pendiente'?'badge-warning':s==='Rechazado'?'badge-danger':'badge-blue';
}

function getNavItems() {
// Configuración declarativa de menú por rol.
    // Para estudiante, el menú se muestra completo en el sidebar, no es necesario repetirlo aquí.
    if (state.role === 'student') return [
    {icon:'🏠', label:'Inicio', screen:'student-home'},
    {icon:'🔍', label:'Explorar Eventos', screen:'explore-events'},
    {icon:'📋', label:'Mis Registros', screen:'my-registrations'},
    {icon:'👤', label:'Perfil', screen:'profile'},
    ];
    // Para organizador, el menú se muestra completo en el sidebar, no es necesario repetirlo aquí.
    if (state.role === 'organizer') return [
    {icon:'🏠', label:'Inicio', screen:'org-home'},
    {icon:'📅', label:'Mis Eventos', screen:'my-events'},
    {icon:'📋', label:'Mis Registros', screen:'org-registrations'},
    {icon:'✉️', label:'Mensajes', screen:'org-messages'},
    {icon:'🔍', label:'Explorar Eventos', screen:'explore-events'},
    {icon:'👤', label:'Perfil', screen:'org-profile'},
    ];
    // Para administrador, el menú se muestra completo en el sidebar, no es necesario repetirlo aquí.
    if (state.role === 'admin') return [
    {icon:'🏠', label:'Inicio', screen:'admin-home'},
    {icon:'👥', label:'Organizadores', screen:'admin-organizers'},
    {icon:'📊', label:'Informes', screen:'admin-reports'},
    {icon:'🛡️', label:'Moderación', screen:'admin-moderation'},
    {icon:'📢', label:'Anuncios', screen:'admin-announcements'},
    {icon:'✅', label:'Aprobaciones', screen:'admin-approvals'},
    {icon:'✉️', label:'Mensajes', screen:'admin-messages'},
    ];
    return [];
}
