# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
import lexer
import glob
from parser import Parser
import sys


def parse_dir(source_code_dir: str):
    """Parses each .jack file in a given directory, builds parse tree and writes it
    into .xml file.
    """
    print(f'{"="*100}\nWorking with directory {source_code_dir}...')
    for src_fname in glob.glob(f'{source_code_dir}/*.jack'):
        xml_fname = f'{src_fname[:-5]}__my.xml'
        with open(src_fname, 'r') as src_file:
            print(f'\tParsing file {src_fname.split("/")[-1]}...', end='')
            code   = ''.join(src_file.readlines())
            tokens = lexer.tokenize(code)
            parser = Parser(tokens, xml_fname)
            parser.parse()
            print('OK')
    print(f'Parsing complete.\n{"="*100}')


def main():
    if len(sys.argv) > 1:
        parse_dir(sys.argv[1])
    else:
        tmpl = '../test/provided_files/{dirname}'
        for dirname in ('Square', 'ArrayTest', 'ExpressionLessSquare'):
            parse_dir(tmpl.format(dirname=dirname))


if __name__ == '__main__':
    main()
