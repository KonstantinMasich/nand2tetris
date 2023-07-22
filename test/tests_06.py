import os
import pytest
from p06.code.assembler import Assembler
from test_utils.commons import parametrize, are_identical_files
import test_utils.test_configs_06 as test_configs


@parametrize(test_configs.TESTDATA__BUILD_SYMBOL_TABLE)
def test_build_symbol_table(asm_fname, expected):
    asm = Assembler()
    asm.compile_file(asm_fname)
    assert expected == asm.symbols


@parametrize(test_configs.TESTDATA__BUILD_A_INSTR)
def test_build_a_instr(cmd, context, expected):
    asm = Assembler()
    asm.symbols.update(context)
    assert expected == asm._build_a_instr(cmd)


@parametrize(test_configs.TESTDATA__BUILD_C_INSTR)
def test_build_c_instr(cmd, expected):
    asm = Assembler()
    assert expected == asm._build_c_instr(cmd)


@parametrize(test_configs.TESTDATA__COMPILE)
def test_compile(asm_fname, expected):
    assert expected == list(Assembler().compile_file(asm_fname))


@parametrize(test_configs.TESTDATA__TO_16BIT_BINARY)
def test_to_16bits_binary__sanity(num, expected):
    assert expected == Assembler.to_16bit_binary(num)


def test_to_16bits_binary__overflow():
    """Method to_16bits_binary should raise an exception when
    presented with overflowing number."""
    for n in {2**16, 2**16 + 30, 2**18}:
        with pytest.raises(ValueError):
            Assembler.to_16bit_binary(n)


@parametrize(test_configs.TESTDATA__GET_CLEAN_INSTRUCTION)
def test_get_clean_instruction(instr, expected):
    assert expected == Assembler._get_clean_instruction(instr)


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                        TESTS WITH PROVIDED TOOLS                           ║
# ╚════════════════════════════════════════════════════════════════════════════╝
def test_using_tools():
    asm = Assembler()
    asm_dir, hack_dir = 'p06/asm_files', 'p06/hack_files'
    for asm_fname in os.listdir(asm_dir):
        # 1. Compile .asm file to .hack file using Assembler:
        correct_hack_fname = asm_fname.replace(".asm", ".hack")
        my_hack_fname      = f'my__{correct_hack_fname}'
        asm.compile_file(f'{asm_dir}/{asm_fname}', f'{hack_dir}/{my_hack_fname}')
        # 2. Compare the generated .hack file to the correct one:
        assert are_identical_files(f'{hack_dir}/{correct_hack_fname}',
                                   f'{hack_dir}/{my_hack_fname}')
