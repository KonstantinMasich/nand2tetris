# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝

def parse(tokens: list):
    for token_tuple in tokens:
        token, t_type = token_tuple
        if token == 'class' and t_type == 'keyword':
            compile_class(tokens)


def compile_class(tokens):
    print('in parse class')


def compile_let(tokens):

    pass



