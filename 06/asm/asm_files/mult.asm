@3
D=A
@R0
M=D
@5
D=A
@R1
M=D

// 1. Set iterator to R1 value:
// i = R1
@R1
D=M
@i
M=D

// 2. Loop:
(LOOP)
    @R0
    D=M
    @R2
    M=D+M
    // Iterate and check loop termination condition:
    @i
    M=M-1
    D=M
    @CONT
        D;JEQ
    @LOOP
        0;JMP

(CONT)
// Clean up and terminate:
@R0
M=0
@R1
M=0
@R2
M=0
@i
M=0

(END)
    @END
    0;JMP
