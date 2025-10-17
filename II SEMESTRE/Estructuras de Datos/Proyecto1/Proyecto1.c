#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h> // Para usar tipo bool, true, false


//######################################################
//          ESTRUCTURAS
//######################################################

//-------------------------------------------------------
//FUNCIONES DE PAIS
//-------------------------------------------------------

//Crea el nodo llamado Pais
struct Pais {
    struct Pais* prev; //punteros lista
    struct Pais* next;
    char nombre[20];    //nombre
    int primer_valor; //primer aspecto
    int segundo_valor; //segundo aspecto
};


// Crear un nuevo país
//E: constante de nombre, primer_valor y segundo valor

struct Pais* createNewPais(const char* nombre, int primer_valor, int segundo_valor) {
    struct Pais* newPais = calloc(1, sizeof(struct Pais));
    if (!newPais) return NULL;

    //metodo para ponerle el nombre
    strncpy(newPais->nombre, nombre, sizeof(newPais->nombre) - 1);
    newPais->nombre[sizeof(newPais->nombre) - 1] = '\0';

    //valores
    newPais->primer_valor = primer_valor;
    newPais->segundo_valor = segundo_valor;

    //punteros
    newPais->prev = NULL;
    newPais->next = NULL;

    return newPais;
}




//--------------------------------------------------------------------------
//  FUNCIONES DE Y PARA LISTA
//--------------------------------------------------------------------------------

//Lista DOblemente enlazada
struct Latinoamerica {
    struct Pais* start;
    struct Pais* end;
};

/*
// Mezclar arreglo de strings
//E: arreglo de caracteres
//Cantidad de paises que se desean
void shuffle(char* arr[], int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        char* temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
ESTA PARTE SE PUEDE ELIMINAR PERO LA DEJO POR SI SE OCUPA DESPUES
*/

// Agregar país al final de la lista
//E: lista y pais
//S: pais agregado al final
void agregarPais(struct Latinoamerica* lista, struct Pais* nuevo) {
    if (lista->start == NULL) {
        lista->start = nuevo;
        lista->end = nuevo;
    } else {
        lista->end->next = nuevo;
        nuevo->prev = lista->end;
        lista->end = nuevo;
    }
}

//Imprimir lista
void printList(struct Latinoamerica* lista){
    // Mostrar la lista
    struct Pais* actual = lista->start;
    while (actual) {
        printf("%s -> [%d, %d]\n", actual->nombre, actual->primer_valor, actual->segundo_valor);
        actual = actual->next;
    }
}

//IMPRIME LATAM
void imprimirLatinoamerica(struct Latinoamerica* lista) {
    printf("Recorrido norte → sur:\n");
    struct Pais* actual = lista->start;
    while (actual) {
        printf("%s ", actual->nombre);
        actual = actual->next;
    }

    printf("\nRecorrido sur → norte:\n");
    actual = lista->end;
    while (actual) {
        printf("%s ", actual->nombre);
        actual = actual->prev;
    }
    printf("\n");
}

//Recibe un pais y lo elimina (arregla fronteras y punteros)
void eliminarPais(struct Latinoamerica* lista, struct Pais* pais) {
    if (!lista || !pais) return;

    // Si es el inicio
    if (pais == lista->start)
        lista->start = pais->next;

    // Si es el final
    if (pais == lista->end)
        lista->end = pais->prev;

    // Reconectar punteros vecinos
    if (pais->prev)
        pais->prev->next = pais->next;

    if (pais->next)
        pais->next->prev = pais->prev;

    free(pais);
}

//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
// UN RANDINT PA
//$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

//Para aleatorizar todo, se implementa un randint
// REcordar en main usar "srand(time(NULL));" para que sea diferente cada vez que se corre
//E: max y min
//S: numero aleatorio

int randint(int min, int max) {
    
    if (min > max) {
        // Intercambiar si min es mayor que max
        int temp = min;
        min = max;
        max = temp;
    }
    return rand() % (max - min + 1) + min;
}


//###############################################################
//      FUNCIONES DE DIFICULTAD, TAMANNIO Y VALORES DE PAISES
//###############################################################

// Asignar valores según tamaño, dificultad y posición
//REVISAR (es muy dificil la diff?)
//Da los valores de los paises
//E: tipo [tamannio de mapa (0,1,2)] {pequennio, mediano y grande}
// dificultad (0,1,2), indice [pais o poisicion en la lista], valor 1 y 2

//S: Solo modifica los valores internos de pais dependiendo su posicion en la lista, tamannio del mapa y dificultad
void asignarValores(int tipo, int dificultad, int index, int* val1, int* val2) {
    switch(tipo) {
        case 0: // Pequeño
            if (index == 0) { *val1=2; *val2=1+dificultad;}
            else if (index == 1) { *val1=1+dificultad; *val2=1; }
            else if (index == 2) { *val1=1; *val2=0+dificultad; }
            else { *val1=1+dificultad; *val2=1; }
            break;
        case 1: // Mediano
            if (index < 3) { *val1=3; *val2=2; }
            else if (index < 6) { *val1=2; *val2=1+dificultad; }
            else { *val1=1; *val2=1+dificultad; }
            break;
        case 2: // Grande
            if (index < 5) { *val1=2; *val2=1+dificultad; }
            else if (index < 11) { *val1=1; *val2=1+dificultad; }
            else { *val1=0+dificultad; *val2=1; }
            break;
    }

    // Limitar máximo 3
    if (*val1 > 3) *val1 = 3;
    if (*val2 > 3) *val2 = 3;
}


// Generar lista de países aleatoria según tamaño y dificultad
struct Latinoamerica* generarLatinoamericaAleatoria(int tipo, int dificultad) {
    struct Latinoamerica* lista = calloc(1, sizeof(struct Latinoamerica));
    if (!lista) return NULL;

    const char* paises[17] = {
        "Mexico", "Guatemala", "Honduras", "El Salvador",
        "Nicaragua", "Costa Rica", "Panama", "Colombia",
        "Venezuela", "Ecuador", "Peru", "Bolivia",
        "Paraguay", "Chile", "Argentina", "Uruguay", "Brasil"
    };

    int cantidad;
    switch (tipo) {
        case 0: cantidad = 4; break;   // pequeño
        case 1: cantidad = 9; break;   // mediano
        case 2: cantidad = 17; break;  // grande
        default: free(lista); return NULL;
    }

    int pais_inicial = randint(0, 16);
    for (int i = 0; i < cantidad; i++) {
        int val1, val2;
        asignarValores(tipo, dificultad, i, &val1, &val2);
        struct Pais* nuevo = createNewPais(paises[pais_inicial], val1, val2);
        pais_inicial += 1;
        if (pais_inicial == 17){
            pais_inicial = 0;
        }
        agregarPais(lista, nuevo);
    }

    return lista;
}

// Liberar memoria de la lista
void liberarLista(struct Latinoamerica* lista) {
    if (!lista) return;
    struct Pais* actual = lista->start;
    while (actual) {
        struct Pais* temp = actual->next;
        free(actual);
        actual = temp;
    }
    free(lista);
}


//En lista doblemente enlazada luego puedo dependiendo del tamannio solo asignar con 3 todos los paises que deseo eliminar y luego los elimino.


//#################################################################################
//  IA
//#################################################################################

//Se crea
struct ONU {
    struct Pais* actualPais; //Pais al que ve
};


//La probabilidad de exito se da por un valor y un random.
//Por ejemplo se da de 0 a 3. Si es igual a 0 falla el proyecto, (o sea un 25% de prob de fracaso)
struct ONU* createNewIA(){
    struct ONU* newONU = calloc(1, sizeof(struct ONU));
    if (!newONU) return NULL;    
    //direcciones
    newONU->actualPais = NULL; //No esta en ningun pais por ahora
    return newONU;
};

//################################################################
// ACCIONES Y CONSIDERACIONES DE PAISES
//################################################################
//COntiene las cosas que se deben realizar a los paises

//REcibe la lista y luego solo elimina los paises cuyos 2 valores sean 3
int quitarPaisesMuertos(struct Latinoamerica* lista) {
    if (!lista || !lista->start) return 0;

    struct Pais* actual = lista->start;
    int paises_muertos = 0;

    while (actual) {
        struct Pais* siguiente = actual->next; // guarda antes de eliminar

        if (actual->primer_valor == 3 && actual->segundo_valor == 3) {
            eliminarPais(lista, actual);
            paises_muertos++;
        }

        actual = siguiente; // moverse al siguiente guardado
    }

    return paises_muertos;
}

//E: tamannio de lista, lista y probabilidad_aumentar
void aumentarAleatorio(struct Latinoamerica* lista, int probabilidad_aumentar, int tamannio){
    //NUmeros aleatorios
    int probabilidad = randint(0,probabilidad_aumentar); //probabilidad que dice si aumenta o no
    int numero_a_aumentar = randint(0,3);
    int indice_pais_aumentar = randint(0,tamannio); //indice del pais a aumentar, es un indice aleatorio junto al tamannio
    int valor = randint(0,1); //SI es 0 es el primer valor el que sufre, si es 1 es el segundo.

    //avanza al pais escogido
    struct Pais* actual = lista->start; //puntero temporal
    for (int i = 0; i < indice_pais_aumentar && actual->next; i++) {
        actual = actual->next;
    }

// Aumenta el valor correspondiente
    if (probabilidad == 0) {
        int* objetivo = (valor == 0) ? &actual->primer_valor : &actual->segundo_valor; //Equivalente a un if-else sin ser if-else
        *objetivo += numero_a_aumentar;
        if (*objetivo > 3) *objetivo = 3; // limitar al máximo
    }

}

//TODO: EXPANSION DE VALORES A OTROS PAISES
//E: int probabilidad de expansion, LATAM, 
//S: void (solo cambia valores dentro de los paises)
void expansionValores(struct Latinoamerica* lista, int cantidad_aumentar) {
    if (!lista || !lista->start) return;

    struct Pais* actual = lista->start;

    while (actual) {
        // Expande si el primer valor llegó a 3
        if (actual->primer_valor == 3) {
            int valor = randint(0, 1); // 0 = derecha, 1 = izquierda
            struct Pais* vecino = (valor == 0) ? actual->next : actual->prev;

            if (vecino) {
                int* objetivo = (valor == 0) ? &vecino->primer_valor : &vecino->segundo_valor;
                *objetivo += cantidad_aumentar;
                if (*objetivo > 3) *objetivo = 3;
                printf("%s expandió a %s (valor %d → %d)\n",
                       actual->nombre, vecino->nombre, *objetivo - cantidad_aumentar, *objetivo);
            }
        }

        // Expande si el segundo valor llegó a 3
        if (actual->segundo_valor == 3) {
            int valor = randint(0, 1);
            struct Pais* vecino = (valor == 0) ? actual->next : actual->prev;

            if (vecino) {
                int* objetivo = (valor == 0) ? &vecino->segundo_valor : &vecino->primer_valor;
                *objetivo += cantidad_aumentar;
                if (*objetivo > 3) *objetivo = 3;
                printf("%s expandió a %s (valor %d → %d)\n",
                       actual->nombre, vecino->nombre, *objetivo - cantidad_aumentar, *objetivo);
            }
        }

        actual = actual->next;
    }
}
//#######################################
//ACIONES DE LA IA
//#########################################
//-------------------------------------------------------------------------------
//                      MOVIMIENTOS IA
//-------------------------------------------------------------------------------
bool moverse_derecha(struct Latinoamerica* lista, struct ONU* ONU) {
    if (!ONU || !lista) return false;

    // Si aún no está posicionada, la ponemos al final
    if (ONU->actualPais == NULL) {
        ONU->actualPais = lista->end;
    }

    // Si ya está al final
    if (ONU->actualPais->next == NULL) {
        ONU->actualPais = lista->start;      //si esta en el final va al inicio
    } else {
        ONU->actualPais = ONU->actualPais->next;
    }

    printf("Posicion Onu %s \n", ONU->actualPais->nombre);
    return true;
    
}


bool moverse_izquierda(struct Latinoamerica* lista, struct ONU* ONU) {
    if (!ONU || !lista) return false;

    // Si aún no está posicionada, la ponemos al final
    if (ONU->actualPais == NULL) {
        ONU->actualPais = lista->end;
    }

    if (ONU->actualPais->prev == NULL) {
        ONU->actualPais = lista->end;  //SI esta al inicio pasa al final
    } else {
        ONU->actualPais = ONU->actualPais->prev;
    }

    printf("Posicion Onu %s \n", ONU->actualPais->nombre);
    return true;
}

bool ponerONU(struct Latinoamerica* lista, struct ONU* ONU) {
    if (!ONU || !lista) return false;

    // Si aún no está posicionada, la ponemos al final
    if (ONU->actualPais == NULL) {
        ONU->actualPais = lista->end;
    }
    return true;
}

bool hacerProyectoIA(int probabilidad_fracaso_proyecto, struct Pais* pais){
    
    int probabilidad = randint(0,probabilidad_fracaso_proyecto);
    int valor = randint(0,1); //SI es 0 es el primer valor el que sufre, si es 1 es el segundo.
    int numero_a_aumentar = randint(0,3); //probabilidad que dice si aumenta 0, 1 o 2 en un elemento o disminuye


    if (probabilidad == 0) {
        int* objetivo = (valor == 0) ? &pais->primer_valor : &pais->segundo_valor; //Equivalente a un if-else sin ser if-else
        *objetivo += numero_a_aumentar;
        if (*objetivo > 3) *objetivo = 3; // limitar al máximo
        printf("La ONU fracaso, aumento en uno de los aspectos negativos del pais: %s, una sorprendente cantidad de: %d \n",pais->nombre, numero_a_aumentar);
        return false;
    } else {
        int* objetivo = (valor == 0) ? &pais->primer_valor : &pais->segundo_valor; //Equivalente a un if-else sin ser if-else
        if (*objetivo == 0){
            // Cambiar de campo
            if (objetivo == &pais->primer_valor){
                objetivo = &pais->segundo_valor;
            }
            else{
                objetivo = &pais->primer_valor;
            };
        } 
        *objetivo -= numero_a_aumentar;
        if (*objetivo < 0) *objetivo = 0; // limitar al minimo
        printf("La ONU hizo un proyecto con exito, disminuyo en uno de los aspectos negativos del pais: %s, una sorprendente cantidad de: %d \n",pais->nombre, numero_a_aumentar);
        return true;
    }

    
}

bool turnoIA (struct Latinoamerica* lista, struct ONU* onu, int cant_movimientos, int probabilidad_fracaso_proyecto){
    
    if (!lista || !onu || !onu->actualPais) return false;


    while (cant_movimientos > 0){
        
        int accion = randint(0,2);

        if (accion == 0 || accion == 1){
            if (onu->actualPais->primer_valor == 3|| onu->actualPais->segundo_valor == 3){
                accion = 2;
            };
        };
        if (accion == 2){
            if (onu->actualPais->primer_valor == 0 || onu->actualPais->segundo_valor == 0){
                accion = randint(0,1);
            };
        };
        switch(accion) {
        case 0: 
            moverse_izquierda(lista, onu);
            break;
        case 1: 
            moverse_derecha(lista,onu);
            break;
        case 2: 
            hacerProyectoIA(probabilidad_fracaso_proyecto, onu->actualPais);
            break;
        }
        cant_movimientos -= 1;
    }
    return true;
}

//################################################################
// TABLA DE DISPERSIÓN DE PROYECTOS
//################################################################

#define TAMANIO_INICIAL_TABLA 20
#define FACTOR_CARGA_MAX 0.7

// Estructura de un proyecto
struct Proyecto {
    char nombre[100];
    char descripcion[300];
    char bibliografia[400];
    char paises[200];  // países donde se aplicó
    int aspecto;  // 1 = gestión pública, 2 = salud
    struct Proyecto* siguiente;  // para colisiones (encadenamiento)
};

// Tabla de dispersión
struct TablaProyectos {
    struct Proyecto** tabla;
    int tamanio;
    int elementos;
};

//----------------------------------------------------------------
// FUNCIÓN DE HASH
//----------------------------------------------------------------
// Función hash simple usando suma de caracteres
unsigned int funcionHash(const char* clave, int tamanio) {
    unsigned int hash = 0;
    for (int i = 0; clave[i] != '\0'; i++) {
        hash = (hash * 31 + clave[i]) % tamanio;
    }
    return hash;
}

//----------------------------------------------------------------
// CREAR TABLA
//----------------------------------------------------------------
struct TablaProyectos* crearTablaProyectos() {
    struct TablaProyectos* tabla = calloc(1, sizeof(struct TablaProyectos));
    if (!tabla) return NULL;
    
    tabla->tamanio = TAMANIO_INICIAL_TABLA;
    tabla->elementos = 0;
    tabla->tabla = calloc(tabla->tamanio, sizeof(struct Proyecto*));
    
    if (!tabla->tabla) {
        free(tabla);
        return NULL;
    }
    
    return tabla;
}
//----------------------------------------------------------------
// CREAR PROYECTO
//----------------------------------------------------------------

struct Proyecto* crearProyecto(const char* nombre, const char* descripcion, 
                            const char* bibliografia, const char* paises, int aspecto) {
    struct Proyecto* nuevo = calloc(1, sizeof(struct Proyecto));
    if (!nuevo) return NULL;
    
    strncpy(nuevo->nombre, nombre, sizeof(nuevo->nombre) - 1);
    strncpy(nuevo->descripcion, descripcion, sizeof(nuevo->descripcion) - 1);
    strncpy(nuevo->bibliografia, bibliografia, sizeof(nuevo->bibliografia) - 1);
    strncpy(nuevo->paises, paises, sizeof(nuevo->paises) - 1);
    nuevo->aspecto = aspecto;
    nuevo->siguiente = NULL;
    
    return nuevo;
}

//----------------------------------------------------------------
// REDIMENSIONAR TABLA
//----------------------------------------------------------------
void redimensionarTabla(struct TablaProyectos* tabla) {
    int nuevoTamanio = tabla->tamanio * 2;
    struct Proyecto** nuevaTabla = calloc(nuevoTamanio, sizeof(struct Proyecto*));
    
    if (!nuevaTabla) return;
    
    // Reinsertar todos los elementos
    for (int i = 0; i < tabla->tamanio; i++) {
        struct Proyecto* actual = tabla->tabla[i];
        while (actual) {
            struct Proyecto* siguiente = actual->siguiente;
            
            // Calcular nueva posición
            unsigned int nuevaPos = funcionHash(actual->nombre, nuevoTamanio);
            
            // Insertar en nueva tabla
            actual->siguiente = nuevaTabla[nuevaPos];
            nuevaTabla[nuevaPos] = actual;
            
            actual = siguiente;
        }
    }
    
    free(tabla->tabla);
    tabla->tabla = nuevaTabla;
    tabla->tamanio = nuevoTamanio;
    
    printf("Tabla redimensionada a %d\n", nuevoTamanio);
}

//----------------------------------------------------------------
// INSERTAR PROYECTO
//----------------------------------------------------------------

bool insertarProyecto(struct TablaProyectos* tabla, const char* nombre, const char* descripcion, const char* bibliografia, 
                    const char* paises, int aspecto) {
    if (!tabla) return false;
    
    // Verificar factor de carga
    float factorCarga = (float)tabla->elementos / tabla->tamanio;
    if (factorCarga > FACTOR_CARGA_MAX) {
        redimensionarTabla(tabla);
    }
    
    unsigned int posicion = funcionHash(nombre, tabla->tamanio);
    
    struct Proyecto* nuevo = crearProyecto(nombre, descripcion, bibliografia, paises, aspecto);
    if (!nuevo) return false;
    
    // Insertar al inicio de la lista (manejo de colisiones)
    nuevo->siguiente = tabla->tabla[posicion];
    tabla->tabla[posicion] = nuevo;
    tabla->elementos++;
    
    return true;
}

//----------------------------------------------------------------
// CARGAR PROYECTOS DE CORRUPCIÓN
//----------------------------------------------------------------

void cargarProyectosCorrupcion(struct TablaProyectos* tabla) {
    // PROYECTOS DE GESTIÓN PÚBLICA (aspecto 1)
    
    insertarProyecto(tabla, 
        "Sanciones administrativas",
        "Leyes que permitan sancionar funcionarios publicos por actos de corrupcion",
        "Peru tiene procedimientos sancionadores efectivos",
        "Peru",
        1);
    
    insertarProyecto(tabla,
        "Licitaciones transparentes",
        "Procesos de compra publica transparentes con licitacion",
        "Chile tiene portal ChileCompra que mejora transparencia",
        "Chile",
        1);
    
    insertarProyecto(tabla,
        "Supervision externa",
        "ONGs u organismos internacionales revisan gasto publico",
        "Presion mediatica lleva a reformas",
        "Varios paises",
        1);
    
    insertarProyecto(tabla,
        "Canales de denuncia",
        "Mecanismos seguros para denunciar irregularidades",
        "Proteccion a denunciantes reduce corrupcion",
        "Latinoamerica",
        1);
    
    insertarProyecto(tabla,
        "Digitalizacion de compras",
        "Sistemas digitales para tramites de compras y contratos",
        "Peru usa PAS digital, Chile usa ChileCompra",
        "Peru, Chile",
        1);
    
    insertarProyecto(tabla,
        "Portal transparencia",
        "Plataforma digital con contratos publicos accesibles",
        "BID indica que mejora gestion financiera",
        "Varios paises",
        1);
    
    insertarProyecto(tabla,
        "Blockchain compras",
        "Blockchain para registro de procesos de contratacion",
        "Costa Rica estudia SICOP con blockchain",
        "Costa Rica",
        1);
    
    insertarProyecto(tabla,
        "Analisis predictivo",
        "Machine learning para detectar patrones de corrupcion",
        "Mexico usa modelo para identificar contratos corruptos",
        "Mexico",
        1);
    
    // PROYECTOS DE SALUD (aspecto 2)
    
    insertarProyecto(tabla,
        "Denuncias salud",
        "Canales anonimos para denunciar corrupcion en salud",
        "Proteccion a denunciantes reduce corrupcion detectada",
        "Latinoamerica",
        2);
    
    insertarProyecto(tabla,
        "Whistleblower protections",
        "Proteccion legal a denunciantes en sector salud",
        "Costa Rica y Peru tienen sistemas de proteccion",
        "Costa Rica, Peru",
        2);
    
    insertarProyecto(tabla,
        "Auditorias rapidas",
        "Auditorias independientes rapidas ante alertas",
        "COVID-19 demostro efectividad de auditorias externas",
        "Varios paises",
        2);
    
    insertarProyecto(tabla,
        "Digitalizacion salud",
        "Sistemas digitales para compras de insumos medicos",
        "Reduce sobornos en compras medicas",
        "Varios paises",
        2);
    
    printf("Proyectos cargados: %d\n", tabla->elementos);
}

//----------------------------------------------------------------
// BUSCAR PROYECTOS POR ASPECTO
//----------------------------------------------------------------

void listarProyectosPorAspecto(struct TablaProyectos* tabla, int aspecto) {
    if (!tabla) return;
    
    const char* nombreAspecto = (aspecto == 1) ? "Gestion publica" : "Salud";
    printf("\n=== Proyectos de %s ===\n", nombreAspecto);
    
    int contador = 1;
    for (int i = 0; i < tabla->tamanio; i++) {
        struct Proyecto* actual = tabla->tabla[i];
        while (actual) {
            if (actual->aspecto == aspecto) {
                printf("%d. %s\n", contador, actual->nombre);
                contador++;
            }
            actual = actual->siguiente;
        }
    }
}

//----------------------------------------------------------------
// MOSTRAR DETALLES DE PROYECTO
//----------------------------------------------------------------

struct Proyecto* buscarProyecto(struct TablaProyectos* tabla, const char* nombre) {
    if (!tabla) return NULL;
    
    unsigned int posicion = funcionHash(nombre, tabla->tamanio);
    struct Proyecto* actual = tabla->tabla[posicion];
    
    while (actual) {
        if (strcmp(actual->nombre, nombre) == 0) {
            return actual;
        }
        actual = actual->siguiente;
    }
    
    return NULL;
}

void mostrarDetallesProyecto(struct Proyecto* proyecto) {
    if (!proyecto) return;
    
    printf("\nProyecto: %s\n", proyecto->nombre);
    printf("Descripcion: %s\n", proyecto->descripcion);
    printf("Bibliografia: %s\n", proyecto->bibliografia);
    printf("Aplicado en: %s\n", proyecto->paises);
}

//################################################################
// ESTRUCTURA Y FUNCIONES DEL JUGADOR
//################################################################

struct Jugador {
    struct Pais* actualPais;
    char nombre[30];
};

// Crear jugador
struct Jugador* createNewJugador(const char* nombre) {
    struct Jugador* newJugador = calloc(1, sizeof(struct Jugador));
    if (!newJugador) return NULL;
    
    strncpy(newJugador->nombre, nombre, sizeof(newJugador->nombre) - 1);
    newJugador->nombre[sizeof(newJugador->nombre) - 1] = '\0';
    newJugador->actualPais = NULL;
    
    return newJugador;
}

// Posicionar jugador al inicio
bool ponerJugador(struct Latinoamerica* lista, struct Jugador* jugador) {
    if (!jugador || !lista || !lista->start) return false;
    
    if (jugador->actualPais == NULL) {
        jugador->actualPais = lista->start;
        printf("%s comienza en: %s\n", jugador->nombre, jugador->actualPais->nombre);
    }
    return true;
}

//----------------------------------------------------------------
// MOVIMIENTOS DEL JUGADOR 
//----------------------------------------------------------------

bool jugador_moverse_derecha(struct Latinoamerica* lista, struct Jugador* jugador) {
    if (!jugador || !lista || !jugador->actualPais) return false;

    if (jugador->actualPais->next == NULL) {
        jugador->actualPais = lista->start;
    } else {
        jugador->actualPais = jugador->actualPais->next;
    }

    printf("Te moviste a: %s\n", jugador->actualPais->nombre);
    return true;
}

bool jugador_moverse_izquierda(struct Latinoamerica* lista, struct Jugador* jugador) {
    if (!jugador || !lista || !jugador->actualPais) return false;

    if (jugador->actualPais->prev == NULL) {
        jugador->actualPais = lista->end;
    } else {
        jugador->actualPais = jugador->actualPais->prev;
    }

    printf("Te moviste a: %s\n", jugador->actualPais->nombre);
    return true;
}

//################################################################
// CONDICIONES DE VICTORIA Y DERROTA
//################################################################

bool verificarVictoria(struct Latinoamerica* lista) {
    if (!lista || !lista->start) return false;
    
    bool aspecto1_erradicado = true;
    bool aspecto2_erradicado = true;
    
    struct Pais* actual = lista->start;
    while (actual) {
        if (actual->primer_valor > 0) aspecto1_erradicado = false;
        if (actual->segundo_valor > 0) aspecto2_erradicado = false;
        actual = actual->next;
    }
    
    if (aspecto1_erradicado || aspecto2_erradicado) {
        printf("\nVICTORIA! Erradicaron por completo un aspecto negativo de todos los paises!\n");
        return true;
    }
    
    return false;
}

int contarPaises(struct Latinoamerica* lista) {
    if (!lista || !lista->start) return 0;
    
    int count = 0;
    struct Pais* actual = lista->start;
    while (actual) {
        count++;
        actual = actual->next;
    }
    return count;
}

bool verificarDerrota(struct Latinoamerica* lista) {
    int cantidad = contarPaises(lista);
    
    if (cantidad <= 3) {
        printf("\nDERROTA. Quedan solo %d paises.\n", cantidad);
        return true;
    }
    return false;
}

//----------------------------------------------------------------
// Hacer Proyectos 
//----------------------------------------------------------------

bool jugador_hacerProyecto(struct TablaProyectos* tablaProyectos, int probabilidad_fracaso_proyecto, struct Pais* pais) {
    if (!pais || !tablaProyectos) return false;
    
    printf("\nPais actual: %s [Gestion pub: %d, Salud: %d]\n", 
        pais->nombre, pais->primer_valor, pais->segundo_valor);
    
    // Mostrar qué aspecto se puede mejorar
    printf("\nQue aspecto deseas mejorar?\n");
    printf("1. Gestion publica (valor actual: %d)\n", pais->primer_valor);
    printf("2. Salud (valor actual: %d)\n", pais->segundo_valor);
    printf("0. Cancelar\n");
    printf("Opcion: ");
    
    int aspecto;
    scanf("%d", &aspecto);
    
    if (aspecto == 0) return false;
    if (aspecto != 1 && aspecto != 2) {
        printf("Opcion invalida\n");
        return false;
    }
    
    // Mostrar proyectos disponibles para ese aspecto
    listarProyectosPorAspecto(tablaProyectos, aspecto);
    
    // Crear array temporal con los proyectos del aspecto
    struct Proyecto* proyectosDisponibles[20];
    int contador = 0;
    
    for (int i = 0; i < tablaProyectos->tamanio && contador < 20; i++) {
        struct Proyecto* actual = tablaProyectos->tabla[i];
        while (actual && contador < 20) {
            if (actual->aspecto == aspecto) {
                proyectosDisponibles[contador] = actual;
                contador++;
            }
            actual = actual->siguiente;
        }
    }
    
    printf("\nSelecciona un proyecto (1-%d) o 0 para cancelar: ", contador);
    int seleccion;
    scanf("%d", &seleccion);
    
    if (seleccion == 0) return false;
    if (seleccion < 1 || seleccion > contador) {
        printf("Seleccion invalida\n");
        return false;
    }
    
    struct Proyecto* proyectoSeleccionado = proyectosDisponibles[seleccion - 1];
    mostrarDetallesProyecto(proyectoSeleccionado);
    
    // Intentar implementar el proyecto
    int probabilidad = randint(0, probabilidad_fracaso_proyecto);
    int numero_cambio = randint(1, 2);
    
    int* objetivo = (aspecto == 1) ? &pais->primer_valor : &pais->segundo_valor;
    
    if (probabilidad == 0) {
        // Fracaso
        *objetivo += numero_cambio;
        if (*objetivo > 3) *objetivo = 3;
        printf("\nProyecto FRACASO! Aspecto aumento en %d\n", numero_cambio);
        return false;
    } else {
        // Éxito
        *objetivo -= numero_cambio;
        if (*objetivo < 0) *objetivo = 0;
        printf("\nProyecto EXITOSO! Aspecto disminuyo en %d\n", numero_cambio);
        return true;
    }
}

//----------------------------------------------------------------
// Turno del jugador
//----------------------------------------------------------------

bool turnoJugador(struct Latinoamerica* lista, struct Jugador* jugador, 
                            struct TablaProyectos* tablaProyectos,
                            int cant_acciones, int probabilidad_fracaso_proyecto) {
    if (!lista || !jugador || !jugador->actualPais) return false;
    
    printf("\nTurno de: %s\n", jugador->nombre);
    printf("Acciones: %d\n", cant_acciones);
    
    while (cant_acciones > 0) {
        printf("\nPais actual: %s [%d, %d]\n", 
            jugador->actualPais->nombre, 
            jugador->actualPais->primer_valor, 
            jugador->actualPais->segundo_valor);
        
        printf("Acciones restantes: %d\n", cant_acciones);
        printf("1. Moverse derecha\n");
        printf("2. Moverse izquierda\n");
        printf("3. Implementar proyecto\n");
        printf("4. Ver mapa completo\n"); 
        printf("Opcion: ");
        
        int opcion;
        scanf("%d", &opcion);
        
        switch(opcion) {
            case 1:
                jugador_moverse_derecha(lista, jugador);
                cant_acciones--;
                break;
            case 2:
                jugador_moverse_izquierda(lista, jugador);
                cant_acciones--;
                break;
            case 3:
                if (jugador_hacerProyecto(tablaProyectos, probabilidad_fracaso_proyecto, jugador->actualPais)) {
                    cant_acciones--;
                } else {
                    printf("No se logro el proyecto\n");
                }
                break;
            case 4:
                printList(lista);
                break;
            default:
                printf("Opcion invalida\n");
        }
    }
    
    printf("Turno completado\n");
    return true;
}

//----------------------------------------------------------------
// Ciclo del juego
//----------------------------------------------------------------

void cicloDeJuego(struct Latinoamerica* lista, struct Jugador* jugador, struct ONU* onu, struct TablaProyectos* tablaProyectos,
                            int cant_acciones_jugador, int cant_acciones_onu, int prob_fracaso_proyecto, int prob_aumentar_pais, 
                            int max_valor_expansion) {
    
    int tamannio = contarPaises(lista);
    
    printf("\nComienza la partida\n");
    printf("Paises iniciales: %d\n", tamannio);
    
    while (true) {
        printf("\n=====================================\n");
        printf("Paises restantes: %d\n", tamannio);
        
        // TURNO DEL JUGADOR
        turnoJugador(lista, jugador, tablaProyectos, cant_acciones_jugador, prob_fracaso_proyecto);
        
        if (verificarVictoria(lista)) break;
        
        // TURNO DE LA ONU
        printf("\nTurno de la ONU\n");
        turnoIA(lista, onu, cant_acciones_onu, prob_fracaso_proyecto);
        
        if (verificarVictoria(lista)) break;
        
        // EXPANSION DE PROBLEMATICAS
        printf("\nExpansion de aspectos problematicos\n");
        aumentarAleatorio(lista, prob_aumentar_pais, tamannio);
        expansionValores(lista, max_valor_expansion);
        
        // ELIMINAR PAISES MUERTOS
        int paises_muertos = quitarPaisesMuertos(lista);
        if (paises_muertos > 0) {
            printf("%d pais(es) colapsaron\n", paises_muertos);
            tamannio -= paises_muertos;
        }
        
        printf("\nEstado del mapa:\n");
        printList(lista);
        
        if (verificarDerrota(lista)) break;
    }
    
    printf("\nFin de la partida\n");
}

//----------------------------------------------------------------
// LIBERAR TABLA
//----------------------------------------------------------------

void liberarTablaProyectos(struct TablaProyectos* tabla) {
    if (!tabla) return;
    
    for (int i = 0; i < tabla->tamanio; i++) {
        struct Proyecto* actual = tabla->tabla[i];
        while (actual) {
            struct Proyecto* temp = actual->siguiente;
            free(actual);
            actual = temp;
        }
    }
    
    free(tabla->tabla);
    free(tabla);
}

// MAIN 

int main() {
    srand(time(NULL));
    
    int tipo;
    int dificultad;
    
    printf("Tematica: CORRUPCION en Latinoamerica\n");
    printf("Aspectos: 1= Gestion publica, 2= Salud\n\n");
    
    printf("Selecciona tamano del mapa (0=pequeno, 1=mediano, 2=grande): ");
    scanf("%d", &tipo);
    
    printf("Selecciona dificultad (0=facil, 1=medio, 2=dificil): ");
    scanf("%d", &dificultad);
    
    // Variables de configuración
    int cantidad_mov_jugador = 4;
    int cantidad_mov_IA = 0;
    int prob_fracaso_proyecto = 0;
    int prob_aumentar_pais = 0;
    int max_valor_expansion = 0;
    
    if (dificultad == 0) {
        cantidad_mov_IA = 4;
        prob_fracaso_proyecto = 3;
        prob_aumentar_pais = 1;
        max_valor_expansion = 1;
    } else if (dificultad == 1) {
        cantidad_mov_IA = 4;
        prob_fracaso_proyecto = 2;
        prob_aumentar_pais = 0;
        max_valor_expansion = 1;
    } else {
        cantidad_mov_IA = 3;
        prob_fracaso_proyecto = 1;
        prob_aumentar_pais = 0;
        max_valor_expansion = 2;
    }
    
    // Crear el mundo
    struct Latinoamerica* lista = generarLatinoamericaAleatoria(tipo, dificultad);
    
    // Crear tabla de proyectos
    printf("\nCargando proyectos contra corrupcion...\n");
    struct TablaProyectos* tablaProyectos = crearTablaProyectos();
    cargarProyectosCorrupcion(tablaProyectos);
    
    // Crear jugadores
    printf("\nIngresa el nombre del Jugador: ");
    char nombre[30];
    scanf("%s", nombre);
    
    struct Jugador* jugador = createNewJugador(nombre);
    struct ONU* onu = createNewIA();
    
    // Posicionar jugadores
    ponerJugador(lista, jugador);
    ponerONU(lista, onu);
    
    printf("\nEstado inicial:\n");
    printList(lista);
    
    // INICIAR EL JUEGO
    cicloDeJuego(lista, jugador, onu, tablaProyectos,
                cantidad_mov_jugador, cantidad_mov_IA, 
                prob_fracaso_proyecto, prob_aumentar_pais, 
                max_valor_expansion);
    
    // Limpiar memoria
    free(jugador);
    free(onu);
    liberarTablaProyectos(tablaProyectos);
    liberarLista(lista);
    
    return 0;
}

//TODO: JUGADOR Y SUS FUNCIONES
//Comentarios mas bonitos en ciclo de juego

//SI DA TIEMPO HACEMOS EL MODO ONU DEMONIO (mayor cantidad de turnos pero mayor cantidad de fracaso en sus proyectos) u ONU utopia (menor cantidad de turno pero practicamente 100% de probabildad de exito)