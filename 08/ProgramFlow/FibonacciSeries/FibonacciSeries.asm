
// ========================================================== //
//                   FILE FibonacciSeries
// ========================================================== //
// push ARG 1
            @1
            D=A
            @ARG
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
// push constant 0
            @0
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THAT 0
            @0
            D=A
            @THAT
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push constant 1
            @1
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THAT 1
            @1
            D=A
            @THAT
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push ARG 0
            @0
            D=A
            @ARG
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 2
            @2
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// sub
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
// pop ARG 0
            @0
            D=A
            @ARG
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// label MAIN_LOOP_START
            (Sys.init$MAIN_LOOP_START)
// push ARG 0
            @0
            D=A
            @ARG
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// if-goto COMPUTE_ELEMENT
            @SP
            AM=M-1
            D=M
            @Sys.init$COMPUTE_ELEMENT
                D;JNE
// goto END_PROGRAM
            @Sys.init$END_PROGRAM
                0;JMP
// label COMPUTE_ELEMENT
            (Sys.init$COMPUTE_ELEMENT)
// push THAT 0
            @0
            D=A
            @THAT
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push THAT 1
            @1
            D=A
            @THAT
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
// pop THAT 2
            @2
            D=A
            @THAT
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push pointer 1
            @4
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 1
            @1
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
// push ARG 0
            @0
            D=A
            @ARG
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 1
            @1
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// sub
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
// pop ARG 0
            @0
            D=A
            @ARG
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// goto MAIN_LOOP_START
            @Sys.init$MAIN_LOOP_START
                0;JMP
// label END_PROGRAM
            (Sys.init$END_PROGRAM)


// ========================================================== //
//                    END OF FILE FibonacciSeries
// ========================================================== //

    (Sys.init$WHILE)
        @Sys.init$WHILE
                0;JMP
