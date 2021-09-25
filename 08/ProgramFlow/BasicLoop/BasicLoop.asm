
// ========================================================== //
//                   FILE BasicLoop
// ========================================================== //

// push constant 0
            @0
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop LCL 0
            @0
            D=A
            @LCL
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// label LOOP_START
            (BasicLoop__main__LOOP_START)
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
// push LCL 0
            @0
            D=A
            @LCL
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
// pop LCL 0
            @0
            D=A
            @LCL
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
// if-goto LOOP_START
            @SP
            AM=M-1
            D=M
            @BasicLoop__main__LOOP_START
                D;JNE
// push LCL 0
            @0
            D=A
            @LCL
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE BasicLoop
// ========================================================== //
