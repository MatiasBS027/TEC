;Programa para calcular el minimo comun multiplo (MCM) de dos numeros: a, b
;Usando el teorema: MCM(a,b) = (a*b)/MCD(a,b)
;Los modulos mcm y MCD se invocaran como funciones usando Stack Frame 

includelib \Windows\System32\Kernel32.lib

ExitProcess proto

; Declaración de datos
.data
a dd 69    ; 69 = 0x45
b dd 28    ; 28 = 0x1C
c dd ?     

; Código principal
.code
main PROC
    sub RSP, 8         ; Preparar stack frame
    xor R8, R8         ; para llamar a MCM
    mov R8d, a
    push R8
    xor R8, R8
    mov R8d, b
    push R8
    call mcm    


    pop R8
    mov c, R8d         ; R8 deeb contener mcm(a,b)

    call ExitProcess
main ENDP

; Procedimiento para calcular MCM
mcm PROC
                       ;Calculo del minimo comun multiplo
                       ;RSP: return address
                       ;RSP+8: parametro B
                       ;RSP+16: parametro A
                       ;RSP+24: Return value (MCM)
    mov RAX, [RSP+16]  ;RAX: Parámetro A
    mov RCX, [RSP+8]   ;RCX: Parámetro B
    imul RCX           ;RAX = A*B
    mov R10,RAX	       ;Guardar A*B en R10
    
    mov R8, [RSP+16]   ;RAX parametro A ; Se prepara el stack frame para llamar a MCD   
    mov R9, [RSP+8]    ;RCX parametro B
    sub RSP, 8         
    push R8
    push R9
    call MCD
    pop R9            ; 

    mov RAX, R10      ;RAX = A*B
    xor RDX, RDX     ;Limpiar RDX antes de la division
    idiv R9d           ;RAX = (A*B)/MCD(A,B)


    mov [RSP+24], RAX  ; Guardar resultado en la pila
    ret 16
mcm ENDP

MCD PROC
    ; Calculo del Máximo Común Divisor
    ; usando el algoritmo de Euclides
    ; RSP      : return address
    ; RSP+8    : b
    ; RSP+16   : a
    ; RSP+24   : return value

    ; a = q*b + r
    mov RAX, [RSP+16]    ; RAX : a
    mov RBX, [RSP+8]     ; RBX : b

ciclo_Euclides:
    idiv RBX             ; cociente en RAX, residuo en RDX
    cmp RDX, 0           ; ¿residuo es cero?
    je fin_Euclides      ; si sí, fin del ciclo
    mov RAX, RBX         ; a = b
    mov RBX, RDX         ; b = r
    xor RDX, RDX           ; limpiar RDX (no obligatorio)
    jmp ciclo_Euclides

fin_Euclides:
    mov [RSP+24], RBX    ; guardar resultado (MCD)
    ret 16
MCD ENDP

end