import xml.etree.ElementTree as etree
from .const import T_OP, T_UNARY_OP, TokenType

# ╔══════════════════════╗
# ║ Python version: 3.11 ║
# ╚══════════════════════╝


class Parser:
    """
    Parser (syntax analyzer).

    Gets input from lexer in the form of [(token, token_type), (token, token_type), ...] and
    builds parse tree; optionally writes parse tree into XML file.
    """

    def __init__(self, tokens: list[tuple]):
        self.tokens  = tokens       # Token stream
        self.tok_len = len(tokens)  # Total amount of tokens
        self.i       = 0            # Current token index
        self.statements_parsing_methods = {
            'let'   : self._parse_let_statement   ,
            'do'    : self._parse_do_statement    ,
            'while' : self._parse_while_statement ,
            'if'    : self._parse_if_statement    ,
            'return': self._parse_return_statement
        }

    # ----------------------------------------------------------------------------------------------
    # Cursor property.
    # This is a shorthand for the current token being pointed at by self.tokens[self.i], and
    # for the next token, i.e. self.tokens[self.i + 1]
    @property
    def cur(self):
        return self.tokens[self.i]

    @property
    def cur_tok(self):
        return self.tokens[self.i][0]

    @property
    def next_tok(self):
        return self.tokens[self.i + 1][0] if self.i < self.tok_len - 1 else None
    # ----------------------------------------------------------------------------------------------

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                 CLASS AND CLASS VARS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def parse_class(self) -> etree.Element:
        node = etree.Element('class')
        self._add_tokens_and_advance(node, 3)                         # Class Main {
        while self.cur_tok in {'static', 'field'}:                    # class fields declarations
            node.append(self._parse_class_var_dec())                 
        while self.cur_tok in {'constructor', 'function', 'method'}:  # subroutines
            node.append(self._parse_subroutine_dec())
        self._add_tokens_and_advance(node, 1)                         # }
        return node

    def _parse_class_var_dec(self) -> etree.Element:
        node = etree.Element('classVarDec')
        self._add_tokens_and_advance(node, 3)      # field int varName
        while self.cur_tok == ',':
            self._add_tokens_and_advance(node, 2)  # , y, z
        self._add_tokens_and_advance(node, 1)      # ;
        return node

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                      STATEMENTS                                            ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_statements(self) -> etree.Element:
        node = etree.Element('statements')
        while parse_method := self.statements_parsing_methods.get(self.cur_tok):
            node.append(parse_method())
        return node

    def _parse_let_statement(self) -> etree.Element:
        node = etree.Element('letStatement')
        self._add_tokens_and_advance(node, 2)      # let varname
        if self.cur_tok == '[':
            self._add_tokens_and_advance(node, 1)  # [
            node.append(self._parse_expression())  # expression
            self._add_tokens_and_advance(node, 1)  # ]
        self._add_tokens_and_advance(node, 1)      # =
        node.append(self._parse_expression())      # expression
        self._add_tokens_and_advance(node, 1)      # ;
        return node

    def _parse_if_statement(self) -> etree.Element:
        node = etree.Element('ifStatement')
        self._add_tokens_and_advance(node, 2)      # if (
        if self.cur_tok != ')':
            node.append(self._parse_expression())  # expression
        self._add_tokens_and_advance(node, 2)      # ) {
        node.append(self._parse_statements())      # statements
        self._add_tokens_and_advance(node, 1)      # }
        if self.cur_tok == 'else':
            self._add_tokens_and_advance(node, 2)  # else {
            node.append(self._parse_statements())  # statements
            self._add_tokens_and_advance(node, 1)  # }
        return node

    def _parse_while_statement(self) -> etree.Element:
        node = etree.Element('whileStatement')
        self._add_tokens_and_advance(node, 2)      # while (
        if self.cur_tok != ')':
            node.append(self._parse_expression())  # expression
        self._add_tokens_and_advance(node, 2)      # ) {
        node.append(self._parse_statements())      # statements
        self._add_tokens_and_advance(node, 1)      # }
        return node

    def _parse_do_statement(self) -> etree.Element:
        node = etree.Element('doStatement')
        self._add_tokens_and_advance(node, 1)  # do
        self._parse_subroutine_call(node)      # Bar.foo(params)
        self._add_tokens_and_advance(node, 1)  # ;
        return node

    def _parse_return_statement(self):
        node = etree.Element('returnStatement')
        self._add_tokens_and_advance(node, 1)      # return
        if self.cur_tok != ';':
            node.append(self._parse_expression())  # expression
        self._add_tokens_and_advance(node, 1)      # ;
        return node

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_parameter_list(self) -> etree.Element:
        node = etree.Element('parameterList')
        if self.cur_tok != ')':
            self._add_tokens_and_advance(node, 2)      # int x
            while self.cur_tok == ',':
                self._add_tokens_and_advance(node, 3)  # , int y, int z
        return node

    def _parse_var_dec(self) -> etree.Element:
        node = etree.Element('varDec')
        self._add_tokens_and_advance(node, 3)      # var int x
        while self.cur_tok == ',':
            self._add_tokens_and_advance(node, 2)  # , y, z
        self._add_tokens_and_advance(node, 1)      # ;
        return node

    def _parse_subroutine_body(self) -> etree.Element:
        node = etree.Element('subroutineBody')
        self._add_tokens_and_advance(node, 1)   # {
        while self.cur_tok == 'var':
            node.append(self._parse_var_dec())  # var declarations
        node.append(self._parse_statements())   # statements
        self._add_tokens_and_advance(node, 1)   # }
        return node

    def _parse_subroutine_dec(self) -> etree.Element:
        node = etree.Element('subroutineDec')
        self._add_tokens_and_advance(node, 4)       # function int Foo (
        node.append(self._parse_parameter_list())   # parameters list
        self._add_tokens_and_advance(node, 1)       # )
        node.append(self._parse_subroutine_body())  # { subroutine body }
        return node

    def _parse_subroutine_call(self, node):
        self._add_tokens_and_advance(node, 2 if self.next_tok == '(' else 4)  # foo( or Bar.foo(
        node.append(self._parse_expression_list())                            # expressions
        self._add_tokens_and_advance(node, 1)                                 # )

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                 TERMS AND EXPRESSIONS                                      ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _parse_expression(self) -> etree.Element:
        node = etree.Element('expression')
        node.append(self._parse_term())            # term
        while self.cur_tok in T_OP:
            self._add_tokens_and_advance(node, 1)  # operator
            node.append(self._parse_term())        # term
        return node

    def _parse_expression_list(self) -> etree.Element:
        node = etree.Element('expressionList')
        if self.cur_tok != ')':
            node.append(self._parse_expression())      # expression
            while self.cur[0] == ',':
                self._add_tokens_and_advance(node, 1)  # ,
                node.append(self._parse_expression())  # expression
        return node

    def _parse_term(self) -> etree.Element:
        node = etree.Element('term')
        token, token_type = self.cur
        match token_type:
            # Integer, string constant, or keyword:
            case TokenType.INTEGER | TokenType.STR_CONST | TokenType.KEYWORD:
                self._add_tokens_and_advance(node, 1)
            # Identifier:
            case TokenType.IDENTIFIER:
                match self.next_tok:
                    # varName [ expression ]
                    case '[':
                        self._add_tokens_and_advance(node, 2)  # varName [
                        node.append(self._parse_expression())
                        self._add_tokens_and_advance(node, 1)  # ]
                    # Subroutine call like foo(params) or Foo.bar(params)
                    case '(' | '.':
                        self._parse_subroutine_call(node)
                    # varName
                    case _:
                        self._add_tokens_and_advance(node, 1)
            # ( expression )
            case TokenType.SYMBOL:
                match token:
                    case '(':
                        self._add_tokens_and_advance(node, 1)  # (
                        node.append(self._parse_expression())  # expression
                        self._add_tokens_and_advance(node, 1)  # )
                    case _ if token in T_UNARY_OP:
                        self._add_tokens_and_advance(node, 1)  # unary operator
                        node.append(self._parse_term())
                    case _:
                        raise AttributeError(f'Unexpected token: {token}')
        return node

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                          UTILS                                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _add_tokens_and_advance(self, parent_node, n: int = 1):
        """
        Adds N tokens to the specified parent node, and moves the
        cursor N positions forward.
        """
        for _ in range(n):
            token, token_type = self.cur
            new_node = etree.SubElement(parent_node, token_type.value)
            new_node.text = f' {token} '
            self.i += 1 if self.i < (self.tok_len - 1) else 0

    @staticmethod
    def fill_empty_tags(node: etree.Element):
        """Recursively fills XML tree elements with a whitespace if they contain
        no text. This is needed because empty tags looks like <expressionList />,
        but the course files expect the form <expressionList> </expressionList>.
        """
        for inner_node in list(node):
            if not inner_node.text:
                inner_node.text = '\n'
            Parser.fill_empty_tags(inner_node)

    @staticmethod
    def get_pretty_string(node: etree.Element) -> str:
        """Returns indented XML string as built from the specified node."""
        etree.indent(node)
        return etree.tostring(node).decode('utf-8')

    @staticmethod
    def to_xml(tree_root_node: etree.Element, xml_fname: str):
        """Writes the provided parse tree into a file."""
        Parser.fill_empty_tags(tree_root_node)
        with open(xml_fname, 'w') as xml_file:
            xml_file.write(Parser.get_pretty_string(tree_root_node))
