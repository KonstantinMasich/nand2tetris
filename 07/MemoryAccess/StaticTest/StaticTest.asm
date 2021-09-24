// Initialization
@256
D=A
@SP
M=D

// === push constant 111 ===
@111        // D = 111
D=A
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// === push constant 333 ===
@333        // D = 333
D=A
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// === push constant 888 ===
@888        // D = 888
D=A
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// === pop static 8 ===
@SP           // SP--
AM=M-1
D=M           // D = *SP
@some_f.8      
M=D

// === pop static 3 ===
@SP           // SP--
AM=M-1
D=M           // D = *SP
@some_f.3      
M=D

// === pop static 1 ===
@SP           // SP--
AM=M-1
D=M           // D = *SP
@some_f.1      
M=D

// === push static 3 ===
@some_f.3      // D = *label
D=M
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// === push static 1 ===
@some_f.1      // D = *label
D=M
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// ==========  sub  ==========
              // Pop the first operand into D:
@SP
AM=M-1
D=M           // D = stack[last]
              // Get the second operand without actually decrementing the stack:
@SP           // 
A=M-1         //
M=M-D      // sub operation

// === push static 8 ===
@some_f.8      // D = *label
D=M
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// ==========  add  ==========
              // Pop the first operand into D:
@SP
AM=M-1
D=M           // D = stack[last]
              // Get the second operand without actually decrementing the stack:
@SP           // 
A=M-1         //
M=M+D      // add operation



// Ending
(INFINITE_EXIT_LOOP)
    @INFINITE_EXIT_LOOP
    0;JMP