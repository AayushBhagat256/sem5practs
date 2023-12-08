
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [3000H], 25H
MOV [3001H], 15H
MOV [3002H], 45H
MOV [3003H], 55H

MOV CH, 04H
MOV SI, 3000H
MOV DX, 3001H

BACK1:
  MOV DI, DX
  MOV CL, CH

BACK:
  MOV AL, [SI]
  MOV BL, [DI]
  CMP AL, BL
  JC NEXT  ; Change JNC to JC for ascending order
  MOV [SI], BL
  MOV [DI], AL

NEXT:
  INC DI
  DEC CL
  JNZ BACK

  INC SI
  INC DX
  DEC CH
  JNZ BACK1

ret





