; Módulo de Exponenciación Modular
; Calcula: base^exponente mod modulo
; Usando el lema: (a*b) mod n = ((a mod n)*(b mod n)) mod n

includelib kernel32.lib
ExitProcess proto

.data
    ; Variables de prueba
    test_base dd 9
    test_exp dd 2
    test_mod dd 11
    resultado dd ?

.code
main PROC
    sub RSP, 8          ; Alinear stack (estilo del profe)
    
    ; PRUEBA 
    ; 3^5 mod 7 (debería dar 5)
    
    sub RSP, 8          ; Reservar espacio para el resultado
    
    ; Los parámetros se ponen en orden INVERSO porque el último push queda más cerca de RSP
    
    xor R8, R8
    mov R8d, test_mod
    push R8             ; Parámetro 3: módulo = 7 (va al fondo)
    
    xor R8, R8
    mov R8d, test_exp
    push R8             ; Parámetro 2: exponente = 5 (va en medio)
    
    xor R8, R8
    mov R8d, test_base
    push R8             ; Parámetro 1: base = 3 (queda arriba)
    
    call exponenciacion_modular
    
    pop R8              ; R8 contiene el resultado
    mov resultado, R8d  ; Guardar resultado (debería ser 5)
    
    xor RCX, RCX
    call ExitProcess
main ENDP

; =========================================================
; MÓDULO: exponenciacion_modular
; =========================================================
; Calcula: base^exponente mod modulo
;
; Stack Frame:
; RSP + 32: valor de retorno (resultado)
; RSP + 24: módulo
; RSP + 16: exponente
; RSP + 8 : base
; RSP     : return address
; =========================================================
exponenciacion_modular PROC
    ; Casos especiales
    mov RCX, [RSP+16]   ; RCX = exponente
    cmp RCX, 0
    je exp_cero         ; Si exponente = 0, resultado = 1
    
    ; Inicializar variables 
    mov RAX, 1          ; RAX = resultado acumulado (empieza en 1)
    mov RBX, [RSP+8]    ; RBX = base
    mov R9, [RSP+24]    ; R9 = módulo
    ; RCX ya tiene el exponente
    
ciclo_multiplicacion:
    ; Multiplicar resultado por base 
    ; resultado = resultado * base
    imul RBX            ; RAX = RAX * RBX
   
    ; Aplicar módulo 
    ; Aquí aplicamos: (a*b) mod n
    xor RDX, RDX        ; Limpiar RDX antes de dividir
    div R9              ; RAX = RAX / módulo, RDX = RAX mod módulo (sin signo)
    mov RAX, RDX        ; RAX = residuo (resultado mod módulo)
    
    ;  Verificar 
    dec RCX             ; exponente = exponente - 1
    cmp RCX, 0
    jg ciclo_multiplicacion  ; Si exponente > 0, continuar
    
    ; Guardar resultado y retornar 
fin_exponenciacion:
    mov [RSP+32], RAX   ; Guardar resultado en stack frame
    ret 24              ; Limpiar 3 parámetros (8 bytes c/u)
    
exp_cero:
    ; Caso especial: cualquier número^0 = 1
    mov qword ptr [RSP+32], 1
    ret 24

exponenciacion_modular ENDP

END