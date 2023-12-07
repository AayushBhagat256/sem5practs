
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt


MOV AX,0F3Fh
MOV BX,0A2Ch
MOV CL,00h

ADD AX,BX

JNC jump
INC CL

jump:
MOV [1004h],AX
MOV [1006H],CL
HLT

ret




