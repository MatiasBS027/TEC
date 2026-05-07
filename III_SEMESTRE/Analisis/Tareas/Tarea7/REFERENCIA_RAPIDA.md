# REFERENCIA RÁPIDA - RESULTADOS DE PRUEBAS

## Ejecución de Pruebas

### Suite 1: Pruebas Funcionales

  bash
& "C:\Software\Maxima\maxima-5.49.0\bin\maxima.bat" -q -b "pruebas_tarea7.mac"
  
**Estado**: ✅ EXITOSO (Exit Code: 0)

**Pruebas**: 4/4 funciones pasadas
  
✓ vecinos: 3 pruebas pasadas
✓ extender: 3 pruebas pasadas  
✓ prof: 3 pruebas pasadas
✓ profTodas: 2 pruebas pasadas
  
**Puntuación**: 100/100 pts

---

### Suite 2: Pruebas Límite y Especiales

  bash
& "C:\Software\Maxima\maxima-5.49.0\bin\maxima.bat" -q -b "pruebas_limites.mac"
  
**Estado**: ✅ EXITOSO (Exit Code: 0)

**Pruebas Ejecutadas**: 28/28 pasadas
  
✓ Listas vacías: 7/7
✓ Valores límite: 8/8
✓ Números negativos: 3/3
✓ Rutas parciales: 4/4
✓ Conflictos específicos: 6/6

**Conclusión**: Robusto ante casos extremos

---

## Casos Clave Validados

### Casos de Éxito ✓

| Caso | Entrada | Salida | Validación |
| n=1 | `prof(1)` | `[[1,1]]` | ✓ Correcto |
| n=4 Una | `prof(4)` | `[[1,2],[2,4],[3,1],[4,3]]` | ✓ Válida |
| n=4 Todas | `profTodas(4)` | 2 soluciones | ✓ Completa |
| n=5 Una | `prof(5)` | `[[1,1],[2,3],[3,5],[4,2],[5,4]]` | ✓ Válida |
| n=5 Todas | `profTodas(5)` | 10 soluciones | ✓ Completa |

### Casos sin Solución ✓

| Caso | Entrada | Salida | Validación |
| n=0 | `prof(0)` | `[]` | ✓ Correcto |
| n=2 | `profTodas(2)` | `[]` | ✓ Correcto |
| n=3 | `profTodas(3)` | `[]` | ✓ Correcto |

### Casos de Listas Vacías ✓

| Caso | Entrada | Salida | Validación |
| conflicto vacío | `conflicto([1,1],[])` | `false` | ✓ Correcto |
| vecinos vacío | `vecinos(4,[])` | `[]` | ✓ Correcto |
| extender vacío | `extender(4,[])` | `[]` | ✓ Correcto |

---

## Detección de Conflictos ✓

Todos los tipos de conflicto detectados correctamente:

| Tipo | Ejemplo | Resultado |
| Columna | `[2,1]` vs `[1,1]` | Conflicto ✓ |
| Diagonal | `[2,2]` vs `[1,1]` | Conflicto ✓ |
| Diagonal | `[3,3]` vs `[1,1]` | Conflicto ✓ |
| Sin conflicto | `[2,3]` vs `[1,1]` | Válido ✓ |

---

## Soluciones Verificadas

### n=4: 2 soluciones

Solución 1: [1,2] [2,4] [3,1] [4,3]
Solución 2: [1,3] [2,1] [3,4] [4,2]

**Validación**: Ambas sin conflictos ✓

### n=5: 10 soluciones

Primera: [1,1] [2,3] [3,5] [4,2] [5,4]
...
Total: 10 soluciones completas

**Validación**: Cantidad correcta (teórica) ✓

---

## Puntuación Final

╔═══════════════════════════════════════╗
║     CALIFICACIÓN - TAREA 7            ║
╠═══════════════════════════════════════╣
║ vecinos................ 10/10 ✓      ║
║ extender.............. 30/30 ✓      ║
║ prof.................. 30/30 ✓      ║
║ profTodas............. 30/30 ✓      ║
║                                       ║
║ TOTAL................. 100/100 ✓     ║
╚═══════════════════════════════════════╝

---

## Archivos Disponibles

- **Tarea7.mac** - Código fuente del programa
- **pruebas_tarea7.mac** - Suite de pruebas funcionales
- **pruebas_limites.mac** - Suite de pruebas de límite
- **RESULTADOS_PRUEBAS.md** - Reporte funcional detallado
- **PRUEBAS_LIMITES_RESULTADOS.md** - Reporte de límites detallado
- **RESUMEN_GENERAL_PRUEBAS.md** - Resumen ejecutivo completo
- **REFERENCIA_RAPIDA.md** - Este archivo

---

## Nota Final

✅ Todas las pruebas ejecutadas exitosamente  
✅ 100% de pruebas pasadas  
✅ Resultados verificados contra teoría matemática  
✅ Código robusto ante casos especiales

**El programa está listo para entrega.**
