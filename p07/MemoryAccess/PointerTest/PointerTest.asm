
        @3030
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        @3
        M=D
        
        @3040
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        @4
        M=D
        
        @32
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @2
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
        
        @46
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @6
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
        
        @3
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @4
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

        @2
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
        M=M-D

        @6
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

        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
