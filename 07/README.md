## Implementation details

**Note**: this implementation of VM compiler is different from the one proposed in the course, to be shorter and faster to write. Though main idea is the same, of course.

 * `main.py` compiles everything in MemoryAccess and StackArithmetic folders.
 * `compiler.py` holds a Compiler, which gets a single .vm file as an input and returns a string (not a file!) of assembly commands.
 * `config.py` holds various constants and templates for formatting.

Compiler makes extensive use of templates defined in `config.py`, which allows for clean and short code.

When used with `debug=True` setting, Compiler adds a special instruction `@11111` after each translated VM command. This way it's easy to see (when using the provided CPU Emulator) whole assembly code blocks which correspond to distinct VM commands. That makes testing and debugging easier.

Assembly code is optimised whenever it's possible - to be as short. This is crucial because it's a bottleneck: if a VM instruction is translated into 10 assembly commands instead of optimal solution with, for example, 5 commands, then it will run 2x times slower than optimum - 10 clock cycles instead of 5. 

### Push/pop commands

Push and pop commands are separated into "common" case (LCL, ARG, THIS, and THAT) and special cases - pointer, constant, static, temp.
 * Code for common cases uses a common template.
 * Special cases are optimised and use their own templates. 

General push structure for `push {segment} {index}`:
```
    @{index}
    D=A         // D holds the offset (index)
    @{segment}
    A=M+D       // A points to RAM[segment + index]
    D=M         // D = RAM[segment + index]
    @SP
    M=M+1       // SP++
    A=M-1
    M=D         // stack[last] = RAM[segment + index]
```
General pop structure for `pop {segment} {index}`:
```
    // pop {segment} {index}
    @{index}    // -- First of all let's save target address to RAM[13]
    D=A
    @{segment}
    D=M+D       // D holds the address pointed to by "segment + index" 
    @13
    M=D         // Save address pointed to by "segment + index" to RAM[13]
    @SP
    AM=M-1      // SP--, A = address of stack[last]
    D=M         // D = stack[last]
    @13
    A=M         // A points to "segment + index" cell
    M=D         // Save stack[last] into [segment + index]
```
Push / pop to other segments uses offset pre-calculation to shorten amount of generated assembly instructions.

### Arithmetic commands
Commands are separated into unary (like `neg`), binary (like `add`) and relational (like `gt`) operations.
 * Unary operators use a dedicated template.
 * Binary operators use a dedicated template.
 * Relational operators also use their own template. Service labels are created to support branching in these operators, they consist of a current file name (as a unique identifier) and an integer number.

These operator groups generate pretty much the same assembly code except for different symbols; that's the reason they are grouped together, and they use common templates.

Unary operators, where `op` ∈ {-, !}:
```
    @SP
    A=M-1
    M={op}M
```

Binary operators, where `op` ∈ {+, -, &, |}:
```
    @SP
    AM=M-1    // SP--, A = address of stack[last]
    D=M       // D = stack[last]
    A=A-1     // A = address of stack[last - 1], i.e. one before last
    M=M{op}D  // stack[last - 1] = stack[last - 1] {op} stack [last]
```

Relational operators, where `op` ∈ {JNE, JGE, JLE} (here these operators are inverted relatively to tested conditions, i.e. when we test for equality, we use `JNE`, and when we test for `>`, we use JLE - "jump if less or equal"). The reason is explained below.
```
    @SP
    AM=M-1    // SP--, A = address of stack[last]
    D=M       // D = stack[last]
    A=A-1     // A = address of stack[last - 1]
    D=M-D     // D = diff between stack[last - 1] and stack[last]
    M=0       // stack[last] = False; We ASSUME that tested condition is False
    @{label}
            D;{op} // If it's indeed False - then jump to the end 
    @SP       // And if it's False - set it as False
    A=M-1
    M=0       // stack[last] = False
    ({label})
```
Label is a service label like `(myFileName__lt__14)`.

Note that we assume that tested condition is `False`, and jump to the end in this case; otherwise we set it to `True` first. 

This assumption allows for less branching and cleaner code. It is a bit counterintuitive that we use inverted jump conditions, i.e. we test for `>` but we jump only if `<=` - i.e. the opposite - holds. Why is that? Because we want to assume `False`, i.e. assume that tested condition does *not* hold, actually.

We could make a different assumption, i.e. that the tested condition does hold; then we could use the same jump condition as the tested condition, i.e. `JGT` for testing `>`. This is a valid course of action. However, it appears more efficient to assume `False`.
Comparisons are often used in loops, where most of the time they will yield False. For example, in a loop like `for i from 0 to 100` comparison `i == 100?` will yield False for 99 evaluations, and will yield True only once. Likewise, tests like `element x is in set X?` would yield `False` for every element that is not `x`, and would yield `True` only once - for `x`.

Thus assuming `False`, i.e. assuming that the tested condition does *not* hold, should speed up program execution significantly in most cases.
