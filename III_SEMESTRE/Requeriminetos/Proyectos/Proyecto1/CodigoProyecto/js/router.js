/* ===================================================
ENRUTADOR - Lógica de navegación SPA
=================================================== */

/**
* Cambia de pantalla dentro de la SPA actualizando el estado global.
* No recarga el navegador: solo modifica `state` y vuelve a renderizar.
* @param {string} screen Pantalla destino.
* @param {{eventId?: number, msgId?: number}} [data={}] Datos opcionales de contexto.
*/
function navigate(screen, data={}) {
    state.prevScreen = state.screen;
    state.screen = screen;
    if (data.eventId !== undefined) 
        state.currentEventId = data.eventId;
    if (data.msgId !== undefined) 
        state.currentMsgId = data.msgId;
    render();
}

/**
* Regresa a la pantalla anterior registrada en el estado.
* Si no existe historial, vuelve al login por seguridad.
*/
function goBack() {
    navigate(state.prevScreen || 'login');
}
