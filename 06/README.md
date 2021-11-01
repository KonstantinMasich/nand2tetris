##

## Implementation details

**Note**: this implementation of VM compiler is different from the one proposed in the course, to be shorter and faster to write. Though main idea is the same, of course.

 * `compiler.py` holds a Compiler, which gets a single .asm file and a .hack file name as an input, and creates that .hack file by compiling mnemonics from .asm file.

Compiler is in the `asm` directory.

### Usage

`python compiler.py <path_to_asm_file> <path_to_compiled_hack_file>`

For example:

`python compiler.py asm_files/Fill.asm hack_files/Fill.hack` 

Note that python3.9 was used. You'll need at least python3.8 because of use of walrus operator `:=`; alternatively, refactor the walrus operator out.
