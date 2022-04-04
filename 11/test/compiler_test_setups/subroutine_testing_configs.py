
TEST__COMPILE_PARAMETERS_LIST = {
    '()': {'class': {}, 'foo': {'args': {}, 'locals': {}}},
    '(int a)': {
        'class': {},
        'foo'  : {
            'args'  : {
                'a': {'type': 'int', 'kind': 'argument', 'i': 0}
            },
            'locals': {}}
    },
    '(int a, Double b, String c, Array d)': {
        'class': {},
        'foo'  : {
            'args': {
                'a': {'type': 'int'   , 'kind': 'argument', 'i': 0},
                'b': {'type': 'Double', 'kind': 'argument', 'i': 1},
                'c': {'type': 'String', 'kind': 'argument', 'i': 2},
                'd': {'type': 'Array' , 'kind': 'argument', 'i': 3}
            },
            'locals': {}}
    }
}

TEST__COMPILE_SUBROUTINE_DEC = {
    'function void foo() {}': {'symbols': {'class': {}, 'foo': {'args': {}, 'locals': {}}},
                               'res': ['function Main.foo 0']},
    """function int foo(int a, Double b, String c, Array d) {
            var Point x, y; var int z;
            let z = 19;
            return y;
        }""": {
        'symbols': {
            'class': {},
            'foo'  : {
                'args': {
                    'a': {'type': 'int'   , 'kind': 'argument', 'i': 0},
                    'b': {'type': 'Double', 'kind': 'argument', 'i': 1},
                    'c': {'type': 'String', 'kind': 'argument', 'i': 2},
                    'd': {'type': 'Array' , 'kind': 'argument', 'i': 3}
                },
                'locals': {
                    'x': {'type': 'Point', 'kind': 'local', 'i': 0},
                    'y': {'type': 'Point', 'kind': 'local', 'i': 1},
                    'z': {'type': 'int'  , 'kind': 'local', 'i': 2},
                }
            }
        },
        'res': ['function Main.foo 3', 'push constant 19', 'pop local 2', 'push local 1', 'return']
    }
}

TEST__COMPILE_SUBROUTINE_BODY = {
    '{}': {
        'symbols': {'class': {}, 'foo': {'args': {}, 'locals': {}}},
        'res'    : ['function Main.foo 0']
    },
    '{var int a;}': {
        'symbols': {
            'class': {},
            'foo'  : {
                'args'  : {},
                'locals': {
                    'a': {'type': 'int', 'kind': 'local', 'i': 0}
                }
            }
        },
        'res': ['function Main.foo 1']
    },
    '{var int a, b, c; var String s1; var String s2; var Double x, y;}': {
        'symbols': {
            'class': {},
            'foo'  : {
                'args'  : {},
                'locals': {
                    'a' : {'type': 'int'   , 'kind': 'local', 'i': 0},
                    'b' : {'type': 'int'   , 'kind': 'local', 'i': 1},
                    'c' : {'type': 'int'   , 'kind': 'local', 'i': 2},
                    's1': {'type': 'String', 'kind': 'local', 'i': 3},
                    's2': {'type': 'String', 'kind': 'local', 'i': 4},
                    'x' : {'type': 'Double', 'kind': 'local', 'i': 5},
                    'y' : {'type': 'Double', 'kind': 'local', 'i': 6}
                }
            }
        },
        'res': ['function Main.foo 7']
    },
    '{var int a, b; var Double x, y; let b = 2 + 3; return 9;}': {
        'symbols': {
            'class': {},
            'foo': {
                'args': {},
                'locals': {
                    'a': {'type': 'int'   , 'kind': 'local', 'i': 0},
                    'b': {'type': 'int'   , 'kind': 'local', 'i': 1},
                    'x': {'type': 'Double', 'kind': 'local', 'i': 2},
                    'y': {'type': 'Double', 'kind': 'local', 'i': 3}
                }
            }
        },
        'res': ['function Main.foo 4', 'push constant 2', 'push constant 3', 'add',
                'pop local 1', 'push constant 9', 'return']
    },
    '{var Array x; let x = Array.new(10); let x[7] = 18; return 1010;}': {
        'symbols': {
            'class': {},
            'foo'  : {
                'args': {},
                'locals': {
                    'x' : {'type': 'Array', 'kind': 'local', 'i': 0},
                }
            }
        },
        'res': [
            'function Main.foo 1',
            'push constant 10'   ,
            'call Array.new 1'   ,
            'pop local 0'        ,
            'push constant 7'    ,
            'push local 0'       ,
            'add'                ,
            'push constant 18'   ,
            'pop temp 0'         ,
            'pop pointer 1'      ,
            'push temp 0'        ,
            'pop that 0'         ,
            'push constant 1010' ,
            'return'
        ]
    }
}


TEST__COMPILE_SUBROUTINE_CALL_FOO = {
    'foo()'       : ['push pointer 0', 'call Main.foo 1'],
    'Main.foo(z)' : ['push local 2', 'call Main.foo 1'],
    'foo(x, y, z)': [
        'push pointer 0' ,
        'push local 0'   ,
        'push local 1'   ,
        'push local 2'   ,
        'call Main.foo 4'
    ],
    'Math.foo(a, c, b, M, G)': [
        'push this 0'    ,
        'push this 2'    ,
        'push this 1'    ,
        'push static 1'  ,
        'push static 0'  ,
        'call Math.foo 5'
    ],
}

TEST__COMPILE_SUBROUTINE_CALL_BAR = {
    'Main.bar()': [
        'call Main.bar 0'
    ],
    'Other.bar(a, c, 2, M, G)': [
        'push this 0'    ,
        'push this 2'    ,
        'push constant 2',
        'push static 1'  ,
        'push static 0'  ,
        'call Other.bar 5'
    ],
}

# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
CONFIG__SYMBOLS_SUBROUTINE = {
    'class': {
        'a': {'type': 'int'    , 'kind': 'this'  , 'i': 0},
        'b': {'type': 'String' , 'kind': 'this'  , 'i': 1},
        'c': {'type': 'boolean', 'kind': 'this'  , 'i': 2},
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
