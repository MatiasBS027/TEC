; Programa de prueba de función de producto interno
; de dos vectores enteros de tamaño n

includelib \Windows\System32\kernel32.dll

ExitProcess proto

.data
     n dw 10
     vector1   dw 1,2,3,4,5,9,26,53,589,79
     vector2   dw 1,2,3,4,82,8,4,7,9,4
     productoI dw ?

.code
main PROC
; algo
    sub  RSP,8               ; Se reserva espacio para el resultado (Producto Interno)
    xor  R8,R8
    mov  R8w,n
    push R8                  ; Se pone en el stack 'n' (primer parámetro)
    lea  R8, vector1
    push R8                  ; Se pone en la pila la dir. del primer vector
    lea  R8, vector2
    push R8                  ; Se pone en la pila la dir. del segundo vector
    call productovectorial
    pop  R8
    mov productoI, R8w
    call ExitProcess

main ENDP

; Módulos (Procedimientos o funciones)
productoVectorial PROC
; Stack Frame:
; rsp + 40: return value
; rsp + 32: n
; rsp + 24: dir. vector 1
; rsp + 16: dir. vector 2
; rsp + 8 : return address
; rsp     : i

    sub rsp,8             ; se reserva espacio para var. locales
    mov qword ptr [rsp],1 ; i <- 1
    mov R9,0              ; R9 acumula la suma de los productos
    mov RBX,[rsp+24]      ;RBX: base de vector 1
    mov RCX,[rsp+16]      ;RCX: base de vector 2
    mov RSI,0
    ciclo_suma_Prod_Int:
       xor RAX,RAX
       mov AX,[RBX+RSI]
       xor R8,R8
       mov R8w,[RCX+RSI]
       imul R8w
       add R9w,AX
       add qword ptr[rsp],1       ; i = i + 1
       mov RAX,[rsp+32]
       add RSI,2
       cmp [rsp],RAX
       jle ciclo_suma_Prod_Int

   mov [rsp+40],R9      ; Se actualiza el valor de retorno
   add RSP,8
   ret 24
productoVectorial ENDP

END