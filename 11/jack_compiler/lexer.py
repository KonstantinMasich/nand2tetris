# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import re

# Regex:
RE_WRAPPED_TAGS   = r'<(\w*)\/>'
RE_COMMENT_BLOCK  = r'\/\*\*.+\*\/'
RE_COMMENT_INLINE = r'\/\/.+\n'
RE_STR_CONSTANT   = r'(\".+?\")'

# Jack language constants:
T_SYMBOLS = (
    '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-',
    '*', '/', '&', '|', '<', '>', '=', '~'
)
T_KEYWORDS = (
    'class', 'constructor', 'function', 'method', 'field',
    'static', 'var', 'int', 'char', 'boolean', 'void',
    'true',  'false', 'null', 'this', 'let', 'do', 'if',
    'else', 'while', 'return'
)
T_TYPES = {
    **{s: 'symbol' for s in T_SYMBOLS},
    **{kw: 'keyword' for kw in T_KEYWORDS},
}


def clean_code(code: str) -> str:
    """Returns cleaned-up code (as one big string) without comments and blank lines."""
    res = re.sub(RE_COMMENT_INLINE, '\n', code)
    res = res.replace('\n', '').replace('*/', '*/\n')
    return re.sub(RE_COMMENT_BLOCK, '', res).replace('\n', '').replace('\t', '')


def get_token_type(token: str):
    """Returns one of the 5 possible token types."""
    if (t_type := T_TYPES.get(token)) is not None:
        return t_type
    # 1. Is it a digit?
    try:
        int(token)
        return 'integerConstant'
    except ValueError:
        pass
    # 2. Is it a string constant?
    if token.startswith('"') and token.endswith('"'):
        return 'stringConstant'
    # 3. Nothing of the above? Then it must be an identifier:
    return 'identifier'


def tokenize(code: str) -> list:
    """Returns a list of "token, type", pairs like
    [['class', 'keyword'], ['Main', 'identifier'], ['{': 'symbol'], ...]
    """
    code = clean_code(code)
    # 1. Build strings table and substitute strings by their keys from the table:
    str_table = {f'{t[0]}s': t[1] for t in list(enumerate(re.findall(RE_STR_CONSTANT, code)))}
    for i, s in str_table.items():
        code = code.replace(s, i)
    # 2. Break the code into a list of terminals, removing empty words (i.e. ''):
    for symbol in T_SYMBOLS:
        code = code.replace(symbol, f' {symbol} ')
    tokens = [x for x in code.split(' ') if x]
    # 3. Lastly, assign a type to each terminal and convert string constants back to
    #    their desired representation from their keys in strings table:
    tokens = [str_table.get(x, x) for x in tokens]
    return [[t.replace('"', ''), get_token_type(t)] for t in tokens]
