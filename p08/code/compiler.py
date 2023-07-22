import glob
from .const import *


# ╔══════════════════════╗
# ║ Python version: 3.11 ║
# ╚══════════════════════╝


class VMCompiler:
    """Translates from intermediate VM language (kind of like a bytecode) to
    assembly language for Nand2Tetris."""

    def __init__(self):
        self.fname        = 'Sys'
        self.fname_func   = 'Sys.init'
        self.service_mark = 0
        self.cid          = 1

    def compile(self, vm_dir: str):
        """Translates the VM program - which is a directory with one or
        more .vm files - to Hack assembly language.

        :param vm_dir: a directory with .vm files
        """
        asm_code  = ''
        asm_fname = f'{vm_dir}/{vm_dir.split("/")[-1]}.asm'
        vm_files  = glob.glob(f'{vm_dir}/*.vm')
        # 1. Compile all the files in VM directory:
        for vm_fname in vm_files:
            asm_code += self._compile_file(vm_fname)
        # 2. Add bootstrap code, if Sys.vm exists, or an infinite loop in the end:
        if f'{vm_dir}/Sys.vm' in vm_files:
            asm_code = BOOTSTRAP__CODE + asm_code
        else:
            asm_code += INFINITE_LOOP
        # 3. Write the result into a single .asm file:
        with open(asm_fname, 'w') as asm_file:
            asm_file.writelines(asm_code)

    def _compile_file(self, vm_fname: str) -> str:
        """Translates the specified .vm file into assembly language and returns the
        resulting assembly in the form of a string.

        :param vm_fname: input file path (.vm)
        :return: string with assembly instructions.
        """
        self.fname = vm_fname.split('/')[-1].replace('.vm', '')
        self.service_mark = 0
        with open(vm_fname) as vm_file:
            asm_lines = (
                asm_instr for line in vm_file.readlines()
                if (asm_instr := self._translate(line))
            )
        return ''.join(asm_lines)

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                    TRANSLATION METHODS                                     ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _translate(self, instr: str) -> str:
        """Translates a given VM language instruction into a string with assembly instructions.
        Does nothing if a given string is not a valid instruction.
        """
        if clean_instr := instr.replace('\n', '').split('//')[0].strip():
            match clean_instr.split():
                case [cmd] if cmd in ARITHMETIC_INSTRUCTIONS:
                    return self._translate_arithmetic(cmd)
                case ['push' | 'pop' as cmd, segment, idx]:
                    return self._translate_pushpop(cmd, segment, idx)
                case ['label' | 'goto' | 'if-goto' as cmd, label]:
                    return self._translate_branching(cmd, label)
                case ['function' | 'call' as cmd, fname_func, args]:
                    return self._translate_func_flow(cmd, fname_func, args)
                case ['return']:
                    return self._translate_func_flow('return')
                case _:
                    raise ValueError(f'Invalid VM instruction "{instr}"!')

    def _translate_arithmetic(self, instr: str) -> str:
        """Returns VM instructions for arithmetic instruction: add, sub, gt, etc.

        :param instr: instruction in VM language.
        :return: instructions in assembly language (as one string).
        """
        op, template = ARITHMETIC_INSTRUCTIONS[instr]
        self.service_mark += 1
        return template.format(op=op, fname=self.fname, instr=instr, mark=self.service_mark)

    def _translate_pushpop(self, cmd: str, segment: str, idx: str) -> str:
        """Returns VM instructions for PUSH and POP commands.

        :param segment: segment, like 'argument', 'local', 'constant', etc.
        :param idx: segment index
        :return: instructions in assembly language
        """
        kwargs = {
            'fname'          : self.fname,
            'idx'            : idx,
            'segment_alias'  : SEG_ALIAS.get(segment, segment),
            'base_and_offset': int(idx) + SEG_BASE.get(segment, 0)
        }
        template = TMPL__PUSH[segment] if cmd == 'push' else TMPL__POP[segment]
        return template.format(**kwargs)

    def _translate_branching(self, cmd: str, label: str) -> str:
        """Returns VM instructions for branching commands - label, goto, and if-goto.

        :param cmd: command, one of {label, goto, if-goto}
        :param label: label name
        :return: instructions in assembly language
        """
        return TMPL__BRANCHING[cmd].format(fname_func=self.fname_func, label=label)

    def _translate_func_flow(self, cmd: str, fname_func: str = None, n: str = None) -> str:
        """Returns VM instructions for function flow commands - function, call, and return.

        :param cmd: command, one of {function, call, return}
        :param fname_func: filename + name of the defined or called function, like "Main.foo"
        :param n: either nLocals (for or function command) or nArgs (for call command)
        :return: instructions in assembly language
        """
        match cmd:
            case 'function':
                self.fname_func = fname_func
                if n == 0:
                    return TMPL__FUNCTION_NO_LOCALS.format(fname_func=fname_func)
                initialization = INIT_TO_ZERO * int(n)
                return TMPL__FUNCTION_WITH_LOCALS.format(fname_func=fname_func, n=n,
                                                         init_zero_commands=initialization)
            case 'call':
                self.cid += 1
                return TMPL__CALL.format(fname_func=fname_func, n=n, cid=self.cid)
            case 'return':
                return TMPL__RETURN
