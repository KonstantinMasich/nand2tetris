# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import os
import glob
# import sys
from compiler import Compiler


def main(vm_dir: str, debug: bool = False):
    """Compiles all the .vm files in a given directory into a single .asm file."""
    print(f'{"="*100}\nCompiling directory {vm_dir}...')
    if debug:
        print(f'Debug mode is ON; separator instruction is inserted.')
    os.chdir(vm_dir)
    asm_code = ''
    for fname in glob.glob('*.vm'):
        print(f'\t * Compiling file {fname}... ', end='')
        asm_code += Compiler(fname, debug=debug).compile()
        print('OK')
    # 2. Write the result into a single .asm file:
    asm_fname = f'{vm_dir.split("/")[-1]}.asm'
    with open(asm_fname, 'w') as asm_file:
        asm_file.write(asm_code)
    print(f'Compilation complete.\n{"="*100}')


if __name__ == '__main__':
    # main(sys.argv[1])
    # main('/home/konstantin/study/nand2tetris/projects/07/MemoryAccess/BasicTest')
    main('/home/konstantin/study/nand2tetris/projects/07/MemoryAccess/PointerTest', debug=True)
