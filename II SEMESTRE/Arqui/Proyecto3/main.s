.global _start
_start:

@ PARTE 1 - INICIALIZACIÓN Y ESTRUCTURA PRINCIPAL
@ Configurar datos y función main

    .data                   @ Sección de datos
    .align 2                @ Alinear a 4 bytes

@ Vector a ordenar: 8 números enteros de 16 bits (con signo)
vector:
    .hword  45, -12, 78, -3, 23, 89, -56, 12

@ Tamaño del vector 
vector_size:
    .word   8               @ 8 elementos

    .text                   @ Sección de código
    .global _start          @ Punto de entrada del programa

@ FUNCIÓN PRINCIPAL
_start:
    @ Preparar parámetros para ordenar
    LDR     R0, =vector         @ R0 = dirección donde está el vector
    LDR     R1, =vector_size    @ R1 = dirección de vector_size
    LDR     R1, [R1]            @ R1 = 8 (leer el valor)
    
    @ Llamar a la función que ordena 
    BL      bubble_sort
    
    @ Terminar el programa
    MOV     R7, #1              @ Salir
    MOV     R0, #0              @ Código de salida 0 (éxito)
    SWI     0                   @ Llamada al sistema

