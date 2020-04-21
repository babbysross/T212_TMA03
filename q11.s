@ q11.s
@ Assembly program to calculate taxi fare, for T212 TMA 03 Q11a
@ Temporary storage in address 30
@ Final result in address 32

mov [32],3  @ Place base fare of 3 in address 32
in          @ Input prevailing rate
mov [30],A  @ Store prevailing rate in address 30
in          @ Input distance travelled
mul [30]    @ Multiply value in address 30 by distance travelled in accumulator
mov [30],A  @ Move total to address 30
add A,[32]  @ Add total to base fare in address 32
mov [32],A  @ Move final result to address 32
out         @ Output the final result, still stored in the accumulator