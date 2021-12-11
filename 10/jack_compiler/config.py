
# Regex:
RE_WRAPPED_TAGS   = r'<(\w*)\/>'
RE_COMMENT_BLOCK  = r'(\/\*(.|\n)+\*\/)'
RE_COMMENT_INLINE = r'\/\/.+\n'
RE_STR_CONSTANT   = r'(\".+?\")'

# Jack language constants:
T_SYMBOLS = (
    '{', '}', '(', ')', '[', ']', '.', ',', ';','+', '-',
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
T_OP           = ('+', '-', '*', '/', '&', '|', '<', '>', '=')
T_UNARY_OP     = ('-', '~')
T_KW_CONSTANTS = ('true', 'false', 'null', 'this')
