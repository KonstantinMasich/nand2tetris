"""Test configurations file for testing Project 06 (Assembler)."""

from p06.code.const import PREDEFINED_SYMBOLS


TESTDATA__BUILD_SYMBOL_TABLE = {
    # -------------------------------------------------------------------------
    'Add.asm': dict(
        asm_fname = 'p06/asm_files/Add.asm',
        expected  = PREDEFINED_SYMBOLS
    ),
    # -------------------------------------------------------------------------
    'Fill.asm': dict(
        asm_fname = 'p06/asm_files/Fill.asm',
        expected  = {
            **PREDEFINED_SYMBOLS,
            **dict(START=0, BLACK=6, WHITE=10, PAINT=14, LOOP=22, i=16, pixel=17)
        }
    ),
    # -------------------------------------------------------------------------
}

TESTDATA__BUILD_A_INSTR = {
    '0'   : dict(cmd='@0'   , context=dict(), expected='0000000000000000'),
    '17'  : dict(cmd='@17'  , context=dict(), expected='0000000000010001'),
    'R0'  : dict(cmd='@0'   , context=dict(), expected='0000000000000000'),
    'R9'  : dict(cmd='@9'   , context=dict(), expected='0000000000001001'),
    'THIS': dict(cmd='@THIS', context=dict(), expected='0000000000000011'),
    'TAG' : dict(cmd='@TAG' , context=dict(TAG=10)  , expected='0000000000001010'),
    'IF_3': dict(cmd='@IF_3', context=dict(IF_3=255), expected='0000000011111111'),
    'IF_4': dict(cmd='@IF_4', context=dict(IF_4=256), expected='0000000100000000'),
}

TESTDATA__BUILD_C_INSTR = {
    'A=A+1' : dict(cmd='A=A+1', expected='1110110111100000'),
    'M=!D'  : dict(cmd='M=!D' , expected='1110001101001000'),
    'D=!M'  : dict(cmd='D=!M' , expected='1111110001010000'),
    'Full'  : dict(cmd='ADM=D+M;JLE', expected='1111000010111110'),
    'Jump_1': dict(cmd='0;JGE'      , expected='1110101010000011'),
    'Jump_2': dict(cmd='D+A;JEQ'    , expected='1110000010000010'),
}

TESTDATA__COMPILE = {
    # -------------------------------------------------------------------------
    'Add.asm': dict(
        asm_fname = 'p06/asm_files/Add.asm',
        expected  = [
            '0000000000000010', '1110110000010000', '0000000000000011',
            '1110000010010000', '0000000000000000', '1110001100001000']
    ),
    # -------------------------------------------------------------------------
    'Fill.asm': dict(
        asm_fname = 'p06/asm_files/Fill.asm',
        expected  = [
            '0110000000000000', '1111110000010000', '0000000000001010', '1110001100000010',
            '0000000000000110', '1110101010000111', '0000000000000000', '1110111010001000',
            '0000000000001110', '1110101010000111', '0000000000000000', '1110101010001000',
            '0000000000001110', '1110101010000111', '0001111111111110', '1110110000010000',
            '0000000000010000', '1110001100001000', '0100000000000000', '1110110000010000',
            '0000000000010001', '1110001100001000', '0000000000000000', '1111110000010000',
            '0000000000010001', '1111110000100000', '1110001100001000', '0000000000010001',
            '1111110111001000', '0000000000010000', '1111110010001000', '1111110000010000',
            '0000000000000000', '1110001100000010', '0000000000010110', '1110001100000111',
        ]
    )
    # -------------------------------------------------------------------------
}

TESTDATA__TO_16BIT_BINARY = {
    '0'       : dict(num =     0, expected = '0' * 16),
    '65536'   : dict(num = 65535, expected = '1' * 16),
    '1'       : dict(num =     1, expected = '0000000000000001'),
    '4'       : dict(num =     4, expected = '0000000000000100'),
    '32768'   : dict(num = 32768, expected = '1000000000000000'),
}

TESTDATA__GET_CLEAN_INSTRUCTION = {
    'blank'        : dict(instr =  '  \n ', expected = ''),
    'blank_comment': dict(instr = ' // hi', expected = ''),
    'simple_1'     : dict(instr =  'D=M+1', expected = 'D=M+1'),
    'simple_2'     : dict(instr =         'D = M + 1 ', expected = 'D=M+1'),
    'comment'      : dict(instr =  'D = M + 1  // hi ', expected = 'D=M+1'),
}
