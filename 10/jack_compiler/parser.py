# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
from lxml import etree
import re
from config import *


class Parser:
    """
    Parser (syntax analyzer).

    Gets input from lexer in the form of [(token, token_type), (token, token_type), ...] and
    builds parse tree; optionally writes parse tree into XML file.
   """

    def __init__(self, tokens: list, fname: str):
        self.tokens  = tokens                  # A list of pairs [['class': 'keyword'], [_, _],...]
        self.n       = len(tokens)             # Total amount of tokens
        self.i       = 0                       # Current token index
        self.root    = etree.Element('class')  # Root element of parsing tree
        self.fname   = fname                   # Output filename
        self.__PARSE_STATEMENT_METHODS = {
            'let'   : self._parse_let_statement   ,
            'do'    : self._parse_do_statement    ,
            'while' : self._parse_while_statement ,
            'if'    : self._parse_if_statement    ,
            'return': self._parse_return_statement
        }

    def parse(self, unwrap_tags: bool = False):
        """Parses the entire file and outputs its structure into the specified file."""
        self._parse_class(self.root)
        if self.fname:
            xml_str = etree.tostring(self.root, pretty_print=True).decode('utf-8')
            xml_str = Parser.unwrap_tags(xml_str)
            with open(self.fname, 'w') as xml_file:
                xml_file.write(xml_str)

    # ----------------------------------------------------------------------------------------------
    #                     Properties (shorthand, for convenience)
    # current token's (tokens[i]) value and type; and the next token's value, i.e. tokens[i+1]
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
    # ║                                 CLASS AND CLASS VARS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_class(self, node):
        self.__write_terminals(3, node)                            # Class Main {
        while self.curr in ('static', 'field'):                    # class fields declarations
            self._parse_class_var_dec(node)
        while self.curr in ('constructor', 'function', 'method'):  # functions declarations
            self._parse_subroutine_dec(node)
        self.__write_terminals(1, node)                            # {

    def _parse_class_var_dec(self, node):
        inner_node = etree.SubElement(node, 'classVarDec')
        self.__write_terminals(3, inner_node)      # field int x
        while self.curr == ',':
            self.__write_terminals(2, inner_node)  # , y, z
        self.__write_terminals(1, inner_node)      # ;

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_parameter_list(self, node):
        inner_node = etree.SubElement(node, 'parameterList')
        if self.curr != ')':
            self.__write_terminals(2, inner_node)      # int x
            while self.curr == ',':
                self.__write_terminals(3, inner_node)  # , int y, int z

    def _parse_var_dec(self, node):
        inner_node = etree.SubElement(node, 'varDec')
        self.__write_terminals(3, inner_node)      # var int x
        while self.curr == ',':
            self.__write_terminals(2, inner_node)  # , y, z
        self.__write_terminals(1, inner_node)      # ;

    def _parse_subroutine_dec(self, node):
        inner_node = etree.SubElement(node, 'subroutineDec')
        self.__write_terminals(4, inner_node)    # function int Foo (
        self._parse_parameter_list(inner_node)   # parameters list
        self.__write_terminals(1, inner_node)    # )
        self._parse_subroutine_body(inner_node)  # { subroutine body }

    def _parse_subroutine_body(self, node):
        inner_node = etree.SubElement(node, 'subroutineBody')
        self.__write_terminals(1, inner_node)  # {
        while self.curr == 'var':
            self._parse_var_dec(inner_node)    # var declarations
        self._parse_statements(inner_node)     # statements
        self.__write_terminals(1, inner_node)  # }

    def _parse_subroutine_call(self, node):
        # Simply parse "foo(" which is 2 terminals, or "Bar.foo(" which is 4 terminals:
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
            xml_str = xml_str.replace(f'<{tag}/>', f'<{tag}>\n</{tag}>')
        return xml_str
