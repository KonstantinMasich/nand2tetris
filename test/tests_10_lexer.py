import glob
import p10.code.lexer as lexer
from test_utils.commons import parametrize, are_identical_files
import test_utils.test_configs_10__lexer as test_configs


@parametrize(test_configs.TESTDATA__REMOVE_COMMENTS)
def test_remove_comments(code, expected):
    assert expected == lexer.remove_comments(code)


@parametrize(test_configs.TESTDATA__GET_TOKEN_TYPE)
def test_get_token_type(token, expected):
    assert expected == lexer.get_token_type(token)


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                        TESTS WITH PROVIDED TOOLS                           ║
# ╚════════════════════════════════════════════════════════════════════════════╝
def test_using_tools():
    for jack_fname in glob.glob('p10/*/*.jack'):
        out_fname = jack_fname.replace('.jack', 'T__my.xml')
        cmp_fname = jack_fname.replace('.jack', 'T.xml')
        with open(jack_fname) as jack_file:
            tokens = lexer.tokenize(jack_file.read())
            lexer.to_xml(out_fname, tokens)
            assert are_identical_files(out_fname, cmp_fname)
