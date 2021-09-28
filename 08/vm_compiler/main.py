# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import os
import glob
from compiler import Compiler
from config import BOOTSTRAP_CODE, INFINITE_LOOP


def compile_dir(vm_dir: str, debug: bool = False):
    """Compiles all the .vm files in a given directory into a single .asm file."""
    print(f'{"="*100}\nCompiling directory {vm_dir}...')
    if debug:
        print(f'Debug mode is ON; separator instruction is inserted.')
    asm_code      = ''
    vm_files      = glob.glob(f'{vm_dir}/*.vm')
    # 1. Compile each .vm file:
    for fname in vm_files:
        print(f'\t * Compiling file {fname}... ', end='')
        asm_code += Compiler(fname, debug=debug).compile()
        print('OK')
    # 2. Add bootstrap code, if needed (i.e. if Sys.vm exists), or an infinite loop:
    if f'{vm_dir}/Sys.vm' in vm_files:
        asm_code = BOOTSTRAP_CODE + asm_code
    else:
        asm_code += INFINITE_LOOP
    # 3. Write the result into a single .asm file:
    with open(f'{vm_dir}/{vm_dir.split("/")[-1]}.asm', 'w') as asm_file:
        asm_file.write(asm_code)
    print(f'Compilation complete.\n{"="*100}')


def main():
    for directory in ['ProgramFlow', 'FunctionCalls']:
        for subdirectory in os.listdir(f'../{directory}'):
            compile_dir(f'../{directory}/{subdirectory}', debug=False)


if __name__ == '__main__':
    main()
