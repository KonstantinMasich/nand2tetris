
// ========================================================== //
//                   FILE PointerTest
// ========================================================== //

// push constant 3030
            @3030
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 0
            @SP
            AM=M-1
            D=M
            @3
            M=D
// push constant 3040
            @3040
            D=A
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
// push constant 32
            @32
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THIS 2
            @2
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
// push constant 46
            @46
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop THAT 6
            @6
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
// push pointer 0
            @3
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
// push pointer 1
            @4
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
// push THIS 2
            @2
            D=A
            @THIS
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
// push THAT 6
            @6
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


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE PointerTest
// ========================================================== //
