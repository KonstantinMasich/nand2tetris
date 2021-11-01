##

## Implementation details

**Note**: this implementation of VM compiler is different from the one proposed in the course, to be shorter and faster to write. Though main idea is the same, of course.

 * `compiler.py` holds a Compiler, which gets a single .asm file and a .hack file name as an input, and creates that .hack file by compiling mnemonics from .asm file.

Compiler is in the `asm` directory.

Example of usage:
`python3 compiler.py asm_files/Fill.asm hack_files/Fill.hack` 
