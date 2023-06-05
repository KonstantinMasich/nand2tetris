
    (SimpleFunction.test)
        @SP
        A=M
    
        M=0
        A=A+1

        M=0
        A=A+1

        @2
        D=A
        @SP
        M=M+D

        @0
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @1
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M+D

        @SP
        A=M-1
        M=!M

        @0
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M+D

        @1
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M-D

        @LCL
        D=M
        @13
        M=D
        @5
        D=D-A
        A=D
        D=M
        @14
        M=D
        @SP
        AM=M-1
        D=M
        @ARG
        A=M
        M=D
        @ARG
        D=M+1
        @SP
        M=D
        @13
        AM=M-1
        D=M
        @THAT
        M=D
        @13
        AM=M-1
        D=M
        @THIS
        M=D
        @13
        AM=M-1
        D=M
        @ARG
        M=D
        @13
        AM=M-1
        D=M
        @LCL
        M=D
        @14
        A=M
        0;JMP

        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
