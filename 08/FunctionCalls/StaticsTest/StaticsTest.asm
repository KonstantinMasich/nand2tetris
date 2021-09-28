
// ***************************
// *      BOOTSTRAP CODE     *
// ***************************
            @256
            D=A
            @SP
            M=D
            // call Sys.init 0
            @Sys_ret_addr__MAIN// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
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
            M=M+1                   // <-- Here's that delayed SP increment.
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
//                   FILE Class1
// ========================================================== //
// function Class1.set 0
        (Class1.set)
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
// push static 0
            @SP
            AM=M-1
            D=M
            @Class1.0
            M=D
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
// push static 1
            @SP
            AM=M-1
            D=M
            @Class1.1
            M=D
// push constant 0
            @0
            D=A
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
// function Class1.get 0
        (Class1.get)
// push static 0
            @Class1.0
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
// push static 1
            @Class1.1
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
//                    END OF FILE Class1
// ========================================================== //

// ========================================================== //
//                   FILE Sys
// ========================================================== //
// function Sys.init 0
        (Sys.init)
// push constant 6
            @6
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
// call Class1.set 2
            @Sys_ret_addr__1// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
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
            @2                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     // 
            M=M+1                   // <-- Here's that delayed SP increment.
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Class1.set     // 8. Goto Class1.set
                0;JMP
            (Sys_ret_addr__1)
// pop temp 0
            @SP
            AM=M-1
            D=M
            @5
            M=D
// push constant 23
            @23
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// push constant 15
            @15
            D=A
            @SP
            M=M+1
            A=M-1
            M=D
// call Class2.set 2
            @Sys_ret_addr__2// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
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
            @2                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     // 
            M=M+1                   // <-- Here's that delayed SP increment.
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Class2.set     // 8. Goto Class2.set
                0;JMP
            (Sys_ret_addr__2)
// pop temp 0
            @SP
            AM=M-1
            D=M
            @5
            M=D
// call Class1.get 0
            @Sys_ret_addr__3// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
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
            M=M+1                   // <-- Here's that delayed SP increment.
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Class1.get     // 8. Goto Class1.get
                0;JMP
            (Sys_ret_addr__3)
// call Class2.get 0
            @Sys_ret_addr__4// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
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
            M=M+1                   // <-- Here's that delayed SP increment.
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @Class2.get     // 8. Goto Class2.get
                0;JMP
            (Sys_ret_addr__4)
// label WHILE
            (Sys.init$WHILE)
// goto WHILE
            @Sys.init$WHILE
                0;JMP


// ========================================================== //
//                    END OF FILE Sys
// ========================================================== //

// ========================================================== //
//                   FILE Class2
// ========================================================== //
// function Class2.set 0
        (Class2.set)
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
// push static 0
            @SP
            AM=M-1
            D=M
            @Class2.0
            M=D
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
// push static 1
            @SP
            AM=M-1
            D=M
            @Class2.1
            M=D
// push constant 0
            @0
            D=A
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
// function Class2.get 0
        (Class2.get)
// push static 0
            @Class2.0
            D=M
            @SP
            M=M+1
            A=M-1
            M=D
// push static 1
            @Class2.1
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
//                    END OF FILE Class2
// ========================================================== //
