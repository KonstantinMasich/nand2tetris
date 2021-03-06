# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
"""Stores settings, templates, and constants."""

# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                                     TEMPLATES: PUSH / POP                                        #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
TMPL_PUSHPOP = {
    'argument': {
        'push': """// push {segment} {index}
            @{index}
            D=A
            @{segment}
            A=M+D
            D=M 
            @SP
            M=M+1
            A=M-1
            M=D\n""",
        'pop': """// pop {segment} {index}
            @{index}
            D=A
            @{segment}
            D=M+D
            @13
            M=D
            @SP
            AM=M-1
            D=M
            @13
            A=M
            M=D\n"""
        },
    'constant': {
        'push': """// push constant {val}
            @{val}
            D=A
            @SP
            M=M+1
            A=M-1
            M=D\n""",
        'pop': """// pop constant {val}
            @SP
            M=M-1\n"""
    },
    'temp': {
        'push': """// push temp {index}
            @{addr_temp}
            D=M
            @SP
            M=M+1
            A=M-1
            M=D\n""",
        'pop': """// pop temp {index}
            @SP
            AM=M-1
            D=M
            @{addr_temp}
            M=D\n"""
    },
    'pointer': {
        'push': """// push pointer {index}
            @{addr_ptr}
            D=M
            @SP
            M=M+1
            A=M-1
            M=D\n""",
        'pop': """// pop pointer {index}
            @SP
            AM=M-1
            D=M
            @{addr_ptr}
            M=D\n"""
    },
    'static': {
        'push': """// push static {index}
            @{fname}.{index}
            D=M
            @SP
            M=M+1
            A=M-1
            M=D\n""",
        'pop': """// push static {index}
            @SP
            AM=M-1
            D=M
            @{fname}.{index}
            M=D\n"""
    }
}
# Push/pop commands for LCL, THIS and THAT use the same template as ARG, so just copy those:
TMPL_PUSHPOP['local'] = TMPL_PUSHPOP['this'] = TMPL_PUSHPOP['that'] = TMPL_PUSHPOP['argument']


# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                                    TEMPLATES: ARITHMETICS                                        #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
# Templates for arithmetic binary (+, -, &, !), unary (!, -) and comparison (==, >, <) operations.
# They are similar in nature, so all we really have to do is to place the necessary operation
# symbol into the template - and that's it!
TMPL_OP_UNARY = """// {opname}
            @SP
            A=M-1
            M={op}M\n"""
TMPL_OP_BINARY = """// {opname}
            @SP
            AM=M-1
            D=M
            A=A-1
            M=M{op}D\n"""
TMPL_OP_COMP = """// {opname}
            @SP
            AM=M-1
            D=M
            A=A-1
            D=M-D
            M=0
            @{label}
                    D;{op}
            @SP
            A=M-1
            M=-1 
        ({label})\n"""
ARITHMETIC_OPS = {
    'neg': {'op': '-',   'template':  TMPL_OP_UNARY},
    'not': {'op': '!',   'template':  TMPL_OP_UNARY},
    'add': {'op': '+',   'template': TMPL_OP_BINARY},
    'sub': {'op': '-',   'template': TMPL_OP_BINARY},
    'and': {'op': '&',   'template': TMPL_OP_BINARY},
    'or' : {'op': '|',   'template': TMPL_OP_BINARY},
    'eq' : {'op': 'JNE', 'template':   TMPL_OP_COMP},
    'lt' : {'op': 'JGE', 'template':   TMPL_OP_COMP},
    'gt' : {'op': 'JLE', 'template':   TMPL_OP_COMP},
}
# IMPORTANT: note that for relational operators their assembly actions (JNE, JLE, JGE) are
#            inverted, i.e. equality comparison "=" is implemented using JNE - jump
#            if NOT equal. That is done for optimisation - read the documentation (README.md)


# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                                           LABELS                                                 #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
LBL_IF_ELSE = '{fname}__{cmd}__{mark}'


# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                                            MISC                                                  #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
PUSH_POP_COMMANDS   = ('push', 'pop')
ARITHMETIC_COMMANDS = ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')
SEGMENTS            = {'argument': 'ARG', 'local': 'LCL', 'this': 'THIS', 'that': 'THAT', 'pointer': 'THIS'}
FILE_HEADER = """
// ========================================================== //
//                   FILE {fname}
// ========================================================== //

"""
FILE_FOOTER = """

    (INFINITE__END__LOOP)
        @INFINITE__END__LOOP
                0;JMP

// ========================================================== //
//                    END OF FILE {fname}
// ========================================================== //
"""
DBG_INSTRUCTION = '            @11111\n'
