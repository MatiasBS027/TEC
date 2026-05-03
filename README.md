# TEC - Repositorio de Carrera Académica

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Repository Size](https://img.shields.io/github/repo-size/MatiasBS027/TEC)
![Last Update](https://img.shields.io/github/last-commit/MatiasBS027/TEC)

## 📚 Descripción

Repositorio educativo que contiene el conjunto completo de proyectos, tareas, laboratorios y ejercicios desarrollados durante la carrera académica en el Instituto Tecnológico de Costa Rica (TEC). Este repositorio documenta el progreso desde conceptos fundamentales de programación hasta tópicos avanzados en ingeniería de software.

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
│   ├── Introduccion a la Programacion/   # Conceptos básicos de Python
│   │   ├── Examenes/                     # Evaluaciones realizadas
│   │   ├── IntroTallerTrabajos/          # Ejercicios de talleres
│   │   ├── PracticaExamenes/             # Preparación para exámenes
│   │   └── Tareas/                       # Tareas semanales (T1-T7)
│   │
│   └── Taller de Programacion/           # Proyectos prácticos
│       ├── Labs/                         # Laboratorios: Archivos, Diccionarios, Listas, Matrices, OO, etc.
│       ├── TP#1/                         # Trabajo Práctico 1
│       ├── TP#2/                         # Trabajo Práctico 2
│       └── TP#3/                         # Trabajo Práctico 3
│
├── II SEMESTRE/                         # Programación Avanzada
│   ├── Arqui/                            # Programación en Ensamblador (x86)
│   │   ├── mcm2025.asm                   # Máximo común múltiplo
│   │   ├── ProductoInterno.asm           # Operaciones vectoriales
│   │   └── Proyectos (1-3)/              # Proyectos integrados
│   │
│   ├── Estructuras de Datos/             # Programación en C
│   │   ├── Clases/                       # Materiales de clase
│   │   ├── Proyecto (1-3)/               # Proyectos principales
│   │   ├── ProyectosC/                   # Ejercicios: ABB, bucles, funciones, punteros, structs
│   │   └── Tareas/                       # Tareas T2, T3, T5, T6
│   │
│   └── POO/                              # Programación Orientada a Objetos (Java & Swing)
│       ├── Fundamentos_Java/             # Conceptos básicos de Java
│       ├── Proyecto1-2/                  # Proyectos principales
│       ├── PES, TCS, TIS, TPS/           # Actividades y ejercicios
│       └── HolaSwing, EjemploDOM/        # Interfaces gráficas
│
└── III SEMESTRE/                        # Formación Integral
    ├── Analisis/                         # Análisis y Evaluación
    ├── BasesDeDatos/                     # Diseño y gestión de BDD
    └── Requerimientos/                   # Especificación de sistemas
```

## 💻 Tecnologías y Lenguajes

### I Semestre
- **Python 3.x** - Introducción a la programación, lógica estructurada
- **Conceptos**: Variables, estructuras de control, funciones, POO básica, manejo de archivos

### II Semestre
- **Ensamblador x86** - Programación de bajo nivel
- **C** - Estructuras de datos, punteros, memoria dinámica
- **Java** - Programación orientada a objetos, interfaces gráficas (Swing)
- **XML/DOM** - Procesamiento de documentos
- **UML** - Diagramas de arquitectura

### III Semestre
- **SQL** - Diseño y consultas de bases de datos
- **Análisis de Sistemas** - Modelado y especificación
- **Ingeniería de Requisitos**

## 🚀 Cómo Usar este Repositorio

### Navegación Recomendada

1. **Por Semestre**: Cada carpeta de semestre contiene las materias cursadas en ese período
2. **Por Materia**: Cada materia agrupa todos los trabajos, laboratorios y proyectos
3. **Por Tipo de Trabajo**:
   - `Tareas/` - Trabajos cortos individuales
   - `Labs/` - Laboratorios prácticos
   - `Proyecto#/` - Proyectos integrales
   - `Examenes/` - Evaluaciones

### Ejecutar Código

#### Python (I Semestre)
```bash
python archivo.py
```

#### C (II Semestre - Estructuras de Datos)
```bash
gcc -o salida archivo.c
./salida
```

#### Java (II Semestre - POO)
```bash
javac archivo.java
java ClassName
```

#### Ensamblador (II Semestre - Arqui)
```bash
nasm -f win32 archivo.asm -o archivo.obj
# o utilizar un entorno IDE como NASM o x86 Emulator
```

## 📊 Estadísticas del Repositorio

| Semestre | Materias | Lenguajes | Proyectos |
|----------|----------|-----------|-----------|
| I        | 2        | Python    | 3+ TPs    |
| II       | 3        | Asm, C, Java | 9+ Proyectos |
| III      | 3        | SQL, UML  | En progreso |

## 🎓 Materias Principales

### I Semestre
- **Introducción a la Programación**: Fundamentos de lógica, control de flujo, estructuras de datos básicas
- **Taller de Programación**: Aplicación práctica de conceptos en proyectos reales

### II Semestre
- **Arquitectura de Computadoras**: Programación en ensamblador, operaciones de bajo nivel
- **Estructuras de Datos**: Implementación de árboles, listas, operaciones en memoria
- **Programación Orientada a Objetos**: Diseño OO, patrones, interfaces gráficas

### III Semestre
- **Análisis de Sistemas**: Evaluación y mejora de procesos
- **Bases de Datos**: Diseño relacional, consultas SQL
- **Ingeniería de Requisitos**: Especificación y análisis de necesidades

## 📝 Convenciones del Repositorio

- **Nombres de archivos**: Descriptivos y en inglés/español según contexto educativo
- **Estructura de directorios**: Organizada por semestre → materia → tipo de trabajo
- **Comentarios en código**: Incluidos en español para claridad académica
- **Documentación**: Cada proyecto principal incluye documentación específica

## 🔍 Encontrar Contenido Específico

Para buscar un tema o concepto:

```bash
# Buscar archivos que contengan un patrón
grep -r "patrón" --include="*.py" I\ SEMESTRE/

# Buscar en estructuras de datos
grep -r "struct" --include="*.c" II\ SEMESTRE/Estructuras\ de\ Datos/

# Buscar clases Java
grep -r "class " --include="*.java" II\ SEMESTRE/POO/
```

## 📋 Requisitos Previos

Para utilizar este repositorio necesitarás:

- **Python 3.6+** - Para código del I semestre
- **GCC** - Compilador C para II semestre
- **Java JDK 8+** - Para proyectos POO
- **NASM o similar** - Para código en ensamblador
- **Git** - Para clonar y gestionar el repositorio

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/MatiasBS027/TEC.git

# Navegar al directorio
cd TEC

# Ver la estructura
tree    # En Windows: dir /s
```

## 📈 Evolución del Aprendizaje

Este repositorio documenta la progresión desde:
- ✅ **Conceptos básicos** (I Semestre): Variables, control de flujo, funciones
- ✅ **Estructuras avanzadas** (II Semestre): Punteros, memoria, OOP
- 🔄 **Sistemas complejos** (III Semestre): Bases de datos, análisis integral

## 📚 Recursos Educativos

Cada carpeta de proyecto puede incluir:
- Código fuente comentado
- Documentación técnica
- Diagramas UML
- Reportes y análisis
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
- El código ha evolucionado con el aprendizaje - versiones anteriores pueden no representar las mejores prácticas actuales
- Se actualiza regularmente con nuevos proyectos y trabajos

---

**Última actualización**: Mayo 2026  
**Estado**: En desarrollo continuo  
**Progreso**: 3 semestres completados

