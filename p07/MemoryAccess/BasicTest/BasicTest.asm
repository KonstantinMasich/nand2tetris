
        @10
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @0
        D=A
        @LCL
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @21
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @22
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @2
        D=A
        @ARG
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @1
        D=A
        @ARG
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @36
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @6
        D=A
        @THIS
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @42
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @45
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @5
        D=A
        @THAT
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @2
        D=A
        @THAT
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        
        @510
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        @11
        M=D
        
        @0
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @5
        D=A
        @THAT
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

        @6
        D=A
        @THIS
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @6
        D=A
        @THIS
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
        AM=M-1
        D=M
        A=A-1
        M=M-D

        @11
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

        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
