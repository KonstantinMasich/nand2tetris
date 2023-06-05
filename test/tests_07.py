import glob
from p07.code.compiler  import VMCompiler
from test_utils.commons import run_tests_with_tool


def test_with_cpu_emulator():
    vm_compiler = VMCompiler()
    for directory in {'p07/StackArithmetic', 'p07/MemoryAccess'}:
        for subdir in glob.glob(f'{directory}/*'):
            vm_compiler.compile(subdir)
            vme_test_files = [fname for fname in glob.glob(f'{subdir}/*.tst')
                              if 'VME.tst' in fname]
            run_tests_with_tool(tool='CPUEmulator', target_dir=subdir, ignored=vme_test_files)
