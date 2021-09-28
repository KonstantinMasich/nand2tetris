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
#                              TEMPLATES: BRANCHING (LABEL & GOTO)                                 #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
TMPL_BRANCHING = {
    'label': """// label {label}
            ({file_func}${label})\n""",
    'goto': """// goto {label}
            @{file_func}${label}
                0;JMP\n""",
    'if-goto': """// if-goto {label}
            @SP
            AM=M-1
            D=M
            @{file_func}${label}
                D;JNE\n"""
}


# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                        TEMPLATES: FUNCTION FLOW (FUNCTION, CALL, RETURN)                         #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
TMPL_FUNCTION = {
    'function no args': """// function {file_func} {k}
        ({file_func})\n""",
    'function': """// function {file_func} {k}
        ({file_func})
            @SP
            A=M
{push_commands}
            @{k}
            D=A
            @SP
            M=M+D\n""",
    'call': """// call {called_file_func} {k}
            @{fname}_ret_addr__{cid}// 1. Push return address. Note that SP is not incremented
            D=A                     //    in this push. Instead it will get incremented after
            @SP                     //    this command - from step 2 onwards. 
            A=M	                    //    This is done for optimisation reasons (this way less
            M=D                     //    assembly instructions are used).
            @LCL                    // 2. Push LCL
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @ARG                    // 3. Push ARG
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THIS                   // 4. Push THIS
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @THAT                   // 5. Push THAT
            D=M                     //
            @SP                     //
            AM=M+1                  //
            M=D                     //
            @{k}                    // 6. Set ARG = SP - k - 5
            D=A                     //
            @5                      //
            D=A+D                   //
            @SP                     // 
            M=M+1                   // <-- Here's that delayed SP increment.
            D=M-D                   //
            @ARG                    //
            M=D                     //
            @SP                     // 7. Reposition LCL to SP
            D=M                     //
            @LCL                    //
            M=D                     //
            @{called_file_func}     // 8. Goto {called_file_func}
                0;JMP
            ({fname}_ret_addr__{cid})\n""",
    'return'  : """// return
            @LCL                    // 1. FRAME = LCL
            D=M                     //
            @13                     //
            M=D                     //
            @5                      // 2. RET = *(FRAME-5)
            D=D-A                   //
            A=D                     //
            D=M                     //
            @14                     //
            M=D                     //
            @SP                     // 3. *ARG = pop()
            AM=M-1                  //
            D=M                     //
            @ARG                    //
            A=M                     //
            M=D                     //
            @ARG                    // 4. SP = ARG + 1
            D=M+1                   //
            @SP                     //
            M=D                     //
            @13                     // 5. THAT = *(FRAME-1)
            AM=M-1                  //
            D=M                     //
            @THAT                   //
            M=D                     //
            @13                     // 6. THIS = *(FRAME-2)
            AM=M-1                  //
            D=M                     //
            @THIS                   //
            M=D                     //
            @13                     // 7. ARG = *(FRAME-3)
            AM=M-1                  //
            D=M                     //
            @ARG                    //
            M=D                     //
            @13                     // 8. LCL = *(FRAME-4)
            AM=M-1                  //
            D=M                     //
            @LCL                    //
            M=D                     //
            @14                     // 9. Goto RET
            A=M
                0;JMP\n"""
}
SERIES_PUSH_0 = '\t\t\tM=0\n\t\t\tA=A+1\n'  # "set M to 0, increment A" - for pushing zeroes

# ════════════════════════════════════════════════════════════════════════════════════════════════ #
#                                            MISC                                                  #
# ════════════════════════════════════════════════════════════════════════════════════════════════ #
LBL_IF_ELSE         = '{fname}__{cmd}__{mark}'
PUSH_POP_COMMANDS   = ('push', 'pop')
ARITHMETIC_COMMANDS = ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')
BRANCHING_COMMANDS  = ('label', 'goto', 'if-goto')
FUNC_COMMANDS       = ('function', 'call', 'return')
SEGMENTS            = {'argument': 'ARG', 'local': 'LCL',
                       'this': 'THIS', 'that': 'THAT', 'pointer': 'THIS'}

FILE_HEADER = """
// ========================================================== //
//                   FILE {fname}
// ========================================================== //
"""

FILE_FOOTER = """

// ========================================================== //
//                    END OF FILE {fname}
// ========================================================== //
"""

BOOTSTRAP_SYS_CALL = TMPL_FUNCTION['call'].format(called_file_func='Sys.init',
                                                  fname='Sys', k='0', cid='MAIN')
INFINITE_LOOP = """
    (Sys.init$WHILE)
        @Sys.init$WHILE
                0;JMP
"""
BOOTSTRAP_CODE = f"""
// ***************************
// *      BOOTSTRAP CODE     *
// ***************************
            @256
            D=A
            @SP
            M=D
            {BOOTSTRAP_SYS_CALL}
// ***************************
// *  END OF BOOTSTRAP CODE  *
// ***************************
"""
DBG_INSTRUCTION = '            @11111\n'
