Python version: 3.11

## Implementation details

**Note**: this implementation of VM is different from the one proposed in the course, to be faster to write and easier to read. Though the main idea is the same, of course.<br>

Implementation of the VM is fairly straightforward, and boils down to **simply filling predefined templates** (in `const.py`) with the necessary values. That's all there is to it, really.<br>

**Optimisations**: assembly code is optimised to be short whenever possible. This is crucial because it's a bottleneck: if a VM instruction is translated into 10 assembly commands instead of optimal solution with, for example, 5 commands, then it will run 2x times slower than optimum - 10 clock cycles instead of 5.<br>

<br>

## Virtual Machine

Virtual machine used in this course is a typical **stack machine**. Its language uses 4 main types of commands:
* Arithmetic commands (+, -, !, ...)
* Memory access commands (`push`, `pop`)
* Program flow commands (`label`, `goto`, `if-goto`)
* Subroutine calling commands (`function`, `call`, `return`)

This project implements the first 2 types of commands; the 2 other types will be implemented in Project 08.

<br>

## Arithmetic commands

**Unary operators**<br>
* Assembly instructions count: 3
* Optimizations: SP stays the same, it is not incremented nor it is decremented.
* Implementation:
```
    @SP                        Simply set RAM[SP-1] = {op} RAM[SP-1]
    A=M-1                      So, for example, if op is "not" operator,
    M={op}M                    then we'll get RAM[SP-1] = !RAM[SP-1]
```
<br>

**Binary operators**<br>
* Assembly instructions count: 5
* Optimizations: SP is decremented on the first step.
* Implementation:
```
    @SP                        Go to RAM[SP-1] and decrement SP at
    AM=M-1                     the same time.
    D=M
    A=A-1
    M=M{op}D                   RAM[SP-1] = RAM[SP-2] {op} RAM[SP-1]
```
<br>

**Comparison operators**<br>

True is represented as -1 (`0xFFFF`), and False is represented as 0 (`0x0000`).

* Assembly instructions count: 11
* Optimizations: instead of setting up multiple labels, we *assume that comparison result is FALSE*. The rationale here is that most of the time we test for equality / inequality during loops, so most of the times comparison result will yield FALSE. Indeed, if we run something like `for i from 0 to 99`, the comparison between `i` and 99 will yield FALSE 99 times (or 100, if it's inclusive), and will yield TRUE only once. <br>
Thus it is probably optimal to assume FALSE.
* Implementation:
```
    @SP
    AM=M-1             
    D=M                        D = RAM[SP-1]
    A=A-1
    D=M-D                      D = RAM[SP-2] - RAM[SP-1]
    M=0                        Assume that comparison result is FALSE by writing 0 now.
    @{fname}__{instr}__{mark}  ----------------------------------------------------------
        D;{jmp}                If it is indeed False - then simply jump to the end label.
    @SP                        ----------------------------------------------------------
    A=M-1                      Otherwise, go to RAM[SP-2] and fix the assumption
    M=-1                       we made earlier, i.e. set RAM[SP-1] = TRUE (-1)
({label_comp_end})     
```
**Service labels**
* Each file can have several (or a lot) of comparisons, and obviously we cannot use the same `label_comp_end` for them; otherwise they would all point to the same location in the code (the first or the last occurrence of the label, depending on how the assembler builds its symbol table).
* So we use special service labels, in the format of `{fname}__{instr}__{mark}`, where `fname` is file name, `instr` is the currently processed comparison command, and `{mark}` is a counter which is incremented each time we put a service label somewhere.
* Examples for service labels in this project: `myfile__eq__3`, `someotherfile__gt__18`.
* We need file name because other files may have exactly the same service labels, so when they are combined together by the linker, there will be multiple (possibly a lot) of labels like `gt__1`, and we will have no way to tell which one of them belongs to which VM file.

<br>

## Memory segments

In this course RAM is divided into heap and stack area, where stack area consists of 8 virtual segments.<br>

Segments directly mapped to concrete locations on the RAM:
* **argument** - a segment for storing arguments that will be passed to function. When the function is called with `call funcName nArgs`, VM knows how many arguments does it need to use from `argument` segment (of course, those arguments have to be pushed onto the stack prior to calling the function).<br>Whenever VM needs to access some argument, it goes to RAM[ARG + offset]. For example, if `ARG` is set to 1050, then `push argument 3` will add the value of RAM[1053] to the stack.
* **local** - a segment for storing local variables used by the function. When the function is defined with `function funcName nLocals`, VM knows how many local variables will it use from `local` segment.<br>Whenever VM needs to access a local variable, it goes to RAM[LCL + offset]. For example, if `LCL` is set to 670, then `pop local 2` will pop top of the stack value into RAM[672].
* **this** - segment for storing the *fields* of the current object.
* **that** - segment for storing the *elements* of the current array.
* **pointer** - segment that is mapped to `THIS` and `THAT` registers.<br>
Note that manipulations with those two segments allow modification of the memory, like RAM[THIS] = 283, whereas manipulations with "pointer" alter `THIS` and `THAT` themselves.<br>
For example, if `THIS` is set to 3030, then `pop this 1` will pop top of stack to RAM[3031]. But if we want to change the `THIS` register itself, for example to 3050, then we use `push constant 3050 ; pop pointer 0`, which will alter the `THIS` register.
* **temp** - segment for temporary variables, mapped to registers in [5, 12] interval. Used for storing various temporary data.

Static segment:
* **static** - segment for storing static variables of all the VM functions in the VM program.<br>
Spans from address 16 to address 255 including those.

Other segments:
* **constant** - a truly virtual segment, does not really exist; that is, does not have any stack areas mapped to it. Used purely for pushing constants onto the stack. Has no "pop" command, only "push".

<br>

## Memory access commands: PUSH

**push constant**<br>
* Assembly instructions count: 6
* Optimizations: SP is incremented without going to it twice.
* Implementation:
```
    @{idx}
    D=A                D = value
    @SP
    M=M+1
    A=M-1
    M=D                RAM[SP-1] = value
```

<br>

**push local**<br>
Stack segment "local" is used for storing function's local variables. For example, `push local 3` means "get the 3rd function's local variable, and push its value onto the stack".<br>
Local segment's base address is stored in `LCL` register.
* Assembly instructions count: 9
* Optimizations: SP is incremented without going to it twice.
* Implementation:
```
    @{idx}             Let's say LCL=518, and command
    D=A                is push local 3. Then:
    @{segment_alias}   @LCL, in this case.
    A=M+D          
    D=M                D = RAM[521]
    @SP
    M=M+1
    A=M-1
    M=D                RAM[SP-1] = RAM[521]
```
<br>

**push argument**<br>
Stack segment "argument" is used for storing function's arguments. For example, `push argument 1` means "get the 1st function's argument, and push its value onto the stack".<br>
Argument segment's base address is stored in `ARG` register.
* Implementation is the same as for `push local` instruction. The only difference is that segment alias is `ARG`, not `LCL`.

<br>

**push this**<br>
This segment's base address is stored in `THIS` register.
* Implementation is the same as for `push local` instruction. The only difference is that segment alias is `THIS`, not `LCL`.

<br>

**push that**<br>
This segment's base address is stored in `THAT` register.
* Implementation is the same as for `push local` instruction. The only difference is that segment alias is `THAT`, not `LCL`.

<br>

**push static**<br>
Stack segment "static" is used for storing all the static variables for all the functions in VM program, meaning - it's a storage of global variables. Its memory mapping is [16, 255], so `push static 2` will push top of the stack into RAM[18].<br>

Note that we make heavy use of "variable labels" logic: if a label is "variable label" like `@i` or `@some_var_name`, then the assembler will allocate RAM[16] to it, or RAM[17] if RAM[16] is already taken, etc. This is exactly what we need.

Generally, the assembler would try to assign RAM in [16, 255] interval to any other "variable label" too, not just to static variables, so `@i` would interfere and be placed in the midst of static variables, which is bad. While that is true, VM language does not use variable labels - only "jump labels". So "true variable labels" simply will never be created, thus we can rely on this logic to create only static variables for us!

The "variable label" logic has an added benefit of marking static variables by their respective file name; this way we can distinguish between static variable defined in one file from static variable defined in another file.
* Assembly instructions count: 6
* Optimizations: we use the "variable label" logic for the assembler.
* Implementation:
```
    @{fname}.{idx}     Create a new variable label,
    D=M                like my_file.4
    @SP
    M=M+1
    A=M-1
    M=D                RAM[SP - 1] = value of static variable
```

<br>

**push pointer**<br>
Stack segment "pointer" is mapped to RAM[3] (`THIS`) and RAM[4] (`THAT`) addresses. If `THIS` is set to 5060 and `pop this 3` pops top of the stack to 5063, then `pop pointer 0` allows to change `THIS` register itself.
* Assembly instructions count: 6
* Optimizations: the necessary offset is calculated by VM compiler before generating instructions, so it is not done in VM code, thus saving a couple of instructions.
* Implementation:
```
    @{base_and_offset} This will be 3 + offset, where offset is
    D=M                set by pointer command. It can be either 
    @SP                0 or 1.
    M=M+1
    A=M-1
    M=D                RAM[SP - 1] = THIS (or THAT)
```

<br>

**push temp**<br>
Stack segment "temp" is mapped to RAM area in [5, 12] interval. So `push temp 4` means pushing value of RAM[9] (because it's base 5 plus offset 4) onto the stack.
* Implementation is the same as for `push pointer` instruction. The only difference is that base_and_offset use base=5 (not 3) during calculation.

<br>

## Memory access commands: POP

**pop constant**<br>
There is no `pop constant` instruction in this course's VM language.

<br>

**pop local**<br>
To pop a value into local segment, we use a temporary register (like `R13`) to store local variable's address, which consists of `LCL` value and an offset.
* Assembly instructions count: 12
* Optimizations: SP is incremented without going to it twice.
* Implementation:
```
    @{idx}             Let's say LCL=780, and command
    D=A                is pop local 2. Then:
    @{segment_alias}   @LCL, in this case.
    D=D+M              D = 782
    @R13
    M=D                Register 13 = 782
    @SP
    AM=M-1
    D=M                D = RAM[SP-1]
    @R13
    A=M                A = 782
    M=D                RAM[782] = RAM[SP-1]
```

<br>

**pop argument**<br>
* Implementation is the same as for `pop local` instruction. The only difference is that segment alias is `ARG`, not `LCL`.

<br>

**pop this**<br>
* Implementation is the same as for `pop local` instruction. The only difference is that segment alias is `THIS`, not `LCL`.

<br>

**pop that**<br>
* Implementation is the same as for `pop local` instruction. The only difference is that segment alias is `THAT`, not `LCL`.

<br>

**pop static**<br>
* Assembly instructions count: 5
* Optimizations: we use the "variable label" logic for the assembler.
* Implementation:
```
    @SP
    AM=M-1
    D=M
    @{fname}.{idx}
    M=D
```

<br>

**pop pointer**<br>
* Assembly instructions count: 5
* Optimizations: the necessary offset is calculated by VM compiler before generating instructions, so it is not done in VM code, thus saving a couple of instructions.
* Implementation:
```
    @SP
    AM=M-1
    D=M
    @{base_and_offset}
    M=D
```

<br>

**pop temp**<br>
* Implementation is the same as for `pop pointer` instruction. The only difference is that base_and_offset use base=5 (not 3) during calculation.