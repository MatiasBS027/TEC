        .global _start

        .data
vector: .hword  7, -4, 15, 2, -8, 3     @ Vector de enteros 16 bits
n:      .word   6                       @ Cantidad de elementos

        .text
_start:
        LDR     r1, =vector     @ r1 = dirección del vector
        LDR     r2, =n
        LDR     r2, [r2]        @ r2 = número de elementos (n)

        SUB     r2, r2, #1      @ límite externo: n-1
outer_loop:
        MOV     r3, #0          @ índice interno i = 0
        MOV     r6, r2          @ tope interno = n - 1 - pasada

inner_loop:
        @ Cargar vector[i] y vector[i+1]
        ADD     r4, r1, r3, LSL #1     @ dirección de vector[i]
        LDRSH    r7, [r4]

        ADD     r5, r4, #2             @ dirección de vector[i+1]
        LDRSH    r8, [r5]

        @ Comparar: si v[i] > v[i+1], intercambiar
        CMP     r7, r8
        BLE     no_swap                @ si r7 <= r8 → no intercambiar

        @ Intercambiar usando ejecución condicional
        STRH    r8, [r4]               @ v[i] = v[i+1]
        STRH    r7, [r5]               @ v[i+1] = v[i]

no_swap:
        ADD     r3, r3, #1             @ i++
        CMP     r3, r6
        BLT     inner_loop             @ while i < límite

        SUBS    r2, r2, #1             @ pasada siguiente
        BGT     outer_loop             @ mientras r2 > 0

end:
        B       end
