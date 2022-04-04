import glob
import os
from lexer import tokenize
from jack_compiler import Compiler


def __compile_dir(dirname: str):
    """Compiles each .jack file in a given directory."""
    print(f'{"="*100}\nWorking with directory {dirname}...')
    for src_fname in glob.glob(f'{dirname}/*.jack'):
        vm_fname = f'{src_fname[:-5]}__my.vm'
        with open(src_fname, 'r') as src_file:
            print(f'\tCompiling file {src_fname.split("/")[-1]}...')
            code     = ''.join(src_file.readlines())
            tokens   = tokenize(code)
            compiler = Compiler(tokens, vm_fname)
            compiler.compile()
    print(f'Compilation complete.\n{"="*100}')


def __compare_dir(dirname: str):
    """Compares abc.vm and abc__my.vm files."""
    _, _, filenames = next(os.walk(dirname))
    filenames = set([x.split('.vm')[0].split('.jack')[0].split('__my')[0] for x in filenames])
    for fname in filenames:
        print(f'\tComparing files {fname}.vm and {fname}__my.vm... ')
        with open(f'{dirname}/{fname}.vm') as orig_file, open(f'{dirname}/{fname}__my.vm') as res_file:
            correct_ans = [x[:-1] if x[-1] == '\n' else x for x in orig_file.readlines()]
            result      = [x[:-1] if x[-1] == '\n' else x for x in res_file .readlines()]
            assert result == correct_ans
    print(f'OK\n{"-"*60}')


def test_compare():
    print()
    for dirname in os.listdir('provided_files/'):
        __compile_dir(f'provided_files/{dirname}')
        __compare_dir(f'provided_files/{dirname}')
    assert True
