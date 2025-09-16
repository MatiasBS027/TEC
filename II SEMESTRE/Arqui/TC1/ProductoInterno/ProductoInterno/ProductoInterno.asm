;  Programa de prueba de funcion de producto interno de dos vectores


include \Windows\System32\kernel32.dll

ExitProcess proto

.data
    n dw 10
    vector1   dw 3,1,4,1,5,9,26,53,589,79
    vector2   dw 2,71,82,81,82,8,4,7,9,4
    productoI dw ?

.code
main PROC
; algo
    sub RSP,8
    xor R8,R8
    mov R8w,n
    push R8 ; Se pone en el stack 'n' (Primer paremetro)
    lea R8, vector1
    push R8 ; Se pone en la pila la dirección del vector1 (Segundo parametro)
    lea R8, vector2
    push R8 ; Se pone en la pila la dirección del vector2 (Tercer parametro)
    call productovectorial
    pop R8
    mov productoI, R8w
    call ExitProcess

main ENDP

; Módulos (Procedimientos o funciones)
productovectorial PROC
;Stack Frame:
;rsp +40: return value
;rsp +32:n
;rsp +24:dir. vector1
;rsp +16: dir. vector2
;rsp +8: return address
;rsp: i
    
    sub RSP,8
    mov qword ptr[rsp], 1  ; i <-- 1
    mov R9,0 ; R9 acumula la suma del producto escalar
    mov RBX, [rsp + 24] ; RBX base de vector1
    mov RCX [rsp + 16]  ; RCX base de vector2
    mov  RSI, 0
    ciclo_suma_Prod_Int:
        xor RAX, RAX
        mov AX, [RBX + RSI]
        xor R8, R8
        mov R8W, [RCX + RS1]
        imul R8w
        add R9w, AX
        add qword ptr[rsp], 1 ; i++
        mov RAX, [rsp + 32]
        add RSI,2 ; Desplazamiento de 2 bytes (tamaño de un word)
        cmp [rsp],RAX
        jle ciclo_suma_Prod_In

    mov [rsp+40], R9 ; Devolver el resultado en el stack
    add RSP,8
    ret 24
productovectorial ENDP
END