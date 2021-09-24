
// ========================================================== //
//                   FILE PointerTest.vm
// ========================================================== //

// push constant 3030
            @3030
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
// pop pointer 0
            @SP
            AM=M-1
            D=M
            @3
            M=D
            @11111
// push constant 3040
            @3040
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
            @11111
// push constant 32
            @32
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
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
            @11111
// push constant 46
            @46
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
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
            @11111
// push pointer 0
            @3
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
// push pointer 1
            @4
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
            @11111
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
            @11111
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
            @11111
// sub
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M-D
            @11111
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
            @11111
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
            @11111


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE PointerTest.vm
// ========================================================== //
