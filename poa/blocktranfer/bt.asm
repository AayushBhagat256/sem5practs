; multi-segment executable file template.

data segment
    ; add your data here!
    n1 db 45h,32h,36h
ends

extra segment ;chnage here
    n2 db ?
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax 
    ; add this line
    mov ax,extra
    mov es, ax

    ; add your code here
            
    lea si, n1
    lea di, n2 
    
    mov cl , 04h
    
    l1:
    mov ax,ds:[si]
    mov es:[di],ax
    
    inc si
    inc di
    dec cl
    jnz l1  
ends

end start ; set entry point and stop the assembler.
