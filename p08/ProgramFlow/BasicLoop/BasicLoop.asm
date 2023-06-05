
        @0
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
        
        (Sys.init$LOOP_START)
    
        @0
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
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
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M+D

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
        
        @0
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @1
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M-D

        @0
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
            @Sys.init$LOOP_START
                D;JNE
    
        @0
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
