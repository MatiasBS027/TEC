; Programa para calcular el mínimo común múltiplo de dos enteros: a, b
; usando el teorema mcm(a,b) = a*b/MCD(a,b).
; Los módulos mcm y MCD se invocarán como funciones usando Stack Frame.

includelib \Windows\System32\kernel32.dll

ExitProcess proto

.data
	a dd 42     ; 42 = 0x2A
	b dd 56     ; 56 = 0x38
	c dd ?

.code
main PROC
	sub RSP,8        ; Preparando el stack frame
	xor R8,R8		 ; para llamar a mcm
	mov R8d,a
	push R8
	xor R8,R8
	mov R8d,b
	push R8
	call mcm

	pop R8          ; R8 debe contener mcm(a,b)
	mov c,R8d

	call ExitProcess ; Well-behaved ending

main ENDP

mcm PROC             ; Calculo del mínimo común múltiplo
                     ; RSP   : return address
					 ; RSP+8 : b
					 ; RSP+16: a
					 ; RSP+24: return value

	mov RAX,[RSP+16] ; RAX: parámetro a
	mov RCX,[RSP+8]  ; RCX: parámetro b
	imul RCX         ; RAX: a*b (temporal)
	mov R10,RAX      ; R10: a*b

	mov R8,[RSP+16] ; RAX: parámetro a  ; Se prepara el Stack Frame para llamar a MCD
	mov R9,[RSP+8]  ; RCX: parámetro b
	sub RSP,8
	push R8
	push R9
	call MCD
	pop R9         ;  R9: MCD(a,b)

	mov RAX,R10
	xor RDX,RDX
	idiv R9d       ;  EDX tiene el mcm(a,b) [Problema (!)]

	mov [RSP+24],RAX ; 
	ret 16
mcm ENDP

MCD PROC             ; Calculo del Máximo Común Divisor
					 ; usando el algoritmo de Euclides
                     ; RSP   : return address
					 ; RSP+8 : b
					 ; RSP+16: a
					 ; RSP+24: return value

	; a = qb + r
	mov RAX,[RSP+16]  ; RAX: a
	mov RBX,[RSP+8]   ; RBX: b
ciclo_Euclides:
	idiv RBX
	cmp RDX,0          ; El residuo queda en RDX (!)
	je  fin_Euclides
	mov RAX,RBX
	mov RBX,RDX
	xor RDX,RDX    ; Quitar para mostrar a los estudiantes el efecto colateral (!)
	jmp ciclo_Euclides
fin_Euclides:
	mov [RSP+24],RBX  ; DEPURACION: ¿rbx=6?
	ret 16
MCD ENDP

END