from lxml import etree
from lexer import tokenize
import json
from parser import Parser
from test_configuration import *
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
    def test_bar(self):
        with open('test_config_parser.json') as json_file:
            data = json.load(json_file)
            print(data)

    def test_foo(self):
        code   = 'if (((y + size) < 254) & ((x + size) < 510)) { do erase(); }'
        tokens = tokenize(code)
        p = Parser(tokens, '')
        print(tokens)
        p._parse_subroutine_call(p.root)
        res = etree.tostring(p.root, pretty_print=True).decode('utf-8')
        res = Parser.unwrap_tags(res)
        print(res)
        self.assertTrue(True)
        # s = """
        # <class><identifier>foo</identifier><symbol>(</symbol><expressionList/><symbol>)</symbol></class><>
        # <term></term>
        # <term/>
        # <parametersList></parametersList>
        # <parametersList/>
        # """
        # print(Parser.unwrap_tags(s))

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
        actual   = etree.tostring(parser.root, pretty_print=True).decode('utf-8').replace('\n', '').replace(' ', '')
        actual   = Parser.unwrap_tags(actual)
        expected = expected.replace('\n', '').replace(' ', '')
        if verbose:
            print(etree.tostring(parser.root, pretty_print=True).decode('utf-8'))
        # 3. Assert equality:
        self.maxDiff = None
        self.assertEqual(expected, actual, f'\n{"-"*50}\nFAILED to parse code:\n{code}\n{"-"*50}')


if __name__ == '__main__':
    unittest.main()
