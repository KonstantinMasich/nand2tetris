# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import lexer
from parser import Parser

# FNAME = '../test/jack_src_code/class_valid.jack'
FNAME = '../test/jack_src_code/simple.jack'
# FNAME = '../test/provided_files/Main.jack'

with open(FNAME, 'r') as f:
    code   = ''.join(f.readlines())
    tokens = lexer.tokenize(code)
    print(tokens)
    lexer.to_xml('filename.xml', tokens)
    # Parse:
    p = Parser(tokens, 'check.xml')
    p.parse()
