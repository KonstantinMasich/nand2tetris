// ==========  function SimpleFunction.SimpleFunction.test 2 ==========
(SimpleFunction$SimpleFunction.test)
@2
D=A
@i_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS
M=D+1
(helper_loop_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS)
    @i_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS
    MD=M-1
    @helper_loop_end_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS
        D;JEQ
    @SP
    A=M
    M=0
    @SP
    M=M+1
    @helper_loop_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS
        0;JMP
(helper_loop_end_DKZBEpYCdBODWFVuuZwcqLiIGPyYqObS)

// === push LCL 0 ===
@0        // Go to RAM[ LCL[idx] ]
D=A           // D = 0
@LCL        //
A=M+D         //
D=M           // D = RAM[ LCL[idx] ]
@SP           // *SP = D
A=M
M=D
@SP           // SP++
M=M+1

// === push LCL 1 ===
@1        // Go to RAM[ LCL[idx] ]
D=A           // D = 1
@LCL        //
A=M+D         //
D=M           // D = RAM[ LCL[idx] ]
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

// ==========  not  ==========
         // Change the stack[last] directly:
@SP      // *SP = !SP
A=M-1
M=!M

// === push ARG 0 ===
@0        // Go to RAM[ ARG[idx] ]
D=A           // D = 0
@ARG        //
A=M+D         //
D=M           // D = RAM[ ARG[idx] ]
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

// === push ARG 1 ===
@1        // Go to RAM[ ARG[idx] ]
D=A           // D = 1
@ARG        //
A=M+D         //
D=M           // D = RAM[ ARG[idx] ]
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



// Ending
(INFINITE_EXIT_LOOP)
    @INFINITE_EXIT_LOOP
    0;JMP