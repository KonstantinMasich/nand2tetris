from lexer import *
from jack_compiler import Compiler
from compiler_test_setups.class_testing_configs import *
from compiler_test_setups.subroutine_testing_configs import *
from compiler_test_setups.statement_testing_configs import *
from compiler_test_setups.expression_testing_config import *


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                   TEST: CLASSES                                            ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
def test_compile_class():
    for code, correct_ans in TEST__COMPILE_CLASS.items():
        comp = Compiler(tokenize(code), '')
        comp.compile_class()
        for attr in ('symbols', 'classname', 'res'):
            assert getattr(comp, attr) == correct_ans[attr]
        assert comp.tokens[comp.i - 1][0] == '}'
        assert comp.curr is None


def test_compile_class_var_dec():
    """Verifies that the compiler builds a correct symbol table for class attributes."""
    for code, correct_ans in TEST__COMPILE_CLASS_VAR_DEC.items():
        comp = Compiler(tokenize(code), '')
        comp.compile_class_var_dec()
        assert comp.symbols == correct_ans
        assert comp.tokens[comp.i - 1][0] == ';'
        assert comp.curr is None


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                 TEST: SUBROUTINES                                          ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
def test_compile_parameters_list():
    for code, correct_ans in TEST__COMPILE_PARAMETERS_LIST.items():
        comp = Compiler(tokenize(code), '')
        comp.symbols['foo'] = {'args': {}, 'locals': {}}
        comp.scope = 'foo'
        comp.compile_parameters_list('function')
        assert comp.symbols == correct_ans
        assert comp.tokens[comp.i - 1][0] == ')'
        assert comp.curr is None


def test_compile_subroutine_body():
    for code, correct_ans in TEST__COMPILE_SUBROUTINE_BODY.items():
        comp = Compiler(tokenize(code), '')
        comp.symbols['foo'] = {'args': {}, 'locals': {}}
        comp.classname, comp.scope = 'Main', 'foo'
        comp.compile_subroutine_body('function', 'foo')
        for attr in ('symbols', 'res'):
            assert getattr(comp, attr) == correct_ans[attr]
        assert comp.tokens[comp.i - 1][0] == '}'
        assert comp.curr is None


def test_compile_subroutine_dec():
    for code, correct_ans in TEST__COMPILE_SUBROUTINE_DEC.items():
        comp = Compiler(tokenize(code), '')
        comp.classname = 'Main'
        comp.compile_subroutine_dec()
        for attr in ('symbols', 'res'):
            assert getattr(comp, attr) == correct_ans[attr]
        assert comp.tokens[comp.i - 1][0] == '}'
        assert comp.curr is None


def test_compile_subroutine_call():
    __run_tests(TEST__COMPILE_SUBROUTINE_CALL_FOO, Compiler.compile_subroutine_call,
                symbols=CONFIG__SYMBOLS_SUBROUTINE, classname='Main', scope='foo',
                last=None, before_last=')')
    __run_tests(TEST__COMPILE_SUBROUTINE_CALL_BAR, Compiler.compile_subroutine_call,
                symbols=CONFIG__SYMBOLS_SUBROUTINE, classname='Main', scope='bar',
                last=None, before_last=')')


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                  TEST: STATEMENTS                                          ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
def test_compile_let_statement():
    __run_tests(TEST__COMPILE_LET_STATEMENT, Compiler.compile_let_statement,
                symbols=CONFIG__SYMBOLS_STATEMENT, scope='foo', last=None, before_last=';')


def test_compile_do_statement():
    __run_tests(TEST__COMPILE_DO_STATEMENT, Compiler.compile_do_statement,
                symbols=CONFIG__SYMBOLS_STATEMENT)


def test_compile_if_statement():
    __run_tests(TEST__COMPILE_IF_STATEMENT, Compiler.compile_if_statement,
                symbols=CONFIG__SYMBOLS_STATEMENT, scope='foo', last=None, before_last='}')


def test_compile_while_statement():
    __run_tests(TEST__COMPILE_WHILE_STATEMENT, Compiler.compile_while_statement,
                symbols=CONFIG__SYMBOLS_STATEMENT, scope='foo', last=None, before_last='}')


def test_compile_return_statement():
    __run_tests(TEST__COMPILE_RETURN_STATEMENT, Compiler.compile_return_statement,
                symbols=CONFIG__SYMBOLS_STATEMENT, scope='foo')


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                               TEST: TERMS AND EXPRESSIONS                                  ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
def test_compile_term():
    __run_tests(TEST__COMPILE_TERM, Compiler.compile_term,
                symbols=CONFIG__SYMBOLS_SUBROUTINE, classname='Main', scope='foo')


def test_compile_expression():
    __run_tests(TEST__COMPILE_EXPRESSION, Compiler.compile_expression)


def test_compile_expression_list():
    __run_tests(TEST__COMPILE_EXPRESSION_LIST, Compiler.compile_expression_list)


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                         HELPERS                                            ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
def __run_tests(test_config: dict, f, symbols: dict = None, classname: str = None,
                scope: str = 'class', last=None, before_last='inactive'):
    for code, expected in test_config.items():
        __test_compilation(code, expected, f, symbols, classname, scope, last, before_last)


def __test_compilation(code: str, expected, f, symbols: dict = None, classname: str = None,
                       scope: str = 'class', last=None, before_last='inactive'):
    """Tokenizes and parses the code, runs the specified function with args and kwargs, and
    runs an assertion test.
    """
    comp = Compiler(tokenize(code), '')
    comp.classname, comp.symbols, comp.scope = classname, symbols, scope
    f(comp)
    assert comp.res  == expected
    assert comp.curr == last
    if before_last != 'inactive': assert comp.tokens[comp.i - 1][0] == before_last
