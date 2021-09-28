
// ========================================================== //
//                   FILE SimpleFunction
// ========================================================== //
// function SimpleFunction.test 2
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
// push LCL 0
            @0
            D=A
            @LCL
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push LCL 1
            @1
            D=A
            @LCL
            A=M+D
            D=M 
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
// not
            @SP
            A=M-1
            M=!M
// push ARG 0
            @0
            D=A
            @ARG
            A=M+D
            D=M 
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
// push ARG 1
            @1
            D=A
            @ARG
            A=M+D
            D=M 
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
// return
            @LCL                    // 1. FRAME = LCL
            D=M                     //
            @13                     //
            M=D                     //
            @5                      // 2. RET = *(FRAME-5)
            D=D-A                   //
            A=D                     //
            D=M                     //
            @14                     //
            M=D                     //
            @SP                     // 3. *ARG = pop()
            AM=M-1                  //
            D=M                     //
            @ARG                    //
            A=M                     //
            M=D                     //
            @ARG                    // 4. SP = ARG + 1
            D=M+1                   //
            @SP                     //
            M=D                     //
            @13                     // 5. THAT = *(FRAME-1)
            AM=M-1                  //
            D=M                     //
            @THAT                   //
            M=D                     //
            @13                     // 6. THIS = *(FRAME-2)
            AM=M-1                  //
            D=M                     //
            @THIS                   //
            M=D                     //
            @13                     // 7. ARG = *(FRAME-3)
            AM=M-1                  //
            D=M                     //
            @ARG                    //
            M=D                     //
            @13                     // 8. LCL = *(FRAME-4)
            AM=M-1                  //
            D=M                     //
            @LCL                    //
            M=D                     //
            @14                     // 9. Goto RET
            A=M
                0;JMP


// ========================================================== //
//                    END OF FILE SimpleFunction
// ========================================================== //

    (Sys.init$WHILE)
        @Sys.init$WHILE
                0;JMP
