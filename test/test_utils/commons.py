"""Functions commonly used by various tests."""

import pytest
import glob
import subprocess


CODE_OK = 0
DASHES  = "-" * 60


def parametrize(test_cases: dict):
    """A simple, convenient wrapper around pytest.mark.parametrize to allow passing
    dictionary-like test cases to pytest.mark.parametrize decorator.
    """
    return pytest.mark.parametrize(
        argnames  = list(test_cases.values())[0].keys(),
        argvalues = [case_data.values() for case_data in test_cases.values()],
        ids       = test_cases.keys()
    )


def run_tests_with_tool(tool: str,
                        target_dir: str,
                        tst_extension: str = 'tst',
                        ignored: set = None):
    """Runs the specified tool from Nand2Tetris suite (from "tools" directory),
    and compares its real output to expected output.
    :param tool: tool name to run without the extension, like 'HardwareSimulator'
    :param target_dir: directory with test files / comparison files
    :param tst_extension: extension for test files, defaults to 'tst'
    :param ignored: a cointer of file names to ignore during testing
    """
    print(f'\n{DASHES}\nRunning {tool} on {target_dir}\n{DASHES}')
    template  = f'{target_dir}/*{tst_extension}'
    filenames = [f for f in sorted(glob.glob(template))
                 if f not in (ignored or [])]
    for fname in filenames:
        print(f'Testing {fname}... ', end='')
        cmd = f'./tools/{tool}.sh {fname}'.split()
        assert subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode == CODE_OK
        print('OK')


def are_identical_files(fname_1: str, fname_2: str) -> bool:
    """Using TextComparer supplied script, returns True if the two given files
    are identical, False otherwise.
    """
    print(f'Comparing "{fname_1}" with "{fname_2}"... ')
    cmd = f'./tools/TextComparer.sh {fname_1} {fname_2}'.split()
    return subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode == CODE_OK
