
// -----------------------------
// --     BOOTSTRAP CODE      --
// -----------------------------
        @256
        D=A
        @SP
        M=D
        
        @Sys.init_ret_addr__MAIN
        D=A
        @SP
        A=M
        M=D
        @LCL
        D=M
        @SP
        AM=M+1
        M=D
        @ARG
        D=M
        @SP
        AM=M+1
        M=D
        @THIS
        D=M
        @SP
        AM=M+1
        M=D
        @THAT
        D=M
        @SP
        AM=M+1
        M=D
        @0
        D=A
        @5
        D=A+D
        @SP
        M=M+1
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Sys.init
            0;JMP
        (Sys.init_ret_addr__MAIN)

// -----------------------------
// --  END OF BOOTSTRAP CODE  --
// -----------------------------

    (Sys.init)
        @SP
        A=M
    
        @0
        D=A
        @SP
        M=M+D

        @4000
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
        
        @5000
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
        
        @Sys.main_ret_addr__2
        D=A
        @SP
        A=M
        M=D
        @LCL
        D=M
        @SP
        AM=M+1
        M=D
        @ARG
        D=M
        @SP
        AM=M+1
        M=D
        @THIS
        D=M
        @SP
        AM=M+1
        M=D
        @THAT
        D=M
        @SP
        AM=M+1
        M=D
        @0
        D=A
        @5
        D=A+D
        @SP
        M=M+1
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Sys.main
            0;JMP
        (Sys.main_ret_addr__2)

        @SP
        AM=M-1
        D=M
        @6
        M=D
        
        (Sys.init$LOOP)
    
            @Sys.init$LOOP
                0;JMP
    
    (Sys.main)
        @SP
        A=M
    
        M=0
        A=A+1

        M=0
        A=A+1

        M=0
        A=A+1

        M=0
        A=A+1

        M=0
        A=A+1

        @5
        D=A
        @SP
        M=M+D

        @4001
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
        
        @5001
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
        
        @200
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @1
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
        
        @40
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @2
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
        
        @6
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @3
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
        
        @123
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @Sys.add12_ret_addr__3
        D=A
        @SP
        A=M
        M=D
        @LCL
        D=M
        @SP
        AM=M+1
        M=D
        @ARG
        D=M
        @SP
        AM=M+1
        M=D
        @THIS
        D=M
        @SP
        AM=M+1
        M=D
        @THAT
        D=M
        @SP
        AM=M+1
        M=D
        @1
        D=A
        @5
        D=A+D
        @SP
        M=M+1
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Sys.add12
            0;JMP
        (Sys.add12_ret_addr__3)

        @SP
        AM=M-1
        D=M
        @5
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
        
        @1
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @2
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @3
        D=A
        @LCL
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @4
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
        AM=M-1
        D=M
        A=A-1
        M=M+D

        @SP
        AM=M-1
        D=M
        A=A-1
        M=M+D

        @SP
        AM=M-1
        D=M
        A=A-1
        M=M+D

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

    (Sys.add12)
        @SP
        A=M
    
        @0
        D=A
        @SP
        M=M+D

        @4002
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
        
        @5002
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
        
        @0
        D=A
        @ARG
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        
        @12
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
