
// ========================================================== //
//                   FILE StackTest
// ========================================================== //

// push constant 17
            @17
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 17
            @17
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// eq
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            M=0
            @StackTest__eq__0
                    D;JNE
            @SP
            A=M-1
            M=-1 
        (StackTest__eq__0)
// push constant 17
            @17
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 16
            @16
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// eq
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
// push constant 16
            @16
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 17
            @17
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// eq
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
// push constant 892
            @892
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 891
            @891
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// lt
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            M=0
            @StackTest__lt__3
                    D;JGE
            @SP
            A=M-1
            M=-1 
        (StackTest__lt__3)
// push constant 891
            @891
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 892
            @892
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// lt
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
// push constant 891
            @891
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 891
            @891
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// lt
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
// push constant 32767
            @32767
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 32766
            @32766
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// gt
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            M=0
            @StackTest__gt__6
                    D;JLE
            @SP
            A=M-1
            M=-1 
        (StackTest__gt__6)
// push constant 32766
            @32766
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 32767
            @32767
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// gt
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
// push constant 32766
            @32766
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 32766
            @32766
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// gt
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
// push constant 57
            @57
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 31
            @31
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 53
            @53
            D=A
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
// push constant 112
            @112
            D=A
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
// neg
            @SP
            A=M-1
            M=-M
// and
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M&D
// push constant 82
            @82
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// or
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M|D
// not
            @SP
            A=M-1
            M=!M


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE StackTest
// ========================================================== //
