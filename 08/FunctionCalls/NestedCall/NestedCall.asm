
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
// push constant 4000
            @4000
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 0
            @SP
            AM=M-1
            D=M
            @3
            M=D
// push constant 5000
            @5000
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
// call Sys.main 0
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
            @Sys.main     // 8. Goto Sys.main
                0;JMP
            (Sys_ret_addr__1)
// pop temp 1
            @SP
            AM=M-1
            D=M
            @6
            M=D
// label LOOP
            (Sys.init$LOOP)
// goto LOOP
            @Sys.init$LOOP
                0;JMP
// function Sys.main 5
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
// push constant 4001
            @4001
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 0
            @SP
            AM=M-1
            D=M
            @3
            M=D
// push constant 5001
            @5001
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
// push constant 200
            @200
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop LCL 1
            @1
            D=A
            @LCL
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push constant 40
            @40
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop LCL 2
            @2
            D=A
            @LCL
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push constant 6
            @6
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop LCL 3
            @3
            D=A
            @LCL
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D
// push constant 123
            @123
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// call Sys.add12 1
            @Sys_ret_addr__2// 1. Push return address
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
            @Sys.add12     // 8. Goto Sys.add12
                0;JMP
            (Sys_ret_addr__2)
// pop temp 0
            @SP
            AM=M-1
            D=M
            @5
            M=D
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
// push LCL 2
            @2
            D=A
            @LCL
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push LCL 3
            @3
            D=A
            @LCL
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D
// push LCL 4
            @4
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
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
// add
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M+D
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
// function Sys.add12 0
        (Sys.add12)
// push constant 4002
            @4002
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 0
            @SP
            AM=M-1
            D=M
            @3
            M=D
// push constant 5002
            @5002
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// pop pointer 1
            @SP
            AM=M-1
            D=M
            @4
            M=D
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
// push constant 12
            @12
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
//                    END OF FILE Sys
// ========================================================== //
