; Módulo de Exponenciación Modular
; Calcula: base^exponente mod modulo
; Usando el lema: (a*b) mod n = ((a mod n)*(b mod n)) mod n

includelib kernel32.lib
includelib ucrt.lib
includelib legacy_stdio_definitions.lib

EXTERN printf: PROC
EXTERN scanf: PROC

ExitProcess proto

.data
    ; Variables de prueba

    string db "Ingresa el numero primo al que deseas calcularle sus raices primitivas: ", 0
    short_format_string db "%hd", 0                       ;("%hd" lee un short de 16B)
    mensaje_raices db "Raices primitivas encontradas: ", 0
    espacio db " ", 0
    int_format_printf db "%d", 0
    vector_raices_primitivas dw 10913 dup(0)            
    ;Se colocan en 0 para la hora de impresion se finalice cuando se llega a un 0.


.code

main PROC
xor R9, R9
lea R9, vector_raices_primitivas
push R9
call calculo_raices_primitivas
sub rsp, 8		  ;Alineacion
call ExitProcess
add rsp, 8
main ENDP


; =========================================================
; MÓDULO: obtener_primo
; =========================================================
; Obtiene el numero primero que el usuario ingrese. 
; Número Primo máximo: 32 749
;
; Stack Frame:
; RSP + 48 : return value (número primo)
; RSP + 40 : return adress
; RSP +  8 : espacio para los argumentos de printf (shadow space)
; RSP      : alineación (para que complete con los 8B del return adress de printf y luego scanf)
; =========================================================
obtener_primo PROC
    sub RSP, 40        ; (Espacio para los argumentos de printf, shadow space) 32, (alineacion) 8
    lea RCX, string
    call printf
    lea RCX, short_format_string
    lea RDX, [RSP + 48]             ;Pasar la direccion [RSP + 48] (número primo) a scanf para que guarde el resultado
    call scanf
    add RSP, 40       ;Restaurando la pila
    ret 
obtener_primo ENDP

; =========================================================
; MÓDULO: imprimir_raices_primitivas
; =========================================================
; Imprime todas las raíces primitivas almacenadas en el vector
; Stack Frame:
; RSP + 48  : dir.vector_raices_primitivas
; RSP + 40  : return adress
; RSP +  8  : espacio para los argumentos de printf (shadow space)
; RSP      : alineación (para que complete con los 8B del return adress de printf)
; =========================================================
imprimir_raices_primitivas PROC
    sub RSP, 40                     ; (Espacio para los argumentos de printf, shadow space) 32, (alineacion) 8
    mov RBX, [RSP + 48]             ; RBX <- dir.vector_raices_primitivas
    xor RSI, RSI                    ; RSI = 0

    ; Imprimir mensaje inicial
    lea RCX, mensaje_raices
    call printf

ciclo_impresion:
    xor R8, R8
    mov R8w, [RBX + RSI*2]               ;R8w <- raiz primitiva en la posición RSI del vector (utiliza escala)
    cmp R8, 0                         ; Verificar si es 0 (fin del vector)
    je fin_impresion                   

    ; Imprimir la raíz primitiva
    lea RCX, int_format_printf        
    mov RDX, R8                       ; Segundo parámetro: la raíz primitiva a imprimir
    call printf

    ; Imprimir espacio
    lea RCX, espacio                  ; Imprimir espacio
    call printf

    inc RSI                           
    jmp ciclo_impresion
    
fin_impresion:
    add RSP, 40                       ; Restaurando la pila
    ret 8                             
imprimir_raices_primitivas ENDP


; =========================================================
; MÓDULO: calculo_raices_primitivas
; =========================================================
; Calcula las raices primitivas de un número primo dado y las almacena en un vector. 
; =========================================================
calculo_raices_primitivas PROC
    ; =========================================================
    ; Stack Frame:
    ; RSP + 32 : dir.vector_raices_primitivas
    ; RSP + 24 : return adress
    ; RSP + 16 : numero_primo
    ; RSP +  8 : alineación
    ; RSP      : return value obtener_primo (se elimina con el pop)
    ; =========================================================
    sub RSP, 24         ; (Variable local: numero_primo) 8, (Alineación) 8, (return value obtener_primo) 8
    call obtener_primo
    xor R10,R10
    pop R10          ; Se guarda el número primo en R10, Cambio en el stack frame: RSP : alineación
    mov [RSP + 8], R10  ;Guardar el numero primo en la variable local numero_primo
    add RSP, 8           ; Eliminar el espacio para la alineación, Cambio en el stack frame: RSP : numero_primo

    ;Inicializar variables para el ciclo de busqueda de raices primitivas y preparar el stack frame para el modulo de verificacion de raiz primitiva
    ; =========================================================
    ; Stack Frame:
    ; RSP + 24 : dir.vector_raices_primitivas
    ; RSP + 16 : return adress
    ; RSP + 8 : numero_primo
    ; RSP     : variable local base_actual
    ; =========================================================
    sub RSP, 8          ; (Variable local: base_actual), 8
    mov qword ptr [RSP], 2         ;Base inicial para buscar raices primitivas, base_actual = 2
    mov RSI, 0                     ; RSI = 0

ciclo_busqueda_raices_primitivas:
    xor R11, R11
    mov R11, [RSP + 8] ; Parámetro 1: módulo = numero_primo 
    xor R9, R9
    mov R9, R11
    dec R9               ; Parámetro 2: exponente_final = (numero_primo - 1) 
    xor R8, R8
    mov R8, [RSP]  ; Parámetro 3: base_actual
    sub RSP, 16          ;(alineación) 8,  (return value verificacion_raiz_primitiva), 8
    push R11
    push R9
    push R8
    call verificacion_raiz_primitiva

    ; =========================================================
    ; Stack Frame:
    ; RSP + 40 : dir.vector_raices_primitivas
    ; RSP + 32 : return adress
    ; RSP + 24 : numero_primo
    ; RSP + 16 : variable local base_actual
    ; RSP + 8  : alineación
    ; RSP      : return value verificacion_raiz_primitiva
    ; =========================================================
    pop R8              ; R8 contiene el resultado, Cambio en el stack frame: RSP : alineación
    add RSP, 8          ; Eliminar espacio para la alineación, Cambio en el stack frame: RSP : base_actual
    cmp R8, 1
    jne no_raiz_primitiva

    ;Guardar la raiz primitiva en el vector
    ; =========================================================
    ; Stack Frame:
    ; RSP + 24 : dir.vector_raices_primitivas
    ; RSP + 16 : return adress
    ; RSP + 8 : numero_primo
    ; RSP     : variable local base_actual
    ; =========================================================
    mov R8, [RSP]           ; R8 <- base_actual (raíz primitiva)
    mov RBX, [RSP + 24]         ; RBX <- dir.vector_raices_primitivas
    mov [RBX + RSI *2], R8w     ; dir.vector_raices_primitivas + correspondiente posición (se utiliza base índice escala) <- R8w (raíz primitiva)
    inc RSI

no_raiz_primitiva:
    add qword ptr [RSP], 1      ; base_actual = base_actual + 1
    mov R10, [RSP + 8]          ; R10 <- numero_primo
    cmp qword ptr [RSP], R10      ; cmp base_actual, numero_primo 
    jl ciclo_busqueda_raices_primitivas ; base_actual < numero_primo
    add RSP, 16                         ; Eliminar el espacio de las variables locales

    ;Imprimir las raices primitivas encontradas
    ; =========================================================
    ; Stack Frame:
    ; RSP + 8 : dir.vector_raices_primitivas
    ; RSP     : return adress
    ; =========================================================
    mov R9, [RSP + 8]                   ; R9 <- dir.vector_raices_primitivas

    ;No se requiere alineación pues ya está alineado
    push R9                             ; Parámetro: dir.vector_raices_primitivas
    call imprimir_raices_primitivas

    ret 8
calculo_raices_primitivas ENDP


; =========================================================
; MÓDULO: verificacion_raiz_primitiva
; =========================================================
; Verifica si un número dado (base) es raiz primitiva de un numero primo dado 
; Retorna 1 si el número es una raíz primitiva, 0 sino.
; Stack Frame:
; RSP + 40 : return value
; RSP + 32 : numero_primo
; RSP + 24 : exponente_final
; RSP + 16 : base
; RSP +  8 : return adress
; RSP      : exponente_actual
; =========================================================
verificacion_raiz_primitiva PROC
    sub RSP, 8          ; (variable local: exponente_actual) 8
    mov qword ptr [RSP], 2   ; exponente_actual = 2

ciclo_verificacion_potencias:
    ;Preparar el stack frame para el segundo modulo
    mov R11, [RSP + 32]      ; R11 <- numero_primo
    mov R12, [RSP]           ; R12 <- exponente_actual
    mov R13, [RSP + 16]      ; R13 <- base
    sub RSP, 16          ; (alineación) 8, (return value exponenciacion_modular) 8
    push R11             ; Parámetro 1: módulo = numero_primo
    push R12             ; Parámetro 2: exponente_actual 
    push R13             ; Parámetro 3: base
    call exponenciacion_modular

    pop R8              ; R8 contiene el resultado, Cambio en el stack frame: RSP : alineación
    add RSP, 8          ; Eliminar la alineación, Cambio en el stack frame: RSP : exponente_actual
    cmp R8, qword ptr [RSP + 16]    ; cmp resultado exponenciación modular, base 
    je fin_ciclo_no_raiz_primitiva  ; resultado exponenciación modular = base 

    add qword ptr [RSP], 1          ; exponente_actual = exponente_actual + 1
    mov R12, [RSP]                  ; R12 <- exponente_actual
    cmp R12, qword ptr [RSP + 24]   ; cmp exponente_actual, exponente_final          
    jle ciclo_verificacion_potencias    ; exponente_actual <= exponente_final
    
    ;Es raiz primitiva del número primo
    mov qword ptr [RSP + 40], 1         ; return value = 1
    add RSP, 8                          ; Eliminar variables locales
    ret 24

fin_ciclo_no_raiz_primitiva:
    ;No es raiz primitiva del número primo
    mov qword ptr [RSP + 40], 0         ; return value = 0
    add RSP, 8                          ; Eliminar variables locales
    ret 24
verificacion_raiz_primitiva ENDP

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
    xor RCX, RCX
    ; Casos especiales
    mov RCX, [RSP+16]   ; RCX = exponente
    cmp RCX, 0
    je exp_cero         ; Si exponente = 0, resultado = 1
    
    ; Inicializar variables
    xor RAX, RAX
    mov RAX, 1          ; RAX = resultado acumulado (empieza en 1)
    xor RBX, RBX
    mov RBX, [RSP+8]    ; RBX = base
    xor R9, R9
    mov R9, [RSP+24]    ; R9 = módulo
    ; RCX ya tiene el exponente
    
ciclo_multiplicacion:
    ; Multiplicar resultado por base 
    ; resultado = resultado * base
    imul RBX            ; RAX = RAX * RBX
   
    ; Aplicar módulo 
    ; Aquí aplicamos: (a*b) mod n
    xor RDX, RDX        ; Limpiar RDX antes de dividir
    div R9              ; RAX = RAX  / módulo, RDX = RAX mod módulo (sin signo)
    mov RAX, RDX        ; RAX = residuo (resultado mod módulo)
    
    ;  Verificar 
    dec RCX             ; exponente = exponente - 1
    cmp RCX, 0
    jg ciclo_multiplicacion  ; Si exponente > 0, continuar
    
    ; Guardar resultado y retornar 
fin_exponenciacion:
    mov [RSP+32], RAX   ; Guardar resultado en stack frame
    ret 24              ; Limpiar 3 parámetros (8 bytes cada uno)
    
exp_cero:
    ; Caso especial: cualquier número^0 = 1
    mov qword ptr [RSP+32], 1
    ret 24
exponenciacion_modular ENDP

END