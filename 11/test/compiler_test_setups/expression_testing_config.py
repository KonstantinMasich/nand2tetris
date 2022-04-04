TEST__COMPILE_TERM = {
    # Integer constants:
    '14' : ['push constant 14'] ,
    '289': ['push constant 289'],
    # Unary operations:
    '-1' : ['push constant 1', 'neg'],
    # Builtins:
    'true': ['push constant 0', 'not'],
    # String constant:
    '"Hello world!"': [
        'push constant 12'        ,
        'call String.new 1'       ,
        'push constant 72'        ,
        'call String.appendChar 2',
        'push constant 101'       ,
        'call String.appendChar 2',
        'push constant 108'       ,
        'call String.appendChar 2',
        'push constant 108'       ,
        'call String.appendChar 2',
        'push constant 111'       ,
        'call String.appendChar 2',
        'push constant 32'        ,
        'call String.appendChar 2',
        'push constant 119'       ,
        'call String.appendChar 2',
        'push constant 111'       ,
        'call String.appendChar 2',
        'push constant 114'       ,
        'call String.appendChar 2',
        'push constant 108'       ,
        'call String.appendChar 2',
        'push constant 100'       ,
        'call String.appendChar 2',
        'push constant 33'        ,
        'call String.appendChar 2',
    ],
    # CLASS VARS: Fields and statics
    'a': ['push this 0']  ,
    'b': ['push this 1']  ,
    'c': ['push this 2']  ,
    'G': ['push static 0'],
    'M': ['push static 1'],
    # SUBROUTINES: arguments
    't1': ['push argument 0'],
    't2': ['push argument 1'],
    # SUBROUTINES: local variables
    'x': ['push local 0'],
    'y': ['push local 1'],
    'z': ['push local 2'],
    # # Arrays:
    # 'arr2[3]': [
    #     'push constant 3',
    #     'push local 4',
    #     'add',
    #     'pop temp 0',
    #     'pop pointer 1',
    #     'push temp 0',
    #     'pop that 0'
    # ],
}

TEST__COMPILE_EXPRESSION = {
    '1 + 2': ['push constant 1', 'push constant 2', 'add'],
    '1 - 2': ['push constant 1', 'push constant 2', 'sub'],
    '1 & 2': ['push constant 1', 'push constant 2', 'and'],
    '1 | 2': ['push constant 1', 'push constant 2', 'or'] ,
    '1 > 2': ['push constant 1', 'push constant 2', 'gt'] ,
    '1 < 2': ['push constant 1', 'push constant 2', 'lt'] ,
    '1 = 2': ['push constant 1', 'push constant 2', 'eq'] ,
    '1 * 2': ['push constant 1', 'push constant 2', 'call Math.multiply 2'],
    '1 / 2': ['push constant 1', 'push constant 2', 'call Math.divide 2']
}

TEST__COMPILE_EXPRESSION_LIST = {
    '(1+1, 10/5, 3*2, 7&8)': [
        'push constant 1'     ,
        'push constant 1'     ,
        'add'                 ,
        'push constant 10'    ,
        'push constant 5'     ,
        'call Math.divide 2'  ,
        'push constant 3'     ,
        'push constant 2'     ,
        'call Math.multiply 2',
        'push constant 7'     ,
        'push constant 8'     ,
        'and'
    ],
    '()': []
}
