TEST__COMPILE_CLASS = {
    """class Main {}""": {
        'symbols'  : {'class': {}},
        'classname': 'Main',
        'res'      : []
    },
    """class Main {function void main() {do Output.printInt(1 + (2 * 3));return;}""": {
        'symbols'  : {'class': {}, 'main': {'args': {}, 'locals': {}}},
        'classname': 'Main',
        'res'      : [
            'function Main.main 0'  ,
            'push constant 1'       ,
            'push constant 2'       ,
            'push constant 3'       ,
            'call Math.multiply 2'  ,
            'add'                   ,
            'call Output.printInt 1',
            'pop temp 0'            ,
            'push constant 0'       ,
            'return'
        ]
    }
}

TEST__COMPILE_CLASS_VAR_DEC = {
    """field int a;""": {
        'class': {
            'a': {'type': 'int', 'kind': 'this', 'i': 0}
        }
    },
    """field int a,b,c;""": {
        'class': {
            'a': {'type': 'int', 'kind': 'this', 'i': 0},
            'b': {'type': 'int', 'kind': 'this', 'i': 1},
            'c': {'type': 'int', 'kind': 'this', 'i': 2}
        }
    },
    """field int a; field Array arr; field String s;""": {
        'class': {
            'a'  : {'type': 'int'   , 'kind': 'this' , 'i': 0},
            'arr': {'type': 'Array' , 'kind': 'this' , 'i': 1},
            's'  : {'type': 'String', 'kind': 'this' , 'i': 2}
        }
    },
    """field int a; static Double x,y,z; field String s1, s2; static Array arr1, arr2;""": {
        'class': {
            'a'   : {'type': 'int'   , 'kind': 'this'  , 'i': 0},
            'x'   : {'type': 'Double', 'kind': 'static', 'i': 0},
            'y'   : {'type': 'Double', 'kind': 'static', 'i': 1},
            'z'   : {'type': 'Double', 'kind': 'static', 'i': 2},
            's1'  : {'type': 'String', 'kind': 'this'  , 'i': 1},
            's2'  : {'type': 'String', 'kind': 'this'  , 'i': 2},
            'arr1': {'type': 'Array' , 'kind': 'static', 'i': 3},
            'arr2': {'type': 'Array' , 'kind': 'static', 'i': 4}
        }
    }
}
