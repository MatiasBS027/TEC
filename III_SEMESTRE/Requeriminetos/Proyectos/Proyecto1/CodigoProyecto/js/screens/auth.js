/* ===================================================
PANTALLAS DE AUTENTICACIÓN - Login y Registro
=================================================== */

// Renderiza las pantallas de login, registro y éxito de registro según el estado actual.
function renderAuth() {
// Pantalla de login con campos para email y contraseña, y botones para iniciar sesión o ir a registro.
    if (state.screen === 'login') return `
    <div class="auth-wrap">
    <div class="auth-card screen">
        <div class="auth-logo">
        <div class="auth-logo-icon">📅</div>
        <div class="auth-logo-text">TEC Eventos<span>Plataforma de eventos universitarios</span></div>
        </div>
        <h2 class="auth-title">Inicia Sesión</h2>
        <div class="form-group">
        <label>Email</label>
        <input class="form-control" type="email" placeholder="tu.email@tec.ac.cr">
        </div>
        <div class="form-group">
        <label>Contraseña</label>
        <input class="form-control" type="password" placeholder="••••••••">
        </div>
        <button class="btn btn-primary btn-block">Iniciar Sesión</button>
        <div class="auth-footer">¿No tienes cuenta? <a onclick="navigate('register')">Regístrate aquí</a></div>
        <hr class="auth-divider">
        <div class="dev-label">🔧 Acceso para Desarrollo</div>
        <div class="dev-buttons">
        <button class="btn-dev btn-dev-student" onclick="setRole('student')">Estudiante</button>
        <button class="btn-dev btn-dev-org" onclick="setRole('organizer')">Organizador</button>
        <button class="btn-dev btn-dev-admin" onclick="setRole('admin')">Administrador</button>
        </div>
    </div>
    </div>`;
// Pantalla de registro con campos para nombre, email, contraseña y tipo de cuenta.
    if (state.screen === 'register') return `
    <div class="auth-wrap">
    <div class="auth-card screen" style="max-height:90vh;overflow-y:auto;">
        <div class="auth-logo">
        <div class="auth-logo-icon">📅</div>
        <div class="auth-logo-text">TEC Eventos<span>Crea tu cuenta</span></div>
        </div>
        <h2 class="auth-title">Registro</h2>
        <div class="form-group"> 
        <label>Nombre Completo</label>
        <input class="form-control" placeholder="Tu nombre completo">
        </div>
        <div class="form-group">
        <label>Email</label>
        <input class="form-control" type="email" placeholder="tu.email@tec.ac.cr">
        </div>
        <div class="form-group">
        <label>Contraseña</label>
        <input class="form-control" type="password" placeholder="Crea una contraseña">
        </div>
        <div class="form-group">
        <label>Tipo de Cuenta</label>
        <select class="form-control">
            <option>Estudiante</option>
            <option>Organizador</option>
        </select>
        </div>
        <button class="btn btn-primary btn-block" onclick="navigate('register-success')">Crear Cuenta</button>
        <div class="auth-footer">¿Ya tienes cuenta? <a onclick="navigate('login')">Inicia sesión</a></div>
    </div>
    </div>`;
// Pantalla de éxito de registro con mensaje de bienvenida y botón para ir a login.
    if (state.screen === 'register-success') return `
    <div class="auth-wrap">
    <div class="auth-card screen">
        <div class="success-screen">
        <div class="success-icon">✅</div>
        <h3>¡Bienvenido!</h3>
        <p>Tu cuenta ha sido creada exitosamente.</p>
        <button class="btn btn-primary" onclick="navigate('login')" style="margin-top:20px;">Ir a Iniciar Sesión</button>
        </div>
    </div>
    </div>`;
}

// Función para establecer el rol del usuario y navegar a la pantalla correspondiente (solo para desarrollo).
function setRole(role) {
    state.role = role;
    if (role === 'student') 
        navigate('student-home');
    else if (role === 'organizer') 
        navigate('org-home');
    else if (role === 'admin') 
        navigate('admin-home');
}

function attachAuthEvents() {}
