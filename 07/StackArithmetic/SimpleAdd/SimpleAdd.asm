
// ========================================================== //
//                   FILE SimpleAdd
// ========================================================== //

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
            M=M{'op': '-', 'template': '// {opname}\n            @SP\n            AM=M-1\n            D=M\n            A=A-1\n            M=M{op}D\n'}D


    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE SimpleAdd
// ========================================================== //
