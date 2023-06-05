"""VM-related constants: codes, templates, etc."""

SEG_BASE = {'pointer': 3, 'temp': 5}

# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       ARITHMETICS                                          ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
TMPL__OP_UNARY = """
        @SP
        A=M-1
        M={op}M
"""

TMPL__OP_BINARY = """
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M{op}D
"""

TMPL__OP_COMP = """
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        M=0
        @{fname}__{instr}__{mark}
            D;{op}
        @SP
        A=M-1
        M=-1
    ({fname}__{instr}__{mark})
"""

ARITHMETIC_INSTRUCTIONS = {
    'neg': ('-',   TMPL__OP_UNARY),
    'not': ('!',   TMPL__OP_UNARY),
    'add': ('+',   TMPL__OP_BINARY),
    'sub': ('-',   TMPL__OP_BINARY),
    'and': ('&',   TMPL__OP_BINARY),
    'or' : ('|',   TMPL__OP_BINARY),
    'eq' : ('JNE', TMPL__OP_COMP),
    'lt' : ('JGE', TMPL__OP_COMP),
    'gt' : ('JLE', TMPL__OP_COMP),
}

# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                     MEMORY ACCESS                                          ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
SEG_ALIAS = {'argument': 'ARG', 'local': 'LCL', 'this': 'THIS', 'that': 'THAT'}

TMPL__PUSH = {
    'constant': """
        @{idx}
        D=A
        @SP
        M=M+1
        A=M-1
        M=D
        """,
    'local': """
        @{idx}
        D=A
        @{segment_alias}
        A=M+D
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        """,
    'pointer': """
        @{base_and_offset}
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        """,
    'static': """
        @{fname}.{idx}
        D=M
        @SP
        M=M+1
        A=M-1
        M=D
        """,
}

TMPL__POP = {
    'local': """
        @{idx}
        D=A
        @{segment_alias}
        D=D+M
        @R13
        M=D
        @SP
        AM=M-1
        D=M
        @R13
        A=M
        M=D
        """,
    'pointer': """
        @SP
        AM=M-1
        D=M
        @{base_and_offset}
        M=D
        """,
    'static': """
        @SP
        AM=M-1
        D=M
        @{fname}.{idx}
        M=D
        """,
}

# Push and pop templates for local, argument, this and that are the same:
TMPL__PUSH['argument'] = TMPL__PUSH['this'] = TMPL__PUSH['that'] = TMPL__PUSH['local']
TMPL__POP['argument']  = TMPL__POP['this']  = TMPL__POP['that']  = TMPL__POP['local']

# Push and pop templates for temp and pointer are the same:
TMPL__PUSH['temp'] = TMPL__PUSH['pointer']
TMPL__POP['temp']  = TMPL__POP['pointer']
