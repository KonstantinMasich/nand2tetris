
TEST__COMPILE_LET_STATEMENT = {
        'let t1 = 123;': ['push constant 123', 'pop argument 0'],
        'let t2 = 789;': ['push constant 789', 'pop argument 1'],
        'let z  = 234;': ['push constant 234', 'pop local 2'],
        'let z = Math.multiply(7, 4+2);': [
            'push constant 7',
            'push constant 4',
            'push constant 2',
            'add',
            'call Math.multiply 2',
            'pop local 2'
        ],
        'let x = Math.multiply(y, M);' : [
            'push local 1',
            'push static 1',
            'call Math.multiply 2',
            'pop local 0'
        ],
        'let arr1 = Array.new(10);' : ['push constant 10', 'call Array.new 1', 'pop local 3'],
        'let arr2 = Array.new(2+3);': ['push constant 2', 'push constant 3', 'add', 'call Array.new 1', 'pop local 4'],
        'let arr3 = Array.new(x);'  : ['push local 0', 'call Array.new 1', 'pop local 5'],
}


TEST__COMPILE_DO_STATEMENT = {
    'do Foo.Bar();': [
        'call Foo.Bar 0',
        'pop temp 0'
    ],
    'do Output.printString("Hello world!");': [
        'push constant 12'         ,
        'call String.new 1'        ,
        'push constant 72'         ,
        'call String.appendChar 2' ,
        'push constant 101'        ,
        'call String.appendChar 2' ,
        'push constant 108'        ,
        'call String.appendChar 2' ,
        'push constant 108'        ,
        'call String.appendChar 2' ,
        'push constant 111'        ,
        'call String.appendChar 2' ,
        'push constant 32'         ,
        'call String.appendChar 2' ,
        'push constant 119'        ,
        'call String.appendChar 2' ,
        'push constant 111'        ,
        'call String.appendChar 2' ,
        'push constant 114'        ,
        'call String.appendChar 2' ,
        'push constant 108'        ,
        'call String.appendChar 2' ,
        'push constant 100'        ,
        'call String.appendChar 2' ,
        'push constant 33'         ,
        'call String.appendChar 2' ,
        'call Output.printString 1',
        'pop temp 0'
    ],
    'do Output.println();': [
        'call Output.println 0',
        'pop temp 0'
    ]
}

TEST__COMPILE_IF_STATEMENT = {
    'if (true) {}'    : [
        'push constant 0' ,
        'not'             ,
        'if-goto IF_TRUE0',
        'goto IF_FALSE0'  ,
        'label IF_TRUE0'  ,
        'label IF_FALSE0'
    ],
    'if (true) {let x = 123;}': [
        'push constant 0'  ,
        'not'              ,
        'if-goto IF_TRUE0' ,
        'goto IF_FALSE0'   ,
        'label IF_TRUE0'   ,
        'push constant 123',
        'pop local 0'      ,
        'label IF_FALSE0'
    ],
    'if (true) {let x = 123;} else {let y = 14;}': [
        'push constant 0'  ,
        'not'              ,
        'if-goto IF_TRUE0' ,
        'goto IF_FALSE0'   ,
        'label IF_TRUE0'   ,
        'push constant 123',
        'pop local 0'      ,
        'goto IF_END0'     ,
        'label IF_FALSE0'  ,
        'push constant 14' ,
        'pop local 1'      ,
        'label IF_END0'
    ],
    """ if (true) {
            let x = 123;
            if (false) {
                let y = 789;
            }
        }""": [
        'push constant 0'  ,
        'not'              ,
        'if-goto IF_TRUE0' ,
        'goto IF_FALSE0'   ,
        'label IF_TRUE0'   ,
        'push constant 123',
        'pop local 0'      ,
        'push constant 0'  ,
        'if-goto IF_TRUE1' ,
        'goto IF_FALSE1'   ,
        'label IF_TRUE1'   ,
        'push constant 789',
        'pop local 1'      ,
        'label IF_FALSE1'  ,
        'label IF_FALSE0'
    ],
    """if (true) {
        if (2 > 3) {
            let x = 2 + 2;
            if (M = 5) {}
            else { }
        }
        else {
            let x = 123;
        }
    }
    else {
        let y = 999;
    }""": [
        'push constant 0'  ,
        'not'              ,
        'if-goto IF_TRUE0' ,
        'goto IF_FALSE0'   ,
        'label IF_TRUE0'   ,
        'push constant 2'  ,
        'push constant 3'  ,
        'gt'               ,
        'if-goto IF_TRUE1' ,
        'goto IF_FALSE1'   ,
        'label IF_TRUE1'   ,
        'push constant 2'  ,
        'push constant 2'  ,
        'add'              ,
        'pop local 0'      ,
        'push static 1'    ,
        'push constant 5'  ,
        'eq'               ,
        'if-goto IF_TRUE2' ,
        'goto IF_FALSE2'   ,
        'label IF_TRUE2'   ,
        'goto IF_END2'     ,
        'label IF_FALSE2'  ,
        'label IF_END2'    ,
        'goto IF_END1'     ,
        'label IF_FALSE1'  ,
        'push constant 123',
        'pop local 0'      ,
        'label IF_END1'    ,
        'goto IF_END0'     ,
        'label IF_FALSE0'  ,
        'push constant 999',
        'pop local 1'      ,
        'label IF_END0'
    ]
}

TEST__COMPILE_RETURN_STATEMENT = {
    'return;'    : ['push constant 0' , 'return'],
    'return 17;' : ['push constant 17', 'return'],
    'return G;'  : ['push static 0'   , 'return'],
    'return M;'  : ['push static 1'   , 'return'],
    'return t1;' : ['push argument 0' , 'return'],
    'return t2;' : ['push argument 1' , 'return'],
    'return x;'  : ['push local 0'    , 'return'],
    'return y;'  : ['push local 1'    , 'return'],
    'return z;'  : ['push local 2'    , 'return'],
    'return 9+3;': ['push constant 9', 'push constant 3', 'add', 'return'],
    'return Foo.Bar(7,8,9);': ['push constant 7', 'push constant 8', 'push constant 9', 'call Foo.Bar 3', 'return'],
}


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
CONFIG__SYMBOLS_STATEMENT = {
    'class': {
        'a': {'type': 'int'    , 'kind': 'field' , 'i': 0},
        'b': {'type': 'String' , 'kind': 'field' , 'i': 1},
        'c': {'type': 'boolean', 'kind': 'field' , 'i': 2},
        'G': {'type': 'int'    , 'kind': 'static', 'i': 0},
        'M': {'type': 'int'    , 'kind': 'static', 'i': 1},
    },
    'foo': {
        'locals': {
            'x'   : {'type': 'int'    , 'kind': 'local', 'i': 0},
            'y'   : {'type': 'Pointer', 'kind': 'local', 'i': 1},
            'z'   : {'type': 'Square' , 'kind': 'local', 'i': 2},
            'arr1': {'type': 'Array'  , 'kind': 'local', 'i': 3},
            'arr2': {'type': 'Array'  , 'kind': 'local', 'i': 4},
            'arr3': {'type': 'Array'  , 'kind': 'local', 'i': 5},
        },
        'args': {
            't1': {'type': 'int'   , 'kind': 'argument', 'i': 0},
            't2': {'type': 'String', 'kind': 'argument', 'i': 1}
        }
    },
    'bar': {
        'locals': {
            'z': {'type': 'int'    , 'kind': 'local', 'i': 0},
            'x': {'type': 'Pointer', 'kind': 'local', 'i': 1},
            'y': {'type': 'Square' , 'kind': 'local', 'i': 2},
        },
        'args': {
            't1': {'type': 'int'   , 'kind': 'argument', 'i': 0},
            't2': {'type': 'String', 'kind': 'argument', 'i': 1},
            's1': {'type': 'String', 'kind': 'argument', 'i': 1},
            's2': {'type': 'String', 'kind': 'argument', 'i': 1},
        }
    }
}

TEST__COMPILE_WHILE_STATEMENT = {
    'while (true) {}': [
        'label WHILE_EXP0'  ,
        'push constant 0'   ,
        'not'               ,
        'not'               ,
        'if-goto WHILE_END0',
        'goto WHILE_EXP0'   ,
        'label WHILE_END0'  ,
    ],
    'while (x > 10 & x < 15) {let y = y + z + 2;}': [
        'label WHILE_EXP0'  ,
        'push local 0'      ,
        'push constant 10'  ,
        'gt'                ,
        'push local 0'      ,
        'and'               ,
        'push constant 15'  ,
        'lt'                ,
        'not'               ,
        'if-goto WHILE_END0',
        'push local 1'      ,
        'push local 2'      ,
        'add'               ,
        'push constant 2'   ,
        'add'               ,
        'pop local 1'       ,
        'goto WHILE_EXP0'   ,
        'label WHILE_END0'
    ],
    'while (x < 30) {while (y < 20) {while (z < 10) {let M = 218;}}}': [
        'label WHILE_EXP0'  ,
        'push local 0'      ,
        'push constant 30'  ,
        'lt'                ,
        'not'               ,
        'if-goto WHILE_END0',
        'label WHILE_EXP1'  ,
        'push local 1'      ,
        'push constant 20'  ,
        'lt'                ,
        'not'               ,
        'if-goto WHILE_END1',
        'label WHILE_EXP2'  ,
        'push local 2'      ,
        'push constant 10'  ,
        'lt'                ,
        'not'               ,
        'if-goto WHILE_END2',
        'push constant 218' ,
        'pop static 1'      ,
        'goto WHILE_EXP2'   ,
        'label WHILE_END2'  ,
        'goto WHILE_EXP1'   ,
        'label WHILE_END1'  ,
        'goto WHILE_EXP0'   ,
        'label WHILE_END0'
    ]
}
