/* ===================================================
ESTADO - Estado global de la aplicación
=================================================== */

let state = {
    screen: 'login',       // pantalla actual
    prevScreen: null,
    role: null,            // 'student' | 'organizer' | 'admin'
    notifOpen: false,
    activeTab: 0,
    editingProfile: false,
    modalOpen: false,
    //datos de ejemplo para simular comportamiento sin backend
    events: [
    {id:1, title:'Charla de Inteligencia Artificial', category:'Académico', date:'2024-10-26', location:'Auditorio Principal, TEC Cartago', cupos:50, icon:'🤖', status:'Activo', participants:[], taken:12, attendance:10},
    {id:2, title:'Torneo de Fútbol Intercampus', category:'Deportivo', date:'2024-11-15', location:'Cancha de Fútbol, TEC Cartago', cupos:20, icon:'⚽', status:'Pendiente', participants:[], taken:8, attendance:0},
    {id:3, title:'Concierto de la Orquesta Sinfónica', category:'Cultural', date:'2024-12-01', location:'Teatro Universitario, TEC San José', cupos:200, icon:'🎵', status:'Finalizado', participants:[], taken:180, attendance:170},
    {id:4, title:'Charla de Energías Limpias', category:'Académico', date:'2024-10-26', location:'Auditorio Principal, TEC Cartago', cupos:50, icon:'🌱', status:'Activo', participants:[], taken:20, attendance:0},
    {id:5, title:'Hackathon Anual', category:'Tecnología', date:'2024-09-01', location:'Laboratorio B, TEC Cartago', cupos:100, icon:'💻', status:'Finalizado', participants:[], taken:95, attendance:90},
    ],
    myRegistrations: [1, 3],
    messages: [
    {id:1, from:'Charla de IA', time:'7:34 AM', text:'Se cancela sesión por falta de participantes.', subject:'Cancelación'},
    {id:2, from:'Taller de Programación', time:'12:34 PM', text:'Favor traer materiales solicitados.', subject:'Recordatorio'},
    {id:3, from:'Orquesta Sinfónica', time:'2:44 PM', text:'Descripción del aviso...', subject:'Información'},
    ],
    currentEventId: null,
    currentMsgId: null,
};
