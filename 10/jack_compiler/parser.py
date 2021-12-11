# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
from lxml import etree
import re
from config import *


class Parser:

    def __init__(self, tokens: list, fname: str):
        self.tokens = tokens                  # A list of pairs [['class': 'keyword'], [_, _], ...]
        self.n      = len(tokens)             # Total amount of tokens
        self.i      = 0                       # Current token index
        self.tree   = etree.ElementTree()     # Parsing tree in the form of XML
        self.root   = etree.Element('class')  # Root element of parsing tree
        self.fname  = fname                   # Output filename
        self.__PARSE_STATEMENT_METHODS = {
            'let'   : self._parse_let_statement   ,
            'do'    : self._parse_do_statement    ,
            'while' : self._parse_while_statement ,
            'if'    : self._parse_if_statement    ,
            'return': self._parse_return_statement
        }

    def parse(self, unwrap_tags: bool = False):
        """Parses the entire file and outputs its structure into the specified file."""
        # TODO : add unwrapping tags and update description
        self._parse_class()
        if self.fname:
            self.tree.write('check.xml')

    # ----------------------------------------------------------------------------------------------
    #                     Properties (shorthand, for convenience)
    # current token's (tokens[i]) value and type; and next token's value, i.e. tokens[i+1]
    @property
    def curr(self):
        return self.tokens[self.i][0]

    @property
    def curr_type(self):
        return self.tokens[self.i][1]

    @property
    def next(self):
        return self.tokens[self.i + 1][0] if self.i < self.n - 1 else ''
    # ----------------------------------------------------------------------------------------------

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                          "HIGH" LEVEL COMPILATION METHODS                                  ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_class(self):
        inner_node = self.root

    # def _compile_class(self):
    #     self.__write_terminals(3)  # class Main {
    #     while self.curr in ('static', 'field'):
    #         self._compile_class_var_dec()
    #     while self.curr in ('constructor', 'function', 'method'):
    #         self._compile_subroutine_dec()
    #     self.__write_terminals(1)  # }
    #
    # def _compile_class_var_dec(self):
    #     inner_node = SubElement(self.root, 'classVarDec')
    #     n = self.__find_next(';')
    #     self.__write_terminals(n+1, inner_node)  # expressions ;
    #
    # def _compile_subroutine_dec(self):
    #     node = SubElement(self.root, 'subroutineDec')
    #     self.__write_terminals(4, node)  # function String foo (
    #     self._compile_parameter_list(node)
    #     self.__write_terminals(2, node)  # ) and {
    #     self._compile_subroutine()
    #     self.__write_terminals(1, node)  # }
    #
    # def _compile_parameter_list(self, node):
    #     inner_node = SubElement(node, 'parameterList')
    #     n = self.__find_next(')')
    #     self.__write_terminals(n, inner_node)
    #
    # def _compile_var_dec(self, node):
    #     inner_node = SubElement(node, 'varDec')
    #     self.__write_terminals(1, inner_node)  # var
    #     n = self.__find_next(';')
    #     self.__write_terminals(n+1, inner_node)  # ;
    #
    # def _compile_subroutine(self):
    #     node = SubElement(self.root, 'subroutineBody')
    #     while self.curr == 'var':
    #         self._compile_var_dec(node)
    #     statements_node = SubElement(node, 'statements')
    #     while self.curr != '}':
    #         self._compile_statements(statements_node)
    #
    # # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # # ║                         "MIDDLE" LEVEL COMPILATION METHODS                                 ║
    # # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    # def _compile_statements(self, node):
    #     self.__CMP_METHODS[self.tokens[self.i][0]](node)

    def _parse_subroutine_call(self, node):
        # Parse "foo(" which is 2 terminals, or "Bar.foo(" which is 4 terminals:
        self.__write_terminals(2 if self.next == '(' else 4, node)  # foo( or Bar.foo(
        self._parse_expression_list(node)                           # expressions
        self.__write_terminals(1, node)                             # )

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                     STATEMENTS                                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_statements(self, node):
        inner_node = etree.SubElement(node, 'statements')
        while self.curr in self.__PARSE_STATEMENT_METHODS:
            self.__PARSE_STATEMENT_METHODS[self.curr](inner_node)

    def _parse_let_statement(self, node):
        inner_node = etree.SubElement(node, 'letStatement')
        self.__write_terminals(2, inner_node)      # let varname =
        if self.curr == '[':
            self.__write_terminals(1, inner_node)  # [
            self._parse_expression(inner_node)     # expression
            self.__write_terminals(1, inner_node)  # ]
        self.__write_terminals(1, inner_node)      # =
        self._parse_expression(inner_node)         # 2
        self.__write_terminals(1, inner_node)      # ;

    def _parse_if_statement(self, node):
        inner_node = etree.SubElement(node, 'ifStatement')
        self.__write_terminals(2, inner_node)       # if (
        if self.curr != ')':
            self._parse_expression(inner_node)      # expression
        self.__write_terminals(2, inner_node)       # ) {
        if self.curr != '{':
            self._parse_statements(inner_node)      # statements
        self.__write_terminals(1, inner_node)       # }
        if self.curr == 'else':
            self.__write_terminals(2, inner_node)   # else {
            if self.curr != '}':
                self._parse_statements(inner_node)  # statements
            self.__write_terminals(1, inner_node)   # }

    def _parse_while_statement(self, node):
        inner_node = etree.SubElement(node, 'whileStatement')
        self.__write_terminals(2, inner_node)   # while (
        if self.curr != ')':
            self._parse_expression(inner_node)  # expression
        self.__write_terminals(2, inner_node)   # ) {
        self._parse_statements(inner_node)      # statements
        self.__write_terminals(1, inner_node)   # }

    def _parse_do_statement(self, node):
        inner_node = etree.SubElement(node, 'doStatement')
        self.__write_terminals(1, inner_node)    # do
        self._parse_subroutine_call(inner_node)  # Bar.foo(params)
        self.__write_terminals(1, inner_node)    # ;

    def _parse_return_statement(self, node):
        inner_node = etree.SubElement(node, 'returnStatement')
        self.__write_terminals(1, inner_node)    # return
        if self.curr != ';':
            self._parse_expression(inner_node)   # expression
        self.__write_terminals(1, inner_node)    # ;

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                TERMS AND EXPRESSIONS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_expression(self, node):
        inner_node = etree.SubElement(node, 'expression')
        self._parse_term(inner_node)
        while self.curr in T_OP:
            self.__write_terminals(1, inner_node)
            self._parse_term(inner_node)

    def _parse_expression_list(self, node):
        inner_node = etree.SubElement(node, 'expressionList')
        if self.curr != ')':
            self._parse_expression(inner_node)
            while self.curr == ',':
                self.__write_terminals(1, inner_node)  # ,
                self._parse_expression(inner_node)

    def _parse_term(self, node):
        inner_node = etree.SubElement(node, 'term')
        # Integer / string constant /:
        if self.curr_type in ('integerConstant', 'stringConstant', 'keyword'):
            self.__write_terminals(1, inner_node)
        elif self.curr_type == 'identifier':
            # varName [ expression ]
            if self.next == '[':
                self.__write_terminals(2, inner_node)  # varName [
                self._parse_expression(inner_node)     # expression
                self.__write_terminals(1, inner_node)  # ]
            # Subroutine call like bark(params) or Dog.bark(params)
            elif self.next in ('(', '.'):
                self._parse_subroutine_call(inner_node)
            # varName
            else:
                self.__write_terminals(1, inner_node)
        # ( expression )
        elif self.curr == '(':
            self.__write_terminals(1, inner_node)  # (
            self._parse_expression(inner_node)     # expression
            self.__write_terminals(1, inner_node)  # )
        # unaryOp term
        elif self.curr in T_UNARY_OP:
            self.__write_terminals(1, inner_node)  # unary_op
            self._parse_term(inner_node)           # term

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                         HELPERS                                            ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def __write_terminals(self, n: int, node: etree.SubElement = None):
        """Writes n terminals into a tree with their tags as they are, and moves
        the current token index by n positions up."""
        for idx in range(self.i, self.i+n):
            token, t_type = self.tokens[idx][0], self.tokens[idx][1]
            node = self.root if node is None else node
            etree.SubElement(node, t_type).text = f' {token} '
            if self.i < (len(self.tokens) - 1):
                self.i += 1

    @staticmethod
    def unwrap_tags(xml_str: str):
        """Returns an "unwrapped" XML string, where tags like <term/> are turned into
        explicit form of <term></term>, because that's what nand2tetris works with.
        """
        for tag in re.findall(RE_WRAPPED_TAGS, xml_str):
            xml_str = xml_str.replace(f'<{tag}/>', f'<{tag}></{tag}>')
        return xml_str

    # def __find_next(self, key):
    #     """Returns the amount of symbols one needs to "hop" over in order to get to the key,
    #     or None."""
    #     n = 0
    #     try:
    #         if isinstance(key, list) or isinstance(key, tuple):
    #             while self.tokens[self.i + n][0] not in key:
    #                 n += 1
    #         else:
    #             while self.tokens[self.i + n][0] != key:
    #                 n += 1
    #         return n
    #     except IndexError:
    #         return None
