
        @17
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @17
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__eq__1
            D;JNE
        @SP
        A=M-1
        M=-1
    (StackTest__eq__1)

        @17
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @16
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__eq__2
            D;JNE
        @SP
        A=M-1
        M=-1
    (StackTest__eq__2)

        @16
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @17
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__eq__3
            D;JNE
        @SP
        A=M-1
        M=-1
    (StackTest__eq__3)

        @892
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @891
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__lt__4
            D;JGE
        @SP
        A=M-1
        M=-1
    (StackTest__lt__4)

        @891
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @892
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__lt__5
            D;JGE
        @SP
        A=M-1
        M=-1
    (StackTest__lt__5)

        @891
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @891
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__lt__6
            D;JGE
        @SP
        A=M-1
        M=-1
    (StackTest__lt__6)

        @32767
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @32766
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__gt__7
            D;JLE
        @SP
        A=M-1
        M=-1
    (StackTest__gt__7)

        @32766
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @32767
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__gt__8
            D;JLE
        @SP
        A=M-1
        M=-1
    (StackTest__gt__8)

        @32766
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @32766
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @StackTest__gt__9
            D;JLE
        @SP
        A=M-1
        M=-1
    (StackTest__gt__9)

        @57
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @31
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @53
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

        @112
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

        @SP
        A=M-1
        M=-M

        @SP
        AM=M-1
        D=M
        A=A-1
        M=M&D

        @82
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M|D

        @SP
        A=M-1
        M=!M

        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
