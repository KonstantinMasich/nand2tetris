## Implementation details

**Note 1**: this implementation of VM compiler is different from the one proposed in the course, to be shorter and faster to write. Though main idea is the same, of course.

* `main.py` compiles everything in MemoryAccess and StackArithmetic folders.
* `compiler.py` holds a Compiler, which gets a single .vm file as an input and returns a string (not a file!) of assembly commands.
* `config.py` holds various constants and templates for formatting.

Compiler makes extensive use of templates defined in `config.py`, which allows for clean and short code.

When used with `debug=True` setting, Compiler adds a special instruction `@11111` after each translated VM command. This way it's easy to see (when using the provided CPU Emulator) whole assembly code blocks which correspond to distinct VM commands. That makes testing and debugging easier.

Assembly code is optimised whenever it's possible - to be short. This is crucial because it's a bottleneck: if a VM instruction is translated into 10 assembly commands instead of optimal solution with, for example, 5 commands, then it will run 2x times slower than optimum - 10 clock cycles instead of 5. 


### Service marks, labels and call IDs
* Internal labels that serve commands like `eq`, `gt`, `lt`, are constructed using an incrementing service marks, like `Main__eq__3` or `Math__gt__118`.
This is to distinguish between them: we cannot give the same label to all conditional checks, for obvious reasons. Generally just a service mark would
suffice here, but we may add a file name and comparison name for clarity.
* Labels declared with commands `label` are created as `Main.foo$LABEL`
* A function declaration is universal, i.e. each function is declared only once, as `LinkedList.addNode`
* However, a *call* to function is unique, i.e. each call should get its unique mark to return to; otherwise, all calls to a given function would return to the same place and resume execution from the same line of code, which is clearly wrong. For that, we use the `cid` variable (**c**all **id**) to distinguish between calls to the same function from completely different places in the code. We also use a file name, because a function can be called not only from different places in the same file, but from different files as well.


### Branching control
Label definition `label xxx` - has a file name, current subroutine name, and a label name:
```
    ({file_func}${label})
```

Unconditional `goto xxx`:
```
    @{file_func}${label}
        0;JMP
```

Conditional `if-goto xxx`:
```
    @SP
    AM=M-1
    D=M
    @{file_func}${label}
        D;JNE
```

### Function flow

We go by the book here.

For function call we save the caller's "world" (5 registers - SP, LCL, ARG, THIS and THAT) on top of the stack and create a label to which the CPU will come back and resume executing after the called function finishes running.

For returning from function we restore the caller's "world" (those 5 registers) and jump to the return mark created by the caller while executing a call.


Function declaration - `function Main.add k`:
```
(Main.add)
	@SP
	A=M
	M=0   //  __
	A=A+1 //   |
	M=0   //   |
	A=A+1 //   |
	...   //  .|-->  This is done k times
	M=0   //  .|
	A=A+1 //  --
	@{k}  // Note that we pushed zeroes but didn't increment SP, this
	D=A   // is done for optimisation purposes. Instead, we do the
	@SP   // incrementing now: SP += k
	M=M+D
```
Note that we could skip this "pushing zeroes" step and just increment the stack by `k` but maybe we shoudln't because the stack may hold garbage values, and those need to be overridden - otherwise the convention gets broken.


Function call - `function xxx k`:
```
	@{fname}_ret_addr__{cid}// 1. Push return address. Note that SP is not incremented
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
	@{k}                    // 6. Set ARG = SP - k - 5
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
	@{called_file_func}     // 8. Goto {called_file_func}
	    0;JMP
	({fname}_ret_addr__{cid})
```

Return statement - `return`:
```
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
```
