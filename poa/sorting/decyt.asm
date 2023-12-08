
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV [3000H],25H
MOV [3001H],15H
MOV [3002H],45H
MOV [3003H],55H

MOV SI,3000H
MOV DX,3001H
MOV CH,04H

Back1:MOV CL,CH
      MOV DI,DX

Back:MOV AL,[SI]
     MOV BL,[DI]
     CMP AL,BL
     JNC Next
     MOV [SI],BL
     MOV [DI],AL 
     
Next:INC DI
     DEC CL
     JNZ Back
     
     INC SI
     INC DX
     DEC CH
     JNZ Back1

HLT
RET




