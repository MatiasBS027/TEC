; =========================================================
;  Producto interno de dos vectores de 6 elementos (float)
; =========================================================

includelib kernel32.lib
ExitProcess proto

.data
    ;datos para prueba
    ; Vectores (A y B): 6 elementos + 2 de padding para alineación
    
    align 16
    vectorA real4 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 0.0
    align 16
    vectorB real4 2.0, 1.0, 0.5, 2.0, 2.5, 0.5, 0.0, 0.0
   
   ; Vector C: Almacena resultados intermedios de multiplicación
    align 16
    vectorC real4 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    
    resultado real4 0.0 ; Variable para el resultado final del producto interno

.code
main PROC
    sub rsp, 32                   ; Reservar  espacio
    and rsp, 0FFFFFFFFFFFFFFF0h   ; Forzar alineacion 16 bytes

    ; =========================================================
    ; Etapa 1: multiplicacion elemento por elemento
    ; =========================================================

    ; bloque 1: Primeros 4 elementos 
    vmovups xmm0, xmmword ptr [vectorA]     ; XMM0 = [a1, a2, a3, a4] = [1.0, 2.0, 3.0, 4.0]
    vmovups xmm1, xmmword ptr [vectorB]     ; XMM1 = [b1, b2, b3, b4] = [2.0, 1.0, 0.5, 1.5]
    vmulps  xmm2, xmm0, xmm1                ; Multiplicación paralela: 
                                            ; XMM2 = [2.0, 2.0, 1.5, 6.0]
    vmovups xmmword ptr [vectorC], xmm2     ; Guardar primeros 4 productos en vectorC[0-3]

  
    ; bloque 2: Últimos 2 elementos
    vmovups xmm3, xmmword ptr [vectorA + 16]    ; XMM3 = [a5, a6, 0, 0] = [5.0, 6.0, 0.0, 0.0]
    vmovups xmm4, xmmword ptr [vectorB + 16]    ; XMM4 = [b5, b6, 0, 0] = [2.5, 0.5, 0.0, 0.0]
    vmulps  xmm5, xmm3, xmm4                    ; Multiplicación paralela:
                                                ; XMM5 = [12.5, 3.0, 0.0, 0.0]

    ; Extraer y guardar solo los elementos 5 y 6 
    vextractps dword ptr [vectorC + 16], xmm5, 0  ; vectorC[4] = 12.5
    vextractps dword ptr [vectorC + 20], xmm5, 1  ; vectorC[5] = 3.0

    
    ; =========================================================
    ; Etapa 2: sumar los productos (producto interno)
    ; =========================================================
    
    ; Cargar todos los productos para la suma 
    vmovups xmm0, xmmword ptr [vectorC]      ; XMM0 = [2.0, 2.0, 1.5, 6.0]
    vmovups xmm1, xmmword ptr [vectorC + 16] ; XMM1 = [12.5, 3.0, 0.0, 0.0]
    
    ; Sumar todos los productos 
    vaddps xmm0, xmm0, xmm1                  ; Suma paralela:
                                             ; XMM0 = [14.5, 5.0, 1.5, 6.0]
    
    ; Reducción horizontal - Primera etapa
    vhaddps xmm0, xmm0, xmm0                 ; Suma horizontal:
                                             ; [14.5+5.0, 1.5+6.0, 14.5+5.0, 1.5+6.0]
                                             ; XMM0 = [19.5, 7.5, 19.5, 7.5]
    
    ; Reducción horizontal - Segunda etapa 
    vhaddps xmm0, xmm0, xmm0                 ; Suma horizontal:
                                             ; [19.5+7.5, 19.5+7.5, 19.5+7.5, 19.5+7.5]
                                             ; XMM0 = [27.0, 27.0, 27.0, 27.0]
    
    ; Guardar resultado final
    vmovss resultado, xmm0                   ; Guarda solo el primer elemento (27.0)         

    ; === verificar resultado usando debugger  ========================
    ; El resultado debe ser: 
    ; 1.0*2.0 + 2.0*1.0 + 3.0*0.5 + 4.0*1.5 + 5.0*2.5 + 6.0*0.5 = 27.0
    ;==================================================================
    
    ; limpieza y salida
    add     rsp, 32
    xor     ecx, ecx
    call    ExitProcess

main ENDP
END