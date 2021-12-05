import lexer
from parser import *

with open('../test/jack_src_code/class_valid.jack', 'r') as f:
    code   = ''.join(f.readlines())
    tokens = lexer.tokenize(code)
    print(tokens)
    lexer.to_xml('filename.xml', tokens)
    parse(tokens)

