
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
        @4
        M=D
        
        @0
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @0
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
        
        @1
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @1
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
        
        @0
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @2
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
        
        (Sys.init$MAIN_LOOP_START)
    
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
            @Sys.init$COMPUTE_ELEMENT
                D;JNE
    
            @Sys.init$END_PROGRAM
                0;JMP
    
        (Sys.init$COMPUTE_ELEMENT)
    
        @0
        D=A
        @THAT
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @1
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
        
        @4
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
        M=M+D

        @SP
        AM=M-1
        D=M
        @4
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
        
            @Sys.init$MAIN_LOOP_START
                0;JMP
    
        (Sys.init$END_PROGRAM)
    
        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
