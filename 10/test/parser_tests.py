from lxml import etree
from lexer import tokenize
from parser import Parser
from test_config import *
import unittest


class ParserTests(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    #                            TEST: TERMS AND EXPRESSIONS
    def test_parse_term(self):
        self.__run_tests(CONFIG__PARSE_TERM, Parser._parse_term)

    def test_parse_expression(self):
        self.__run_tests(CONFIG__PARSE_EXPRESSION, Parser._parse_expression)

    def test_parse_subroutine_call(self):
        self.__run_tests(CONFIG__PARSE_SUBROUTINE_CALL, Parser._parse_subroutine_call)
    # -----------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------
    #                               TEST: STATEMENTS
    def test_parse_let_statement(self):
        self.__run_tests(CONFIG__PARSE_LET_STATEMENT, Parser._parse_let_statement)

    def test_parse_do_statement(self):
        self.__run_tests(CONFIG__PARSE_DO_STATEMENT, Parser._parse_do_statement)

    def test_parse_if_statement(self):
        self.__run_tests(CONFIG__PARSE_IF_STATEMENT, Parser._parse_if_statement)

    def test_parse_return_statement(self):
        self.__run_tests(CONFIG__PARSE_RETURN_STATEMENT, Parser._parse_return_statement)

    def test_parse_while_statement(self):
        self.__run_tests(CONFIG__PARSE_WHILE_STATEMENT, Parser._parse_while_statement)
    # -----------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------
    #                 TEST: VARIABLES AND SUBROUTINES - DECLARATION AND CALL
    def test_subroutine_dec(self):
        self.__run_tests(CONFIG__PARSE_SUBROUTINE_DEC, Parser._parse_subroutine_dec)

    def test_parse_subroutine_body(self):
        self.__run_tests(CONFIG__PARSE_SUBROUTINE_BODY, Parser._parse_subroutine_body)

    def test_parse_parameter_list(self):
        self.__run_tests(CONFIG__PARSE_PARAMETER_LIST, Parser._parse_parameter_list)

    def test_parse_var_dec(self):
        self.__run_tests(CONFIG__PARSE_VAR_DEC, Parser._parse_var_dec)
    # -----------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------
    #                 TEST: VARIABLES AND SUBROUTINES - DECLARATION AND CALL
    def test_parse_class_var_dec(self):
        self.__run_tests(CONFIG__PARSE_CLASS_VAR_DEC, Parser._parse_class_var_dec)

    def test_parse_class(self):
        self.__run_tests(CONFIG__PARSE_CLASS, Parser._parse_class)
    # -----------------------------------------------------------------------------------

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                         HELPERS                                            ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def __run_tests(self, test_config: dict, f):
        for code, expected in test_config.items():
            self.__test_parser_func(code, expected, f)

    def __test_parser_func(self, code: str, expected, f, verbose: bool = False):
        """Tokenizes and parses the code, runs the specified function with args and kwargs, and
        runs an assertion test.
        """
        # 1. Tokenize and call the tested method:
        parser = Parser(tokenize(code), '')
        f(parser, node=parser.root)
        # 2. Transform actual and expected strings to the same representation (string with
        #    no newlines and whitespaces):
        actual   = etree.tostring(parser.root, pretty_print=True).decode('utf-8').replace(' ', '')
        actual   = Parser.unwrap_tags(actual).replace('\n', '')
        expected = expected.replace('\n', '').replace(' ', '')
        if verbose:
            print(etree.tostring(parser.root, pretty_print=True).decode('utf-8'))
        # 3. Assert equality:
        self.maxDiff = None
        self.assertEqual(expected, actual, f'\n{"-"*50}\nFAILED to parse code:\n{code}\n{"-"*50}')


if __name__ == '__main__':
    unittest.main()
