## Implementation details

**Note 1**: this implementation of VM compiler is different from the one proposed in the course, to be shorter and faster to write. Though main idea is the same, of course.

**Note 2**: amount of cycles in test scripts `NestedCall.tst`, `FibonacciElement.tst` and `StaticTest.tst` was lowered, so there won't be such a long waiting time after execution actually completes.

* `main.py` compiles everything in MemoryAccess and StackArithmetic folders.
* `compiler.py` holds a Compiler, which gets a single .vm file as an input and returns a string (not a file!) of assembly commands.
* `config.py` holds various constants and templates for formatting.

Compiler makes extensive use of templates defined in `config.py`, which allows for clean and short code.

When used with `debug=True` setting, Compiler adds a special instruction `@11111` after each translated VM command. This way it's easy to see (when using the provided CPU Emulator) whole assembly code blocks which correspond to distinct VM commands. That makes testing and debugging easier.

Assembly code is optimised whenever it's possible - to be short. This is crucial because it's a bottleneck: if a VM instruction is translated into 10 assembly commands instead of optimal solution with, for example, 5 commands, then it will run 2x times slower than optimum - 10 clock cycles instead of 5. 

### Branching control
Label definition `label xxx` - has a file name, current subroutine name, and a label name:
```
    ({fname}__{func}__{label})
```

Unconditional `goto xxx`:
```
    @{fname}__{func}__{label}
        0;JMP
```

Conditional `if-goto xxx`:
```
    @SP
    AM=M-1
    D=M
    @{fname}__{func}__{label}
        D;JNE
```

### Function flow

Function declaration - `function Main.foo k`:
```
    ({fname_and_func})
    @SP
    A=M    // Go the stack[last]
           // Now start pushing k zeroes to the stack
    M=0
    A=A+1
    M=0
    A=A+1
    M=0
    A=A+1
    ...
    M=0
    A=A+1
           // End of pushing zeroes; add k to SP
    @k
    D=A
    @SP
    M=M+D
```
Note that we cannot skip this "pushing zeroes" step and just increment the stack by `k`, because the stack may hold garbage values, and those need to be overridden - otherwise the convention gets broken.

Function call - `function xxx k`:
```
    nop
```

Return statement - `return`:
```
    nop
```

