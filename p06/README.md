Python version: 3.11

## Implementation details

**Note**: this implementation of assembler is different from the one proposed in the course, to be faster to write and easier to read. Though the main idea is the same, of course.

To translate a file from assembly to Hack native language, we do:
1. **Clean the code**. Delete comments, blank lines, whitespaces, etc.
2. **Build symbol table**. First, account for all the labels like `(SOME_TAG)`, and then - for references to already seen tags and to the variables, like `@i`, `@counter`, etc.
3. **Generate instructions**. Go over all the assembly commands, and, keeping in mind symbol table, yield corresponding Hack instructions.

Note that there is a way to do all the work in just one pass, but that would unnecessarily complicate the code.

Since the code is rather short (~60 lines without comments, whitespaces, docstrings, etc.), and Hack assembler doesn't have to have some internal state, it could be arranged as a module with just functions, i.e. without `Assembler` class. Functional programming approach would suit well here.

## Project structure

```
p06
 ├── asm_files
 ├── hack_files
 └── code
      ├── assembler.py
      └── const.py
```

Where:

 * `assembler.py` - holds an Assembler, which translates assembly code into Hack instructions.
 * `const.py` - holds various constants and definitions for the Assembler.


## Usage

Import `Assembler` to another file, and call it from there.

```python
from p06.code.assembler import Assembler

Assembler('p06/asm_files/Add.asm', 'p06/hack_files/Add.hack').compile()
```

## Testing

To test only the Assembler, run from the root directory level:

```bash
python -m pytest -s test/tests_06.py 
```