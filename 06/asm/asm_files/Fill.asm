(START)
// Check whether a key was pressed:
@KBD
D=M
@WHITE
    D;JEQ
@BLACK
    0;JMP

////////////////////////  PIXEL COLOR VALUE  //////////////////////// 
// Color value of the pixel will be stored at register R0
(BLACK)
    @R0
    M=-1
    @PAINT
        0;JMP
(WHITE)
    @R0
    M=0
    @PAINT
        0;JMP


///////////////////////////  PAINT METHOD  //////////////////////////
(PAINT)
    // Initialize i to 8190:
    @8190
    D=A
    @i
    M=D
    // Initialize pixel to 16384 (SCREEN[0])
    @SCREEN
    D=A
    @pixel
    M=D
    (LOOP)
        // 1. Paint a pixel with the value stored in R0:
        @R0
        D=M
        @pixel
        A=M
        M=D
        // 2. Do pixel++ 
        @pixel
        M=M+1
        // 3. Do i--
        @i
        M=M-1
        // 4. Check of termination condition:
        D=M
        @START
            D;JEQ
        @LOOP
            D;JMP
