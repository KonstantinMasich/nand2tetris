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


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                       BRANCHING                                            ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
TMPL__BRANCHING = {
    'label': """
        ({fname_func}${label})
    """,
    'goto': """
            @{fname_func}${label}
                0;JMP
    """,
    'if-goto': """
            @SP
            AM=M-1
            D=M
            @{fname_func}${label}
                D;JNE
    """
}


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                     FUNCTION FLOW                                          ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
TMPL__FUNCTION_NO_LOCALS = """
    ({fname_func})
"""

TMPL__FUNCTION_WITH_LOCALS = """
    ({fname_func})
        @SP
        A=M
    {init_zero_commands}
        @{n}
        D=A
        @SP
        M=M+D
"""

TMPL__CALL = """
        @{fname_func}_ret_addr__{cid}
        D=A
        @SP
        A=M
        M=D
        @LCL
        D=M
        @SP
        AM=M+1
        M=D
        @ARG
        D=M
        @SP
        AM=M+1
        M=D
        @THIS
        D=M
        @SP
        AM=M+1
        M=D
        @THAT
        D=M
        @SP
        AM=M+1
        M=D
        @{n}
        D=A
        @5
        D=A+D
        @SP
        M=M+1
        D=M-D
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @{fname_func}
            0;JMP
        ({fname_func}_ret_addr__{cid})
"""

TMPL__RETURN = """
        @LCL
        D=M
        @13
        M=D
        @5
        D=D-A
        A=D
        D=M
        @14
        M=D
        @SP
        AM=M-1
        D=M
        @ARG
        A=M
        M=D
        @ARG
        D=M+1
        @SP
        M=D
        @13
        AM=M-1
        D=M
        @THAT
        M=D
        @13
        AM=M-1
        D=M
        @THIS
        M=D
        @13
        AM=M-1
        D=M
        @ARG
        M=D
        @13
        AM=M-1
        D=M
        @LCL
        M=D
        @14
        A=M
        0;JMP
"""


# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                         UTILS                                              ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
INIT_TO_ZERO = """
        M=0
        A=A+1
"""

BOOTSTRAP__SYS_INIT_CALL = TMPL__CALL.format(fname='Sys', fname_func='Sys.init',
                                             n='0', cid='MAIN')

BOOTSTRAP__CODE = f"""
// -----------------------------
// --     BOOTSTRAP CODE      --
// -----------------------------
        @256
        D=A
        @SP
        M=D
        {BOOTSTRAP__SYS_INIT_CALL}
// -----------------------------
// --  END OF BOOTSTRAP CODE  --
// -----------------------------
"""

INFINITE_LOOP = """
        (Sys.init$WHILE)
            @Sys.init$WHILE
                    0;JMP
"""
