
// ***************************
// *      BOOTSTRAP CODE     *
// ***************************
            @256
            D=A
            @SP
            M=D
            // call Sys.init 0
            @Sys_ret_addr__MAIN// 1. Push return address
            D=A                     //
            @SP                     //
            A=M	                    //
            M=D                     //
            @LCL                    // 2. Push LCL
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @ARG                    // 3. Push ARG
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THIS                   // 4. Push THIS
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THAT                   // 5. Push THAT
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @0                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     //
            M=M+1                   //
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Sys.init     // 8. Goto Sys.init
                0;JMP
            (Sys_ret_addr__MAIN)

// ***************************
// *  END OF BOOTSTRAP CODE  *
// ***************************

// ========================================================== //
//                   FILE Sys
// ========================================================== //
// function Sys.init 0
        (Sys.init)
// push constant 4
            @4
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// call Main.fibonacci 1
            @Sys_ret_addr__1// 1. Push return address
            D=A                     //
            @SP                     //
            A=M	                    //
            M=D                     //
            @LCL                    // 2. Push LCL
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @ARG                    // 3. Push ARG
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THIS                   // 4. Push THIS
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THAT                   // 5. Push THAT
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @1                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     //
            M=M+1                   //
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Main.fibonacci     // 8. Goto Main.fibonacci
                0;JMP
            (Sys_ret_addr__1)
// label WHILE
            (Sys.init$WHILE)
// goto WHILE
            @Sys.init$WHILE
                0;JMP


// ========================================================== //
//                    END OF FILE Sys
// ========================================================== //

// ========================================================== //
//                   FILE Main
// ========================================================== //
// function Main.fibonacci 0
        (Main.fibonacci)
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
// push constant 2
            @2
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
            @Main__lt__0
                    D;JGE
            @SP
            A=M-1
            M=-1 
        (Main__lt__0)
// if-goto IF_TRUE
            @SP
            AM=M-1
            D=M
            @Main.fibonacci$IF_TRUE
                D;JNE
// goto IF_FALSE
            @Main.fibonacci$IF_FALSE
                0;JMP
// label IF_TRUE
            (Main.fibonacci$IF_TRUE)
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
// label IF_FALSE
            (Main.fibonacci$IF_FALSE)
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
// push constant 2
            @2
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
// call Main.fibonacci 1
            @Main_ret_addr__1// 1. Push return address
            D=A                     //
            @SP                     //
            A=M	                    //
            M=D                     //
            @LCL                    // 2. Push LCL
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @ARG                    // 3. Push ARG
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THIS                   // 4. Push THIS
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THAT                   // 5. Push THAT
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @1                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     //
            M=M+1                   //
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Main.fibonacci     // 8. Goto Main.fibonacci
                0;JMP
            (Main_ret_addr__1)
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
// push constant 1
            @1
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
// call Main.fibonacci 1
            @Main_ret_addr__2// 1. Push return address
            D=A                     //
            @SP                     //
            A=M	                    //
            M=D                     //
            @LCL                    // 2. Push LCL
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @ARG                    // 3. Push ARG
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THIS                   // 4. Push THIS
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THAT                   // 5. Push THAT
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @1                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     //
            M=M+1                   //
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Main.fibonacci     // 8. Goto Main.fibonacci
                0;JMP
            (Main_ret_addr__2)
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
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
//                    END OF FILE Main
// ========================================================== //
