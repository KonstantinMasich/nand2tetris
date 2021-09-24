
// ========================================================== //
//                   FILE BasicTest.vm
// ========================================================== //

// push constant 10
            @10
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
// push constant 21
            @21
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 22
            @22
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop ARG 2
            @2
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
// pop ARG 1
            @1
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
// push constant 36
            @36
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THIS 6
            @6
            D=A
            @THIS
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push constant 42
            @42
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 45
            @45
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THAT 5
            @5
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
// push constant 510
            @510
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop temp 6
            @SP
            AM=M-1
            D=M
            @11
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
// push THAT 5
            @5
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
// sub
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
// push THIS 6
            @6
            D=A
            @THIS
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push THIS 6
            @6
            D=A
            @THIS
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
// sub
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
// push temp 6
            @11
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


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE BasicTest.vm
// ========================================================== //
