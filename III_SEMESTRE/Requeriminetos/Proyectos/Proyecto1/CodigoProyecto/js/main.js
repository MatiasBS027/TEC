/* ===================================================
MAIN - Motor de renderizado y enlace de eventos
=================================================== */

/**
* Punto central de pintado de UI.
* Decide si mostrar autenticación o layout principal según `state.screen`.
*/
function render() {
    const app = document.getElementById('app');
// Pantallas de autenticación
    const authScreens = ['login','register','register-success'];
    if (authScreens.includes(state.screen)) {
    app.innerHTML = renderAuth();
    attachAuthEvents();
    return;
    }
  // Aplicación principal
    app.innerHTML = `
    ${renderSidebar()}
    ${renderTopbar()}
    <div class="content-area" id="content-area">
        ${renderScreen()}
    </div>
    ${renderNotifPanel()}
    `;
    attachMainEvents();
}

/**
* Enrutador visual por pantalla.
* Mapea el valor de `state.screen` hacia su función render correspondiente.
* @returns {string} HTML de la pantalla actual.
*/
function renderScreen() {
    const s = state.screen;
    if (s==='student-home') 
        return renderStudentHome();
    if (s==='explore-events') 
        return renderExploreEvents();
    if (s==='my-registrations') 
        return renderMyRegistrations();
    if (s==='profile') 
        return renderProfile(false);
    if (s==='event-detail') 
        return renderEventDetail('student');
    if (s==='announcements') 
        return renderAnnouncements('student');
    if (s==='msg-detail') 
        return renderMsgDetail();
// Organizador
    if (s==='org-home') 
        return renderOrgHome();
    if (s==='my-events') 
        return renderMyEvents();
    if (s==='org-registrations') 
        return renderMyRegistrations();
    if (s==='org-messages') 
        return renderOrgMessages();
    if (s==='org-profile') 
        return renderProfile(false);
    if (s==='create-event') 
        return renderEventForm(false);
    if (s==='edit-event') 
        return renderEventForm(true);
    if (s==='event-detail-org') 
        return renderEventDetail('organizer');
    if (s==='participants') 
        return renderParticipants();
// Administrador
    if (s==='admin-home') 
        return renderAdminHome();
    if (s==='admin-organizers') 
        return renderAdminOrganizers();
    if (s==='admin-reports') 
        return renderAdminReports();
    if (s==='admin-moderation') 
        return renderAdminModeration();
    if (s==='admin-announcements') 
        return renderAdminAnnouncements();
    if (s==='admin-approvals') 
        return renderAdminApprovals();
    if (s==='admin-messages') 
        return renderOrgMessages();
    if (s==='admin-edit-event') 
        return renderEventForm(true, true);
    return '<p>Pantalla no encontrada</p>';
}

function attachMainEvents() {
// Cierre de panel de notificaciones (placeholder para eventos globales)
    document.addEventListener('click', function handler(e) {
    }, {once:true});
}

/* ===================================================
INICIO
=================================================== */
render();
