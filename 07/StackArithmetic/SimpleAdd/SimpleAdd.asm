// ****************************************
// *****  FILE SimpleAdd.vm
// ****************************************

// push constant 7
        @7
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
// push constant 8
        @8
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

// ****************************************
// ***** ENDOF FILE SimpleAdd.vm
// ****************************************

    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
        0;JMP
