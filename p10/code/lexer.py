import re
import xml.etree.ElementTree as etree
from .const import RE_COMMENT_INLINE, RE_COMMENT_BLOCK, RE_STR_CONSTANT, \
    T_KEYWORDS, T_SYMBOLS, TokenType


# ╔══════════════════════╗
# ║ Python version: 3.11 ║
# ╚══════════════════════╝


def remove_comments(code: str) -> str:
    """Returns code without inline and multiline comments."""
    no_inline = re.sub(RE_COMMENT_INLINE, '', code)
    return re.sub(RE_COMMENT_BLOCK, '', no_inline)


def get_token_type(token: str) -> TokenType:
    """Returns type of the token; one of the 5 possible types."""
    if token in T_SYMBOLS:
        return TokenType.SYMBOL
    if token in T_KEYWORDS:
        return TokenType.KEYWORD
    if token.isdigit():
        return TokenType.INTEGER
    if token.startswith('"') and token.endswith('"'):
        return TokenType.STR_CONST
    return TokenType.IDENTIFIER


def tokenize(code: str) -> list:
    """Returns a list of <token, type>, pairs like
    [['class', 'keyword'], ['Main', 'identifier'], ['{': 'symbol'], ...]
    """
    tokens = []
    code   = remove_comments(code)
    # Substitute (temporarily!) string constans by special identifiers, to avoid
    # dealing with strings with keywords in them, like "while 3+3 class 3;;+2":
    string_table = build_string_table(code, RE_STR_CONSTANT)
    for idx, string in string_table.items():
        code = code.replace(string, idx)
    for line in code.split('\n'):
        if clean_line := line.strip():
            # The easiest way to deal with symbols is to just wrap them in
            # whitespaces, and then split the entire line by whitespace:
            for symbol in T_SYMBOLS:
                clean_line = clean_line.replace(symbol, f' {symbol} ')
            lexemes = [string_table.get(s, s) for s in clean_line.split()]
            # Note that double quotes are removed; this is because the course's
            # tokens dont't include them. See p10/ArrayTest/MainT.xml, for example.
            tokens.extend([(lexeme.replace('"', ''), get_token_type(lexeme))
                           for lexeme in lexemes])
    return tokens


def build_string_table(code: str, regex: str) -> dict:
    """Returns a dict like {'0s': Hello world, '1s': Text 1+2;int while, ... }
    which is built by searching for the matching strings (via regex).
    """
    return {
        f'{idx}s': string
        for idx, string in enumerate(re.findall(regex, code))
    }


def to_xml(fname: str, tokens: list):
    """Outputs the specified tokens list into an .xml file, for testing purposes."""
    root = etree.Element("tokens")
    for token in tokens:
        t_name, t_type = token
        etree.SubElement(root, t_type.value).text = f' {t_name} '
    tree = etree.ElementTree(root)
    etree.indent(tree, level=0)
    tree.write(fname)
