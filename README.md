# TEC - Repositorio de Carrera Académica

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Repository Size](https://img.shields.io/github/repo-size/MatiasBS027/TEC)
![Last Update](https://img.shields.io/github/last-commit/MatiasBS027/TEC)

## 📚 Descripción

Repositorio educativo que contiene el conjunto completo de proyectos, tareas, laboratorios y ejercicios desarrollados durante la carrera de Ingeniería en Computación en el Instituto Tecnológico de Costa Rica (TEC). Documenta el progreso desde fundamentos de programación hasta tópicos avanzados: algoritmos, bases de datos relacionales y NoSQL, contenerización y especificación de sistemas.

## 🎯 Propósito

Este repositorio sirve como:
- **Portfolio académico** de proyectos y trabajos realizados
- **Referencia de código** para revisión y mejora continua
- **Registro del progreso** a través de diferentes semestres y materias
- **Base de conocimiento** para futuras referencias

## 📁 Estructura del Proyecto

```
TEC/
├── I SEMESTRE/                          # Fundamentos de Programación
│   ├── Introduccion a la Programacion/  # Python: lógica, control de flujo, funciones
│   │   ├── Examenes/                    # Evaluaciones realizadas
│   │   ├── IntroTallerTrabajos/         # Ejercicios de talleres
│   │   ├── PracticaExamenes/            # Preparación para exámenes
│   │   └── Tareas/                      # Tareas semanales (T1-T7)
│   └── Taller de Programacion/          # Proyectos prácticos en Python
│       ├── Labs/                        # Archivos, diccionarios, listas, matrices, OO, etc.
│       ├── TP#1/                        # Trabajo Práctico 1
│       ├── TP#2/                        # Trabajo Práctico 2
│       └── TP#3/                        # Trabajo Práctico 3
│
├── II SEMESTRE/                         # Programación Avanzada
│   ├── Arqui/                           # Ensamblador x86
│   │   ├── mcm2025.asm                  # Máximo común múltiplo
│   │   ├── ProductoInterno.asm          # Operaciones vectoriales
│   │   └── Proyectos (1-3)/             # Proyectos integrados
│   ├── Estructuras de Datos/            # C: ABB, listas, punteros, structs, memoria dinámica
│   │   ├── Clases/                      # Material de clase
│   │   ├── Proyecto (1-3)/              # Proyectos principales
│   │   ├── ProyectosC/                  # Ejercicios: bucles, funciones, punteros, structs
│   │   └── Tareas/                      # Tareas T2, T3, T5, T6
│   └── POO/                             # Java + Swing, XML/DOM, UML
│       ├── Fundamentos_Java/            # Conceptos básicos de Java
│       ├── Proyecto1-2/                 # Proyectos principales
│       ├── PES, TCS, TIS, TPS/          # Actividades y ejercicios
│       └── HolaSwing, EjemploDOM/       # Interfaces gráficas
│
├── III_SEMESTRE/                        # Algoritmos, Datos y Requisitos
│   ├── Analisis/                        # Análisis de Algoritmos (ADA) en Maxima (.mac)
│   │   ├── Tareas/Tarea1-Tarea10/       # Búsqueda, ordenamiento, greedy, grafos/DFS,
│   │   │                               # DP-Knapsack, TSP, KNN, pruebas de límites
│   │   └── Tranbajo en Clase/           # Búsqueda, Estructuras, Grafos, Greedy,
│   │                                    # Ordenamiento (Bubble/Merge/Quick/Selection), etc.
│   ├── BasesDeDatos/                    # BD relacionales: SQL + Node.js
│   │   ├── Tarea_1, Tarea_2/            # Apps Node (src/, public/) + análisis de resultados
│   │   ├── TareaEscrita/                # Stored procedures (SPTarea.sql, SPTarea_v2.sql)
│   │   └── Trabajos en Clase/           # Ejercicios SQL (ClaseVacaciones)
│   └── Requeriminetos/                  # Ingeniería de Requisitos (nota: typo en carpeta)
│       ├── Tareas/Tarea1-Tarea4/        # SafeWalk, Geo-beats, app Java (diagramas de clases,
│       │                               # HU), especificaciones PDF
│       ├── Proyectos/                   # Proyecto 2 + UI
│       └── Trabajo en clase/            # Caso "El buen café": casos de uso, diagramas
│                                        # de actividad/contexto/paquetes, historias de
│                                        # usuario, prototipo Cajero.pen
│
├── IV SEMESTRE/                         # Bases de Datos II (IC-4302) — en curso
│   └── BasesDeDatosII/
│       ├── Guia Redis/                  # Práctica Redis: Strings, Listas, Sets, Hashes,
│       │                               # Sorted Sets, EXPIRE/TTL/FLUSHDB + capturas
│       │                               # RedisInsight (PracticaRedis.md/.pdf)
│       └── Trabajo en clase/
│           ├── DockerRestAPI/           # API REST Flask contenerizada (app.py,
│           │                           # Dockerfile, requirements.txt, pyproject.toml)
│           └── MongoDB01/               # PyMongo: upserts, índices, find_one con
│                                        # proyección, aggregate $match/$project,
│                                        # $exists (ejemplo_mongo.py, main.py)
│
├── V SEMESTRE/                          # (reservado — carpeta vacía)
├── VI SEMESTRE/                         # (reservado — carpeta vacía)
├── VII SEMESTRE/                        # (reservado — carpeta vacía)
└── VIII SEMESTRE/                       # (reservado — carpeta vacía)
```

> **Nota:** la carpeta de requisitos se llama literalmente `Requeriminetos/` en disco. Se respeta ese nombre en el árbol para que las rutas coincidan.

## 💻 Tecnologías y Lenguajes

### I Semestre
- **Python 3.x** — lógica estructurada, control de flujo, funciones, POO básica, archivos

### II Semestre
- **Ensamblador x86 (NASM)** — programación de bajo nivel
- **C (GCC)** — estructuras de datos, punteros, memoria dinámica
- **Java (JDK 8+) + Swing** — POO, patrones, interfaces gráficas
- **XML/DOM, UML** — procesamiento de documentos y modelado

### III Semestre
- **Maxima CAS (.mac)** — análisis y prueba de algoritmos: búsqueda (lineal/binaria), ordenamiento (Bubble/Merge/Quick/Selection), greedy (Interval Scheduling, Knapsack, TFS), grafos/DFS, DP (Knapsack), TSP, KNN
- **SQL + Stored Procedures** — diseño relacional, SPTarea.sql
- **Node.js + Express (src/, public/)** — Tareas 1 y 2 de BD
- **Ingeniería de Requisitos** — casos de uso, historias de usuario, diagramas de actividad/contexto/paquetes/clases, prototipado (Pencil `.pen`)

### IV Semestre (en curso — Bases de Datos II, IC-4302)
- **Redis** — Strings (APPEND/GET/STRLEN/MSET/MGET), Listas (LRANGE/LPOP/RPOP/LLEN), Sets (SISMEMBER/SREM/SMEMBERS/SCARD), Hashes (HKEYS/HVALS/HDEL/HLEN/HGETALL), Sorted Sets (ZRANK/ZSCORE/ZCARD/ZREVRANGE), administración (EXPIRE/TTL/FLUSHDB/KEYS), RedisInsight
- **MongoDB + PyMongo** — upserts, índices, proyecciones (`_id: 0`), agregaciones (`$match`/`$project`), `$exists`
- **Docker + Flask + uv** — contenerización de API REST (`python:3.12-alpine`, puerto 3000/3001)

## 🚀 Cómo Usar este Repositorio

### Navegación recomendada

1. **Por semestre**: cada carpeta contiene las materias de ese período
2. **Por materia**: cada materia agrupa trabajos, laboratorios y proyectos
3. **Por tipo de trabajo**:
   - `Tareas/` — trabajos cortos individuales
   - `Labs/` / `Tranbajo en Clase/` / `Trabajo en clase/` — práctica guiada
   - `Proyecto#/` / `Proyectos/` — proyectos integrales
   - `Examenes/` — evaluaciones
   - `Guia Redis/` — práctica documentada con capturas

### Ejecutar código

#### Python (I Semestre, IV Semestre)
```bash
python archivo.py
```

#### C (II Semestre — Estructuras de Datos)
```bash
gcc -o salida archivo.c
./salida
```

#### Java (II Semestre — POO, III Semestre — Requisitos Tarea4)
```bash
javac archivo.java
java ClassName
```

#### Ensamblador (II Semestre — Arqui)
```bash
nasm -f win32 archivo.asm -o archivo.obj
# o utilizar NASM / emulador x86
```

#### Maxima (III Semestre — Análisis/ADA)
```bash
# Por lotes (Windows, ver SKILLS maxima-windows si aplica):
maxima -b Tarea7.mac
# Interactivo:
maxima
```

#### Redis (IV Semestre — Guia Redis)
```bash
redis-cli
# Ejemplos de la práctica:
# GET nombre_curso / LRANGE motores_db 0 -1 / SMEMBERS temas_curso
# HGETALL estudiante:101 / ZREVRANGE ranking_proyectos 0 -1 WITHSCORES
# TTL temas_curso / FLUSHDB
```

#### MongoDB + PyMongo (IV Semestre — MongoDB01)
```bash
# Requiere MongoDB en 127.0.0.1:27017 (o docker run mongo)
pip install pymongo
python ejemplo_mongo.py
```

#### Docker + Flask (IV Semestre — DockerRestAPI)
```bash
cd "IV SEMESTRE/BasesDeDatosII/Trabajo en clase/DockerRestAPI"
docker build -t flask-api .
docker run -p 3000:3000 flask-api
# GET http://localhost:3000/ , GET /task , POST /task , DELETE /task/<id>
```

#### Node.js (III Semestre — BasesDeDatos Tarea_1/Tarea_2)
```bash
cd III_SEMESTRE/BasesDeDatos/Tarea_1/Tarea1
npm install
npm start
```

## 📊 Estadísticas del Repositorio

| Semestre | Materias | Lenguajes / Stack | Contenido destacado |
|----------|----------|-------------------|---------------------|
| I | 2 | Python | 3+ TPs, T1–T7, labs |
| II | 3 | Asm, C, Java | 9+ proyectos (Arqui, ED, POO) |
| III | 3 | Maxima, SQL, Node.js, UML | ADA T1–T10, SPs SQL, SafeWalk/Geo-beats, El buen café |
| IV (en curso) | 1 | Redis, MongoDB, Docker+Flask | Guía Redis + capturas, MongoDB01, DockerRestAPI |
| V–VIII | — | — | Carpetas reservadas (vacías) |

## 🎓 Materias Principales

### I Semestre
- **Introducción a la Programación**: lógica, control de flujo, estructuras básicas
- **Taller de Programación**: aplicación práctica en proyectos

### II Semestre
- **Arquitectura de Computadores**: ensamblador, operaciones de bajo nivel
- **Estructuras de Datos**: árboles, listas, memoria dinámica en C
- **Programación Orientada a Objetos**: diseño OO, patrones, Swing

### III Semestre
- **Análisis de Algoritmos (ADA)**: complejidad, búsqueda, ordenamiento, greedy, grafos, DP, TSP, KNN — implementado y probado en Maxima
- **Bases de Datos I**: modelado relacional, SQL, stored procedures, apps Node
- **Ingeniería de Requisitos**: especificación, casos de uso, historias de usuario, prototipos

### IV Semestre (en curso)
- **Bases de Datos II (IC-4302)**: Redis (estructuras + administración), MongoDB (documentos, agregaciones), Docker + Flask (API REST contenerizada)

## 📝 Convenciones del Repositorio

- **Nombres de archivos**: descriptivos, en inglés/español según contexto educativo
- **Estructura**: semestre → materia → tipo de trabajo
- **Comentarios**: en español para claridad académica
- **Documentación**: cada proyecto principal incluye docs propias (SPEC.md, PLAN.md, análisis, PDFs, capturas)
- **Casos especiales**: se conserva el nombre real `Requeriminetos/` y `Tranbajo en Clase/` aunque tengan typos, para no romper rutas

## 🔍 Encontrar Contenido Específico

```bash
# Python del I semestre
grep -r "patron" --include="*.py" "I SEMESTRE/"

# C de estructuras
grep -r "struct" --include="*.c" "II SEMESTRE/Estructuras de Datos/"

# Java / POO
grep -r "class " --include="*.java" "II SEMESTRE/POO/"

# Algoritmos en Maxima (III semestre)
grep -r "defun" --include="*.mac" "III_SEMESTRE/Analisis/"

# Práctica Redis / Mongo / Docker (IV semestre)
grep -r "ZRANGE\|HGETALL\|SISMEMBER" "IV SEMESTRE/BasesDeDatosII/Guia Redis/"
grep -r "aggregate\|find_one" --include="*.py" "IV SEMESTRE/BasesDeDatosII/Trabajo en clase/MongoDB01/"
```

## 📋 Requisitos Previos

- **Python 3.10+** (3.12 para DockerRestAPI) — I y IV semestre
- **GCC** — C (II semestre)
- **Java JDK 8+** — POO y Requisitos/Tarea4
- **NASM** — ensamblador (II semestre)
- **Maxima** — scripts `.mac` (III semestre, Análisis)
- **Node.js + npm/pnpm** — Tarea_1/Tarea_2 de BD (III semestre)
- **Redis + RedisInsight** (o `redis-cli`) — Guía Redis (IV semestre)
- **MongoDB 6+** + `pymongo` — MongoDB01 (IV semestre)
- **Docker** — DockerRestAPI (IV semestre)
- **Git** — clonar y gestionar el repo

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/MatiasBS027/TEC.git

# Navegar al directorio
cd TEC

# Ver la estructura (Windows)
dir /s
# (Linux/macOS)
tree
```

## 📈 Evolución del Aprendizaje

- ✅ **Conceptos básicos** (I Semestre): variables, control de flujo, funciones
- ✅ **Estructuras avanzadas** (II Semestre): punteros, memoria, OOP
- ✅ **Análisis y sistemas** (III Semestre): algoritmos con Maxima, BD relacionales, requisitos y prototipado
- 🔄 **Datos modernos y despliegue** (IV Semestre, en curso): Redis, MongoDB, Docker + Flask
- ⬜ **Próximos semestres** (V–VIII): carpetas reservadas

## 📚 Recursos Educativos

Cada carpeta de proyecto puede incluir:
- Código fuente comentado
- Documentación técnica (SPEC.md, PLAN.md, análisis)
- Diagramas UML / capturas (RedisInsight, Pencil)
- Reportes y análisis de resultados (.pdf, .docx, .md)
- Ejemplos de ejecución

## ⚖️ Licencia

Este repositorio está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

Para preguntas o sugerencias sobre el contenido académico:
- **GitHub**: [MatiasBS027](https://github.com/MatiasBS027)

## 🤝 Contribuciones

Este es un repositorio educativo personal. Las contribuciones externas no son esperadas, pero se aprecian sugerencias para mejora de código o documentación.

## 📌 Notas Importantes

- Este repositorio es de **naturaleza educativa** y refleja el trabajo académico
- El código ha evolucionado con el aprendizaje — versiones anteriores pueden no representar las mejores prácticas actuales
- Se actualiza regularmente con nuevos proyectos y trabajos

---

**Última actualización**: Octubre 2026
**Estado**: En desarrollo continuo
**Progreso**: III semestres completados + IV semestre en curso (Bases de Datos II)
