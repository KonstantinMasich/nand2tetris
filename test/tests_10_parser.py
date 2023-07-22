import xml.etree.ElementTree as etree
import glob
from p10.code.parser import Parser
from p10.code.lexer import tokenize
from test_utils.commons import parametrize, are_identical_files
import test_utils.test_configs_10__parser_term  as term_test_configs
import test_utils.test_configs_10__parser_stmt  as stmt_test_configs
import test_utils.test_configs_10__parser_mid   as mid_test_configs
import test_utils.test_configs_10__parser_class as class_test_configs

# try:
#     assert are_identical_nodes(expected, node)
# except AssertionError:
#     print()
#     etree.indent(node)
#     print(etree.tostring(node).decode('utf-8'))
#     print()
#     etree.indent(expected)
#     print(etree.tostring(expected).decode('utf-8'))


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                 CLASS AND CLASS VARS                                       ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
@parametrize(class_test_configs.TESTDATA__PARSE_CLASS)
def test_parse_class(tokens, expected):
    node = Parser(tokens).parse_class()
    assert are_identical_nodes(expected, node)


@parametrize(class_test_configs.TESTDATA__PARSE_CLASS_VAR_DEC)
def test_parse_class_var_dec(tokens, expected):
    node = Parser(tokens)._parse_class_var_dec()
    assert are_identical_nodes(expected, node)


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       STATEMENTS                                           ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
@parametrize(stmt_test_configs.TESTDATA__PARSE_LET_STATEMENT)
def test_parse_let_statement(tokens, expected):
    node = Parser(tokens)._parse_let_statement()
    assert are_identical_nodes(expected, node)
    # try:
    #     assert are_identical_nodes(expected, node)
    # except AssertionError:
    #     print()
    #     etree.indent(node)
    #     print(etree.tostring(node).decode('utf-8'))
    #     print()
    #     etree.indent(expected)
    #     print(etree.tostring(expected).decode('utf-8'))


@parametrize(stmt_test_configs.TESTDATA__PARSE_IF_STATEMENT)
def test_parse_if_statement(tokens, expected):
    node = Parser(tokens)._parse_if_statement()
    assert are_identical_nodes(expected, node)


@parametrize(stmt_test_configs.TESTDATA__PARSE_WHILE_STATEMENT)
def test_parse_while_statement(tokens, expected):
    node = Parser(tokens)._parse_while_statement()
    assert are_identical_nodes(expected, node)


@parametrize(stmt_test_configs.TESTDATA__PARSE_DO_STATEMENT)
def test_parse_do_statement(tokens, expected):
    node = Parser(tokens)._parse_do_statement()
    assert are_identical_nodes(expected, node)


@parametrize(stmt_test_configs.TESTDATA__PARSE_RETURN_STATEMENT)
def test_parse_return_statement(tokens, expected):
    node = Parser(tokens)._parse_return_statement()
    assert are_identical_nodes(expected, node)


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
@parametrize(mid_test_configs.TESTDATA__PARSE_PARAMETER_LIST)
def test_parse_parameter_list(tokens, expected):
    node = Parser(tokens)._parse_parameter_list()
    assert are_identical_nodes(expected, node)


@parametrize(mid_test_configs.TESTDATA__PARSE_VAR_DEC)
def test_parse_var_dec(tokens, expected):
    node = Parser(tokens)._parse_var_dec()
    assert are_identical_nodes(expected, node)


@parametrize(mid_test_configs.TESTDATA__PARSE_SUBROUTINE_BODY)
def test_parse_subroutine_body(tokens, expected):
    node = Parser(tokens)._parse_subroutine_body()
    assert are_identical_nodes(expected, node)


@parametrize(mid_test_configs.TESTDATA__PARSE_SUBROUTINE_DEC)
def test_parse_subroutine_dec(tokens, expected):
    node = Parser(tokens)._parse_subroutine_dec()
    assert are_identical_nodes(expected, node)


@parametrize(mid_test_configs.TESTDATA__PARSE_SUBROUTINE_CALL)
def test_parse_subroutine_call(tokens, expected):
    node = etree.Element('__temp__')
    Parser(tokens)._parse_subroutine_call(node)
    assert are_identical_nodes(expected, node)


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                 TERMS AND EXPRESSIONS                                      ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
@parametrize(term_test_configs.TESTDATA__PARSE_TERM)
def test_parse_term(tokens, expected):
    node = Parser(tokens)._parse_term()
    assert are_identical_nodes(expected, node)


@parametrize(term_test_configs.TESTDATA__PARSE_EXPRESSION)
def test_parse_expression(tokens, expected):
    node = Parser(tokens)._parse_expression()
    assert are_identical_nodes(expected, node)


@parametrize(term_test_configs.TESTDATA__PARSE_EXPRESSION_LIST)
def test_parse_expression_list(tokens, expected):
    node = Parser(tokens)._parse_expression_list()
    assert are_identical_nodes(expected, node)


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                                  UTILS                                     ║
# ╚════════════════════════════════════════════════════════════════════════════╝
def are_identical_nodes(n1, n2) -> bool:
    """Returns True if two XML tree nodes are identical, False otherwise.

    Sadly, there is no short and sensible way to compare subtrees (the __eq__ operator in
    fact compares identity!), so we have to turn the nodes to strings, and flatten them.
    NOTE: spaces are deleted, so strings like "hello world" and " h e ll o    w orld " are
          recognized as identical. Keep this in mind.
    """
    s1 = etree.tostring(n1).decode('utf-8').replace('\n', '').replace(' ', '').replace('\t', '')
    s2 = etree.tostring(n2).decode('utf-8').replace('\n', '').replace(' ', '').replace('\t', '')
    return s1 == s2


@parametrize(term_test_configs.TESTDATA__ADD_TOKENS_AND_ADVANCE)
def test_add_tokens_and_advance(tokens, expected):
    root, n = etree.Element('__test__'), len(tokens)
    Parser(tokens)._add_tokens_and_advance(root, n)
    assert expected == etree.tostring(root).decode('utf-8')


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                        TESTS WITH PROVIDED TOOLS                           ║
# ╚════════════════════════════════════════════════════════════════════════════╝
def test_using_tools():
    for jack_fname in glob.glob('p10/*/*.jack'):
        out_fname = jack_fname.replace('.jack', '__my.xml')
        cmp_fname = jack_fname.replace('.jack', '.xml')
        with open(jack_fname) as jack_file:
            tokens = tokenize(jack_file.read())
            parser = Parser(tokens)
            Parser.to_xml(parser.parse_class(), out_fname)
        assert are_identical_files(out_fname, cmp_fname)
