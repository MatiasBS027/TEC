/*
Last Stand para ver si se capta Djisktra (o como se llame), haciendo uso de Matriz de Adyacencia y mucha fe.
*/

#include <stdio.h> //Para I/O

#define infinito 99999999 //Valor absurdamente alto, para denominar a aquellos valores que no puedo llegar desde un nodo, o al inicializar 
// "Y voy a hacer copypaste de ese infinito un monton de veces " ~ Prof. Aurelio Sanabria
#define n_nodos 5     //Numero de nodos, no se me ocurrio alguna funcion en el poco tiempo


/*
ELIMINADA debido a apuro y el uso de define
Recibe una matriz de adyacencia y divide la cantidad total de espacio que ocupa la matriz y la divide entre las columnas, que da de resultado las filas
Debido a que es una matriz N*N esto equivale a la cantdiad de nodos.
E: matriz adyacencia
S: cantidad de nodos de esta

int cantidad_nodos (int matriz[N][N]){
    return n;
}
*/

/*
Funcion para encontrar (en dos arreglos, tomando en cuenta los visitados y la distancia de dichos visitados) el menor nodo no visitado 
Tenga en cuenta que los indices son usados como el numero o identificador de nodos

E: arreglo de distancias y arreglo de aquellos nodos visitados
S: nodo no visitado con menor distancia
*/
int minimo(int distancia[], int visitados[]) {
    int min = infinito; //Se define para llevar el conteo de la menor distancia detectada  
    int indice = -1;    //Si no se encontro ninguno sera -1

    for (int i = 0; i < n_nodos; i++) { //Se recorre todo en los arreglos
        if (visitados[i] == 0 && distancia[i] < min) {   //Mientras el indice o nodo sea igual a 0 (que muestra que NO ha sido visitado) y su distancia sea MENOR a INF
            min = distancia[i];  //El minimo se transforma en su distancia
            indice = i;     //Y su identificador o nombre o indice es marcado 
        }
    }
    return indice;  //Se retorna
}


/*
Funcion que hace el proceso de dijktra
Tenga en cuenta que los indices son usados como el numero o identificador de nodos
E: matriz y nodo por el cual se desea iniciar
S: Texto en consola
*/

void dijkstra(int matriz[n_nodos][n_nodos], int inicio){
    //Se requieren arreglos para almacenar las distancias y nodos visitados
    //Por ende se accede a la cantidad de nodos que ofrece la matriz

    int visitados[n_nodos]; //arreglo de n_nodos visitados
    int distancia[n_nodos]; //arreglo para la distancia de n_nodos

    //Se deben limpiar los arreglos

    for (int i = 0; i < n_nodos; i++){ //mientras i sea menor a la cantidad de nodos
        distancia[i] = infinito; //"Y voy a hacer copypaste de ese infinito un monton de veces", esto es hecho para que no se confunda y
        // entre en un ciclo vicioso donde toda distancia es mas corta
        visitados[i] = 0; //Ningun nodo ha sido visitado aun, por ello hay que ponerlos en 0
    }

    distancia[inicio] = 0; //La distancia del origen en origen pues es 0

    //Si se poseen 4 nodos, se deben hacer hasta 2 movimientos iniciando desde 1 (0), pues tras evaluarse la distancia y escogerse el menor entre 3
    //o sea probar 2 veces entre las 3 opciones, el ultimo no ocuparia una verificacion y solo se pondria de manera directa.
    //Por ello la cantidad de movimientos es siempre que sea menor a n_nodos - 1
    
    for(int movimiento = 0; movimiento < n_nodos - 1; movimiento++){
        
        //Se debe seleccionar el nodo mas cercano NO visitado
        int nodo_minimo = minimo(distancia, visitados);
        visitados[nodo_minimo] = 1;  //Una vez conseguido se marca visitado, por ejemplo, en la primera corrida, el origen se marcara como visitado.


        //Tras imprimir las distancias, revisa por un posible vecino al cual evaluar
        //Debido a que las posiciones son los identificadores del nodo, llega hasta n_nodos - 1

        for (int posible_vecino = 0; posible_vecino < n_nodos; posible_vecino++) { //recorrer todos los posibles_vecinos
            //Si NO ha sido visitado y ademas existe la distancia en la matriz de adyacencia
            if (visitados[posible_vecino] == 0 && matriz[nodo_minimo][posible_vecino] != 0) {
                
                int nuevo_nodo = distancia[nodo_minimo] + matriz[nodo_minimo][posible_vecino]; //la distancia del nodo_minimo + posible_vecino
                //Es decir, cuanta distancia tomara llegar al posible_vecino si paso primero por el nodo_minimo

                if (nuevo_nodo < distancia[posible_vecino]) {   //Se compara la distancia guardada en el espacio del posible vecino, o la distancia actual
                    distancia[posible_vecino] = nuevo_nodo; //y se cambia si es menor
                }
            }
        }

        // Mostrar estado
        printf("\nNodo a revisar: %d | Movimiento %d | Distancias pasando por el nodo: %d\n",inicio, movimiento + 1, nodo_minimo); //Se dice cual movimiento es
        printf("Distancias actuales: \n");    //Se dicen cuales distancias se poseen
        for (int i = 0; i < n_nodos; i++) { //Se recorre el arreglo de distancia
            printf("Nodo: %d", i);
            if (distancia[i] == infinito) printf(" | Distancia: INFINITAS unidades lineales \n");
            else printf(" | Distancia: %d unidades lineales\n", distancia[i]);
        }
        printf("\n");
    }

    //Se recorre cada espacio del arreglo e imprimen las distancias desde el nodo inicial
    printf("\nDistancias finales desde %d:\n", inicio);
    for (int i = 0; i < n_nodos; i++) { 
        printf("A nodo: %d | Distancia: %d\n", i, distancia[i]);
    }
}

/*
Funcion que implementa el recorrido BFS
Tenga en cuenta que los indices son usados como el numero o identificador de nodos

*/
void recorrido_por_achura(int matriz[n_nodos][n_nodos], int inicio) {
    int visitados[n_nodos];
    for (int i = 0; i < n_nodos; i++){ //POner todo en 0s, 0 -> no visitado , 1 -> visitado
        visitados[i] = 0;
    }

    int cola[n_nodos];      //La cola va a ser del tamannio de n_nodos
    int tamannio = 1; //tamannio de la cola
    cola[0] = inicio; //se inserta primer elemento
    visitados[inicio] = 1; //se marca como visitado

    printf("Recorrido por Anchura: ");

    //se agregan vecinos NO visitados
    for (int i = 0; i < tamannio; i++) { //se recorre toda la cola en busca de aquellos ya puestos
        int nodo_actual = cola[i]; // se toma el nodo segun el indice (que va en aumento hasta el final)
        printf("%d ", nodo_actual); //se imprimen aquellos nodos en la cola

        // agregar vecinos no visitados por nodo
        //se recorre cada posible vecino en la matriz_adyacencia
        for (int posible_vecino = 0; posible_vecino < n_nodos; posible_vecino++) {
            //Si NO ha sido visitado y ademas existe la distancia en la matriz de adyacencia
            if (visitados[posible_vecino] == 0 && matriz[nodo_actual][posible_vecino] != 0) {
                cola[tamannio] = posible_vecino; //cola en el espacio de tamannio (debido a que inicia desde 0 una lista estara bien)
                tamannio += 1; //se aumenta el tamannio
                visitados[posible_vecino] = 1; //se marca dicho espacio como visitado
            }
        }
    }

    printf("\n"); //un espacio para que no quede tan pegado
}

/*
Funcion para mostrar el laberinto de forma visual
E: matriz de adyacencia
S: representacion grafica en consola
*/
void mostrar_laberinto(int matriz[n_nodos][n_nodos]) {
    printf("\n");
    printf("========================================\n");
    printf("     VISUALIZACION DEL LABERINTO\n");
    printf("========================================\n\n");
    
    // Representacion visual tipo laberinto
    printf("     ");
    for (int i = 0; i < n_nodos * 6; i++) printf("="); //Se imprimen tantos = como nodos haya
    printf("\n");
    
    for (int i = 0; i < n_nodos; i++) { //Se recorre cada nodo
        printf("     ");
        for (int j = 0; j < n_nodos; j++) { //Se recorre cada posible vecino
            if (i == j) {
                printf("[ %d ]", i);
            } else if (matriz[i][j] != 0) { //Si existe la distancia en la matriz_adyacencia
                printf("--%2d-", matriz[i][j]);
            } else {
                printf("  X  ");
            }
            if (j < n_nodos - 1) printf(" "); //Se imprimen tantos espacios como nodos haya     
        }
        printf("\n");
    }
    printf("     ");
    printf("==============================\n\n");   
}

int main() {
    int matriz_adyacencia[n_nodos][n_nodos] = {
        {0, 10, 0, 30, 100},
        {10, 0, 50, 0, 0},
        {0, 50, 0, 20, 10},
        {30, 0, 20, 0, 60},
        {100, 0, 10, 60, 0}
    };

    int opcion;
    int nodo_inicio;
    
    do {
        printf("\n");
        printf("╔════════════════════════════════════════╗\n");
        printf("║     MENU - ALGORITMOS DE GRAFOS        ║\n");
        printf("╠════════════════════════════════════════╣\n");
        printf("║  1. Mostrar Laberinto                  ║\n");
        printf("║  2. Ejecutar Dijkstra                  ║\n");
        printf("║  3. Ejecutar BFS (Recorrido Anchura)   ║\n");
        printf("║  4. Salir                              ║\n");
        printf("╚════════════════════════════════════════╝\n");
        printf("\nSeleccione una opcion: ");
        scanf("%d", &opcion);
        
        switch(opcion) {
            case 1:
                mostrar_laberinto(matriz_adyacencia);
                break;
                
            case 2:
                printf("\nIngrese el nodo de inicio (0-%d): ", n_nodos - 1);
                scanf("%d", &nodo_inicio);
                if (nodo_inicio >= 0 && nodo_inicio < n_nodos) { //Se verifica que el nodo sea valido
                    printf("\n=== ALGORITMO DE DIJKSTRA ===\n");
                    dijkstra(matriz_adyacencia, nodo_inicio);
                } else {
                    printf("\nNodo invalido!\n");
                }
                break;
                
            case 3:
                printf("\nIngrese el nodo de inicio (0-%d): ", n_nodos - 1);
                scanf("%d", &nodo_inicio);
                if (nodo_inicio >= 0 && nodo_inicio < n_nodos) { //Se verifica que el nodo sea valido
                    printf("\n=== ALGORITMO BFS ===\n");
                    recorrido_por_achura(matriz_adyacencia, nodo_inicio); 
                } else {
                    printf("\nNodo invalido!\n");
                }
                break;
                
            case 4:
                printf("\nSaliendo del programa...\n");
                break;
                
            default:
                printf("\nOpcion invalida! Intente de nuevo.\n");
        }
        
    } while(opcion != 4);
    return 0;
}