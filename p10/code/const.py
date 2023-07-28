import enum

# Regex:
RE_COMMENT_BLOCK  = r'\/\*\*(\n|.)*?\*\/'
RE_COMMENT_INLINE = r'\/\/.+'
RE_STR_CONSTANT   = r'(\".+?\")'

# Jack language constants:
T_SYMBOLS = {
    '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-',
    '*', '/', '&', '|', '<', '>', '=', '~'
}
T_KEYWORDS = {
    'class', 'constructor', 'function', 'method', 'field',
    'static', 'var', 'int', 'char', 'boolean', 'void',
    'true',  'false', 'null', 'this', 'let', 'do', 'if',
    'else', 'while', 'return'
}
T_OP       = {'+', '-', '*', '/', '&', '|', '<', '>', '='}
T_UNARY_OP = {'-', '~'}


# Token types:
class TokenType(enum.Enum):
    SYMBOL     = 'symbol'
    KEYWORD    = 'keyword'
    INTEGER    = 'integerConstant'
    STR_CONST  = 'stringConstant'
    IDENTIFIER = 'identifier'
