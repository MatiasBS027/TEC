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

// Ejemplo de uso
int main() {
    srand(time(NULL));
    int tipo; // 0=pequeño,1=mediano,2=grande
    int dificultad; // afecta los valores
    printf("Escoga su tipo de mapa y nivel de dificultad\n");
    printf("Tipo: ");
    scanf("%d", &tipo);
    printf("\n DIff: ");
    scanf("%d", &dificultad);

    int tamannio = 0;   //tamannio del mapa se debe actualizar con el int que quita paises muertos y retorna la cantidad que fueron quitados 
    int cantidad_mov_IA = 0;    //cantidad de movimientos de la IA por turno
    int prob_fracaso_proyecto = 0;  //probabilidad de fracaso de la IA
    int prob_aumentar_pais = 0; //probabildiad que aumente en un pais aleatorio una problematica
    int max_valor_expansion = 0; //cantidad maxima del valor a la hora de expandirse
    //Definicion del tamannio
    if (tipo == 0 ){
        tamannio = 3;
    }
    else if (tipo == 1){
        tamannio = 8;
    }
    else {
        tipo = 2;
        tamannio = 16;
    };

    //definicion segun la dificultad de valores y que tan buena es la IA
    if (dificultad == 0){
        cantidad_mov_IA = 4;
        prob_fracaso_proyecto = 3;
        prob_aumentar_pais = 1;
        max_valor_expansion = 1;
    } else if (dificultad == 1){
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


    struct Latinoamerica* lista = generarLatinoamericaAleatoria(tipo, dificultad);
    struct ONU* onu = createNewIA();
    printList(lista);
    imprimirLatinoamerica(lista);

    ponerONU(lista, onu);

    printf("\n\n\n");
    printf("Turno de IA\n");
    turnoIA(lista, onu, cantidad_mov_IA, prob_fracaso_proyecto);
    printList(lista);

    aumentarAleatorio(lista,prob_aumentar_pais,tamannio);

    printf("Se aumentan los aspectos negativos en algun pais \n \n");
    printList(lista);

    printf("\n");
    expansionValores(lista, max_valor_expansion);
    printList(lista);
    
    int paises_muertos = quitarPaisesMuertos(lista);
    tamannio -= paises_muertos;
    printf("Lista post eliminados\n");
    printList(lista);
    
    liberarLista(lista);

    return 0;
}

//TODO: JUGADOR Y SUS FUNCIONES
//PROYECTOS DEL JUGADOR HASHMAP Y TODO ESO
//EL CICLO DE TURNOS
//GANAR/PERDER
//Comentarios mas bonitos en ciclo de juego

//SI DA TIEMPO HACEMOS EL MODO ONU DEMONIO (mayor cantidad de turnos pero mayor cantidad de fracaso en sus proyectos) u ONU utopia (menor cantidad de turno pero practicamente 100% de probabildad de exito)
Programa.c
19 KB