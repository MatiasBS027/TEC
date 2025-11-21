/*  
Proyecto2.c
Sistema de ordenamiento de artículos científicos
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stddef.h>

/*
Colores para el menu e interaccion con el usuario
Mediante secuencias de escape ANSI
Más info en: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 
*/
#define RESET   "\033[0m"
#define CYANB   "\033[36;1;3m"
#define YELLOW  "\033[33;3m"
#define WHITEB  "\033[97m"
#define GREENB  "\033[32;1;3m"
#define REDB    "\033[91;1;3m"
#define BLUEB   "\033[94;1;3m"

//######################################################
//          ESTRUCTURAS
//######################################################

struct Articulo {
    char nombre_autor[21];     // 20 + 1 para '\0'
    char apellido_autor[21];   // 20 + 1 para '\0'
    char titulo[501];           // 50 + 1 para '\0'
    char ruta[61];             // 60 + 1 para '\0'
    char anio[11];             // 10 + 1 para '\0'
    char abstract[1001];        // 100 + 1 para '\0'
};

struct MonitculoArticulos {
    struct Articulo** elementos;  // Array de punteros a artículos
    int tamanio;
    int capacidad;
    int tipo_ordenamiento;  // 1 = por año, 2 = por tamaño título
};

//######################################################
//          FUNCIONES AUXILIARES
//######################################################

/* 
Eliminar espacios en blanco al final de una cadena
E: cadena de texto
S: void (modifica la cadena directamente)
*/
void limpiar_espacios_final(char* cadena) {
    int longitud = strlen(cadena);
    
    // Retroceder desde el final eliminando espacios
    char* ptr = cadena;
    for (int i = 0; i < longitud; i++) {
        ptr++;
    }
    
    ptr--; // Volver al último carácter
    
    while (ptr >= cadena && (*ptr == ' ' || *ptr == '\n' || *ptr == '\r')) {
        *ptr = '\0';
        ptr--;
    }
}

/* 
Contar cantidad de palabras en una cadena
E: cadena de texto
S: cantidad de palabras
*/
int contar_palabras(const char* texto) {
    if (!texto) return 0;
    
    int palabras = 0;
    bool en_palabra = false;
    
    const char* ptr = texto;
    while (*ptr != '\0') {
        if (*ptr == ' ' || *ptr == '\t' || *ptr == '\n') {
            en_palabra = false;
        } else if (!en_palabra) {
            en_palabra = true;
            palabras++;
        }
        ptr++;
    }
    
    return palabras;
}

/* 
Comparar dos artículos según el tipo de ordenamiento
E: artículo1, artículo2, tipo (1=año, 2=tamaño título)
S: true si art1 < art2 (para min-heap)
*/
bool comparar_articulos(struct Articulo* art1, struct Articulo* art2, int tipo) {
    if (!art1 || !art2) return false;
    
    switch (tipo) {

        case 1: {
            // Ordenar por año del más viejo al más nuevo (convertir string a int)
            int anio1 = atoi(art1->anio);
            int anio2 = atoi(art2->anio);
            return anio1 < anio2;
        }

        case 2: {
            // Ordenar por año del más nuevo al más viejo (convertir string a int)
            int anio1 = atoi(art1->anio);
            int anio2 = atoi(art2->anio);
            return anio1 > anio2;
        }

        case 3: {
            // Ordenar por tamaño del título en palabras, de menos a más
            int palabras1 = contar_palabras(art1->titulo);
            int palabras2 = contar_palabras(art2->titulo);
            return palabras1 < palabras2;
        }

        case 4: {
            // Ordenar por tamaño del título en palabras, de más a menos
            int palabras1 = contar_palabras(art1->titulo);
            int palabras2 = contar_palabras(art2->titulo);
            return palabras1 > palabras2;
        }

        case 5: {
            // Comparar títulos alfabéticamente ascendente
            // strcmp < 0 → art1 va antes
            int orden = strcmp(art1->titulo, art2->titulo);
            return orden < 0;
        }

        case 6: {
            // Comparar títulos alfabéticamente descendente
            // strcmp > 0 → art1 va antes
            int orden = strcmp(art1->titulo, art2->titulo);
            return orden > 0;
        }

        case 7: {
            // Comparar rutas alfabéticamente ascendente
            // strcmp < 0 → art1 va antes
            int orden = strcmp(art1->ruta, art2->ruta);
            return orden < 0;
        }

        case 8: {
            // Comparar rutas alfabéticamente descendente
            // strcmp > 0 → art1 va antes
            int orden = strcmp(art1->ruta, art2->ruta);
            return orden > 0;
        }

        case 9: {
            // Comparar nombres de autor ascendente
            // strcmp < 0 → art1 va antes
            int orden = strcmp(art1->nombre_autor, art2->nombre_autor);
            return orden < 0;
        }

        case 10: {
            // Comparar nombres de autor descendente
            // strcmp > 0 → art1 va antes
            int orden = strcmp(art1->nombre_autor, art2->nombre_autor);
            return orden > 0;
        }

        case 11: {
            // Comparar apellidos de autor ascendente
            // strcmp < 0 → art1 va antes
            int orden = strcmp(art1->apellido_autor, art2->apellido_autor);
            return orden < 0;
        }

        case 12: {
            // Comparar apellidos de autor descendente
            // strcmp > 0 → art1 va antes
            int orden = strcmp(art1->apellido_autor, art2->apellido_autor);
            return orden > 0;
        }

        default:
            // Tipo inválido → no se altera el orden
            return false;
    }
}

//######################################################
//          FUNCIONES PARA LEER ARTÍCULOS
//######################################################

/* 
Leer una línea y crear un struct Articulo
E: línea de texto del archivo
S: puntero a struct Articulo con los datos
*/
struct Articulo* leer_articulo_desde_linea(char* linea) {
    if (!linea) return NULL;
    
    // Crear el artículo
    struct Articulo* nuevo = calloc(1, sizeof(struct Articulo));
    if (!nuevo) return NULL;
    
    // Extraer los 6 campos con strtok
    char* nombre = strtok(linea, "|");
    char* apellido = strtok(NULL, "|");
    char* titulo = strtok(NULL, "|");
    char* ruta = strtok(NULL, "|");
    char* anio = strtok(NULL, "|");
    char* abstract = strtok(NULL, "|");
    
    // Verificar que todos los campos existan
    if (!nombre || !apellido || !titulo || !ruta || !anio || !abstract) {
        free(nuevo);
        return NULL;
    }
    
    // Copiar a la estructura (strncpy para seguridad)
    strncpy(nuevo->nombre_autor, nombre, 20);
    nuevo->nombre_autor[20] = '\0';
    
    strncpy(nuevo->apellido_autor, apellido, 20);
    nuevo->apellido_autor[20] = '\0';
    
    strncpy(nuevo->titulo, titulo, 50);
    nuevo->titulo[500] = '\0';
    
    strncpy(nuevo->ruta, ruta, 60);
    nuevo->ruta[60] = '\0';
    
    strncpy(nuevo->anio, anio, 10);
    nuevo->anio[10] = '\0';
    
    strncpy(nuevo->abstract, abstract, 100);
    nuevo->abstract[1000] = '\0';
    
    // Limpiar espacios al final de cada campo
    limpiar_espacios_final(nuevo->nombre_autor);
    limpiar_espacios_final(nuevo->apellido_autor);
    limpiar_espacios_final(nuevo->titulo);
    limpiar_espacios_final(nuevo->ruta);
    limpiar_espacios_final(nuevo->anio);
    limpiar_espacios_final(nuevo->abstract);
    
    return nuevo;
}

/* 
Leer todos los artículos del archivo
E: nombre del archivo (ruta), puntero para guardar cantidad
S: array de punteros a struct Articulo
*/
struct Articulo** leer_articulos_desde_archivo(const char* nombre_archivo, int* cantidad) {
    FILE* archivo = fopen(nombre_archivo, "r");
    if (!archivo) {
        printf("Error al abrir el archivo: %s\n", nombre_archivo);
        return NULL;
    }
    
    // Contar cuántas líneas tiene el archivo (cuántos artículos)
    int total_articulos = 0;
    char linea_temp[500];
    while (fgets(linea_temp, sizeof(linea_temp), archivo)) {
        total_articulos++;
    }
    
    // Volver al inicio del archivo
    rewind(archivo);
    
    // Crear array de punteros (uno extra para NULL al final)
    struct Articulo** articulos = calloc(total_articulos + 1, sizeof(struct Articulo*));
    if (!articulos) {
        fclose(archivo);
        return NULL;
    }
    
    // Leer cada línea y crear artículos
    int indice = 0;
    char linea[500];
    while (fgets(linea, sizeof(linea), archivo) && indice < total_articulos) {
        struct Articulo* art = leer_articulo_desde_linea(linea);
        if (art) {
            struct Articulo** ptr = articulos;
            for (int i = 0; i < indice; i++) {
                ptr++;
            }
            *ptr = art;
            indice++;
        }
    }
    
    // Guardar la cantidad de artículos leídos
    *cantidad = indice;
    
    fclose(archivo);
    return articulos;
}

/* 
Liberar memoria de array de artículos
E: array de artículos, cantidad
S: void
*/
void liberar_articulos(struct Articulo** articulos, int cantidad) {
    if (!articulos) return;
    
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad; i++) {
        if (*ptr) {
            free(*ptr);
        }
        ptr++;
    }
    
    free(articulos);
}

//######################################################
//          FUNCIONES DE HEAP - NAVEGACIÓN
//######################################################

// Obtener índice del padre: (indice - 1) / 2
int obtener_padre(int indice) {
    return (indice - 1) / 2;
}

// Obtener índice del hijo izquierdo: 2 * indice + 1
int obtener_hijo_izquierdo(int indice) {
    return 2 * indice + 1;
}

// Obtener índice del hijo derecho: 2 * indice + 2
int obtener_hijo_derecho(int indice) {
    return 2 * indice + 2;
}

//######################################################
//          HEAP PARA ARTÍCULOS
//######################################################

/* 
Crear un nuevo montículo para artículos
E: capacidad inicial, tipo de ordenamiento (1=año, 2=tamaño título)
S: puntero al montículo creado
*/
struct MonitculoArticulos* crear_monticulo_articulos(int capacidad, int tipo_ordenamiento) {
    struct MonitculoArticulos* nuevo = calloc(1, sizeof(struct MonitculoArticulos));
    if (!nuevo) return NULL;
    
    nuevo->elementos = calloc(capacidad, sizeof(struct Articulo*));
    if (!nuevo->elementos) {
        free(nuevo);
        return NULL;
    }
    
    nuevo->tamanio = 0;
    nuevo->capacidad = capacidad;
    nuevo->tipo_ordenamiento = tipo_ordenamiento;
    
    return nuevo;
}

/* 
Insertar un artículo en el montículo
E: puntero al montículo, puntero al artículo
S: true si se insertó correctamente, false si está lleno
*/
bool insertar_articulo(struct MonitculoArticulos* monticulo, struct Articulo* articulo) {
    if (!monticulo || !articulo) return false;
    
    // Verificar si hay espacio
    if (monticulo->tamanio >= monticulo->capacidad) {
        printf("Monticulo lleno\n");
        return false;
    }
    
    // Insertar al final del array
    int indice = monticulo->tamanio;
    struct Articulo** ptr_nuevo = monticulo->elementos;
    for (int i = 0; i < indice; i++) {
        ptr_nuevo++;
    }
    *ptr_nuevo = articulo;
    monticulo->tamanio++;
    
    // Bubble up: subir el elemento hasta su posición correcta
    while (indice > 0) {
        int indice_padre = obtener_padre(indice);
        
        // Obtener punteros a artículos
        struct Articulo** ptr_actual = monticulo->elementos;
        for (int i = 0; i < indice; i++) {
            ptr_actual++;
        }
        
        struct Articulo** ptr_padre = monticulo->elementos;
        for (int i = 0; i < indice_padre; i++) {
            ptr_padre++;
        }
        
        // Comparar según el tipo de ordenamiento
        if (!comparar_articulos(*ptr_actual, *ptr_padre, monticulo->tipo_ordenamiento)) {
            break; // Ya está en posición correcta
        }
        
        // Intercambiar
        struct Articulo* temp = *ptr_actual;
        *ptr_actual = *ptr_padre;
        *ptr_padre = temp;
        
        indice = indice_padre;
    }
    
    return true;
}

/* 
Extraer el mínimo del heap (artículo con menor valor según criterio)
E: puntero al montículo
S: puntero al artículo extraído
*/
struct Articulo* extraer_minimo(struct MonitculoArticulos* monticulo) {
    if (!monticulo || monticulo->tamanio == 0) return NULL;
    
    // Guardar el mínimo (raíz)
    struct Articulo* minimo = *monticulo->elementos;
    
    // Mover el último elemento a la raíz
    monticulo->tamanio--;
    
    if (monticulo->tamanio > 0) {
        struct Articulo** ptr_ultimo = monticulo->elementos;
        for (int i = 0; i < monticulo->tamanio; i++) {
            ptr_ultimo++;
        }
        *monticulo->elementos = *ptr_ultimo;
        
        // Bubble down: bajar el elemento desde la raíz
        int indice = 0;
        while (true) {
            int hijo_izq = obtener_hijo_izquierdo(indice);
            int hijo_der = obtener_hijo_derecho(indice);
            int menor = indice;
            
            // Encontrar el menor entre padre e hijos
            if (hijo_izq < monticulo->tamanio) {
                struct Articulo** ptr_menor = monticulo->elementos;
                for (int i = 0; i < menor; i++) ptr_menor++;
                
                struct Articulo** ptr_izq = monticulo->elementos;
                for (int i = 0; i < hijo_izq; i++) ptr_izq++;
                
                if (comparar_articulos(*ptr_izq, *ptr_menor, monticulo->tipo_ordenamiento)) {
                    menor = hijo_izq;
                }
            }
            
            if (hijo_der < monticulo->tamanio) {
                struct Articulo** ptr_menor = monticulo->elementos;
                for (int i = 0; i < menor; i++) ptr_menor++;
                
                struct Articulo** ptr_der = monticulo->elementos;
                for (int i = 0; i < hijo_der; i++) ptr_der++;
                
                if (comparar_articulos(*ptr_der, *ptr_menor, monticulo->tipo_ordenamiento)) {
                    menor = hijo_der;
                }
            }
            
            if (menor == indice) break; // Ya está en posición correcta
            
            // Intercambiar
            struct Articulo** ptr_indice = monticulo->elementos;
            for (int i = 0; i < indice; i++) ptr_indice++;
            
            struct Articulo** ptr_menor_final = monticulo->elementos;
            for (int i = 0; i < menor; i++) ptr_menor_final++;
            
            struct Articulo* temp = *ptr_indice;
            *ptr_indice = *ptr_menor_final;
            *ptr_menor_final = temp;
            
            indice = menor;
        }
    }
    
    return minimo;
}

/* 
Liberar memoria del montículo de artículos
E: puntero al montículo
S: void (libera la memoria, NO libera los artículos)
*/
void liberar_monticulo_articulos(struct MonitculoArticulos* monticulo) {
    if (!monticulo) return;
    
    if (monticulo->elementos) {
        free(monticulo->elementos);
    }
    
    free(monticulo);
}

//######################################################
//          SISTEMA DE MENÚS
//######################################################

/* 
Mostrar menú principal
E: void
S: void
*/

void mostrar_menu_principal() {
    printf("\n");

    printf(CYANB "╔══════════════════════════════════════════════════╗\n");
    printf("║       SISTEMA DE ORDENAMIENTO DE ARTÍCULOS       ║\n");
    printf("╠══════════════════════════════════════════════════╣\n" RESET);

    printf(CYANB "║  " YELLOW "[0]" RESET " " WHITEB "Salir                                       " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[1]" RESET " " WHITEB "Año publicación (viejo → nuevo)             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[2]" RESET " " WHITEB "Año publicación (nuevo → viejo)             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[3]" RESET " " WHITEB "Tamaño del título (menos → más)             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[4]" RESET " " WHITEB "Tamaño del título (más → menos)             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[5]" RESET " " WHITEB "Títulos (A → Z)                             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[6]" RESET " " WHITEB "Títulos (Z → A)                             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[7]" RESET " " WHITEB "Archivo (A → Z)                             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[8]" RESET " " WHITEB "Archivo (Z → A)                             " CYANB "║\n" RESET);
    printf(CYANB "║  " YELLOW "[9]" RESET " " WHITEB "Nombre autor (A → Z)                        " CYANB "║\n" RESET);
    printf(CYANB "║ " YELLOW "[10]" RESET " " WHITEB "Nombre autor (Z → A)                        " CYANB "║\n" RESET);
    printf(CYANB "║ " YELLOW "[11]" RESET " " WHITEB "Apellido autor (A → Z)                      " CYANB "║\n" RESET);
    printf(CYANB "║ " YELLOW "[12]" RESET " " WHITEB "Apellido autor (Z → A)                      " CYANB "║\n" RESET);

    printf(CYANB "╚══════════════════════════════════════════════════╝\n" RESET);

    printf(GREENB "Seleccione una opción: " RESET);
}
/* 
Mostrar artículos ordenados
E: array de artículos ordenados, cantidad total, cantidad a mostrar
S: void
*/
void mostrar_articulos_ordenados(struct Articulo** articulos, int total, int cantidad_mostrar) {
    if (!articulos) return;

    if (cantidad_mostrar > total) {
        cantidad_mostrar = total;
    }

    printf("\n" CYANB "==============================================" RESET "\n");
    printf(CYANB "   RESULTADOS  " RESET "(mostrando %d de %d)\n", cantidad_mostrar, total);
    printf(CYANB "==============================================\n\n" RESET);

    struct Articulo** ptr = articulos;

    for (int i = 0; i < cantidad_mostrar; i++) {

        
        printf(GREENB "│" RESET "  " YELLOW "--- Artículo %d ---" RESET "                                \n", i + 1);
        

        printf(GREENB "│ " RESET CYANB "Título:   " RESET "%-30s" GREENB "\n" RESET, (*ptr)->titulo);
        printf(GREENB "│ " RESET CYANB "Autor:    " RESET "%-30s" GREENB "\n" RESET, (*ptr)->nombre_autor);
        printf(GREENB "│ " RESET CYANB "Apellido: " RESET "%-30s" GREENB "\n" RESET, (*ptr)->apellido_autor);
        printf(GREENB "│ " RESET CYANB "Año:      " RESET "%-30s" GREENB "\n" RESET, (*ptr)->anio);

       

        printf(GREENB "│ " RESET CYANB "Abstract:" RESET " %s\n" , (*ptr)->abstract);
        
        
        
        printf(GREENB "│ " RESET CYANB "Ruta: " RESET "%s\n", (*ptr)->ruta);
        
        printf("\n");
        ptr++;
    }
}


/* 
Ordenar artículos usando heap
E: array de artículos, cantidad, tipo de ordenamiento
S: void (modifica el array original con el orden)
*/
void ordenar_articulos_heap(struct Articulo** articulos, int cantidad, int tipo_ordenamiento) {
    if (!articulos || cantidad <= 0) return;
    
    // Crear heap
    struct MonitculoArticulos* heap = crear_monticulo_articulos(cantidad, tipo_ordenamiento);
    if (!heap) {
        printf("Error al crear heap\n");
        return;
    }
    
    // Insertar todos los artículos en el heap
    struct Articulo** ptr = articulos;
    for (int i = 0; i < cantidad; i++) {
        insertar_articulo(heap, *ptr);
        ptr++;
    }
    
    // Extraer todos en orden y guardarlos de vuelta en el array
    for (int i = 0; i < cantidad; i++) {
        struct Articulo** ptr_destino = articulos;
        for (int j = 0; j < i; j++) {
            ptr_destino++;
        }
        *ptr_destino = extraer_minimo(heap);
    }
    
    // Liberar heap
    liberar_monticulo_articulos(heap);
}

//######################################################
//                 MAIN CON MENÚ
//######################################################

int main() {
    printf(GREENB "\n\n=== SISTEMA DE GESTION DE ARTICULOS ===\n\n" RESET);
    
    // Leer artículos del archivo
    int cantidad = 0;
    struct Articulo** articulos = leer_articulos_desde_archivo("repo/Articulos.txt", &cantidad);
    
    if (!articulos) {
        printf(REDB "Error al leer el archivo\n" RESET);
        return 1;
    }
    
    printf(GREENB "Articulos cargados: " RESET "%d\n", cantidad);
    
    int opcion = -1;
    while (opcion != 0) {
        mostrar_menu_principal();
        scanf("%d", &opcion);
        
        if (opcion > 0 && opcion < 13) {
            printf(YELLOW "\n¿Cuántos artículos desea mostrar? (1-%d): " RESET, cantidad);
            int cantidad_mostrar;
            scanf("%d", &cantidad_mostrar);
            
            if (cantidad_mostrar < 1 || cantidad_mostrar > cantidad) {
                printf(REDB "Cantidad invalida\n" RESET);
                opcion = 0;
                continue;
            }

            const char* tipo_texto;
            // Ordenar
            switch (opcion) {
                case 1:
                    tipo_texto = "año de publicación (viejo a nuevo)";
                    break;
                case 2:
                    tipo_texto = "año de publicación (nuevo a viejo)";
                    break;
                case 3:
                    tipo_texto = "tamaño del título (menos a más)";
                    break;
                case 4:
                    tipo_texto = "tamaño del título (más a menos)";
                    break;
                case 5:
                    tipo_texto = "título (alfabético ascendente)";
                    break;
                case 6:
                    tipo_texto = "título (alfabético descendente)";
                    break;
                case 7:
                    tipo_texto = "nombre del archivo (alfabético ascendente)";
                    break;
                case 8:
                    tipo_texto = "nombre del archivo (alfabético descendente)";
                    break;
                case 9:
                    tipo_texto = "nombre del autor (alfabético ascendente)";
                    break;
                case 10:
                    tipo_texto = "nombre del autor (alfabético descendente)";
                    break;
                case 11:
                    tipo_texto = "apellido del autor (alfabético ascendente)";
                    break;
                case 12:
                    tipo_texto = "apellido del autor (alfabético descendente)";
                    break;
            }
            printf(GREENB "\nOrdenando por %s...\n" RESET, tipo_texto);
            ordenar_articulos_heap(articulos, cantidad, opcion);
            
            // Mostrar resultados
            mostrar_articulos_ordenados(articulos, cantidad, cantidad_mostrar);
            
        } else if (opcion == 0) {
            printf(BLUEB "\nSaliendo del programa...\n" RESET);
        } else {
            printf(REDB "\nOpcion invalida\n" RESET);
            opcion = 0;
        }
    }
    
    // Liberar memoria
    liberar_articulos(articulos, cantidad);
    printf(BLUEB "Memoria liberada. Programa terminado.\n" RESET);
    
    return 0;
}