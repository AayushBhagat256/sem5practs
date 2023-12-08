; multi-segment executable file template.

fact macro f
    mov ax,01h
    up:
    mul f
    dec f
    jnz up
endm

data segment
    ; add your data here!
    num db 05h
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
   

    ; add your code here
    ;lea si , num
    mov ax,01h
    fact num       
    
ends

end start ; set entry point and stop the assembler.
