;Programa para calcular el minimo comun multiplo (MCM) de dos numeros: a, b
;Usando el teorema: MCM(a,b) = (a*b)/MCD(a,b)
;Los modulos mcm y MCD se invocaran como funciones usando Stack Frame 

includelib \Windows\System32\Kernel32.lib

ExitProcess proto

; Declaración de datos
.data
a DD 69    ; 69 = 0x45
b DD 28    ; 28 = 0x1C
c DD ?     

; Código principal
.code
main PROC
    sub RSP, 8         ; Preparar stack frame
    xor R8, R8         ; para llamar a MCM
    mov R8D, a
    push R8
    xor R8, R8
    mov R8d, b
    push R8
    call MCM    


    pop R8
    mov c, R8d         ; R8 deeb contener mcm(a,b)

    call ExitProcess
main ENDP

; Procedimiento para calcular MCM
MCM PROC
                       ;Calculo del minimo comun multiplo
                       ;RSP: return address
                       ;RSP+8: parametro B
                       ;RSP+16: parametro A
                       ;RSP+24: Return value (MCM)
    mov RAX, [RSP+16]  ;RAX: Parámetro A
    mov RCX, [RSP+24]  ;RCX: Parámetro B
    imul RCX           ;RAX = A*B
    
    mov R8, [RSP+16]
    mov R9, [RSP+8]
    sub RSP, 8         ;Preparar stack frame para llamar a MCD
    push R8
    push R9
    call MCD
    pop R9

    idiv R9           ;RAX = (A*B)/MCD(A,B)
    xor RAX, RAX      ;Limpiar RDX despues de la division
    mov EAX, EAX      ;RAX = MCM(A,B)

    mov [RSP+24], RAX  ; Guardar resultado en la pila
    ret 16
MCM ENDP

end