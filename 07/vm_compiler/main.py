# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import os
import glob
from compiler import Compiler


def compile_dir(vm_dir: str, debug: bool = False):
    """Compiles all the .vm files in a given directory into a single .asm file."""
    if 'Static' in vm_dir:
        return
    print(f'{"="*100}\nCompiling directory {vm_dir}...')
    if debug:
        print(f'Debug mode is ON; separator instruction is inserted.')
    asm_code = ''
    # 1. Compile each .vm file:
    for fname in glob.glob(f'{vm_dir}/*.vm'):
        print(f'\t * Compiling file {fname}... ', end='')
        asm_code += Compiler(fname, debug=debug).compile()
        print('OK')
    # 2. Write the result into a single .asm file:
    asm_fname = f'{vm_dir}/{vm_dir.split("/")[-1]}.asm'
    with open(asm_fname, 'w') as asm_file:
        asm_file.write(asm_code)
    print(f'Compilation complete.\n{"="*100}')


def main():
    for directory in os.listdir('../StackArithmetic'):
        compile_dir(f'../StackArithmetic/{directory}')
    for directory in os.listdir('../MemoryAccess'):
        compile_dir(f'../MemoryAccess/{directory}')


if __name__ == '__main__':
    main()
