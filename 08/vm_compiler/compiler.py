# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝
from config import *


class Compiler:
    """Translates a single .vm file to assembly."""

    def __init__(self, vm_fpath: str, debug: bool = False):
        self.vm_fpath    : str  = vm_fpath                           # Path to target VM file
        self.service_mark: int  = 0                                  # Service labels iterator
        self.func        : str  = 'main'                             # Name of current subroutine
        self.fname       : str  = f'{vm_fpath.split("/")[-1][:-3]}'  # Mark for service labels
        self.debug       : bool = debug                              # Debug mode switch

    def translate_instruction(self, line: str) -> (str, None):
        """Returns a translated .vm line in the form of a string of assembly instructions,
        or None if a line is a valid instruction.
        """
        if clean_line := line.replace('\n', '').split('//')[0].split():
            cmd = clean_line[0]
            if cmd in PUSH_POP_COMMANDS:
                return self.translate_push_pop(cmd, clean_line[1], clean_line[2])
            elif cmd in ARITHMETIC_COMMANDS:
                return self.translate_arithmetic(cmd)
            elif cmd in BRANCHING_COMMANDS:
                return self.translate_branching(cmd, clean_line[1])
            return clean_line

    def translate_push_pop(self, cmd: str, segment: str, index: str) -> str:
        """Returns a translated .vm line for push or pop commands."""
        offset = int(index)
        kwargs = {'segment': SEGMENTS.get(segment, segment), 'index': index, 'fname': self.fname,
                  'val': index, 'addr_temp': 5 + offset, 'addr_ptr': 3 + offset}
        return TMPL_PUSHPOP[segment][cmd].format(**kwargs)

    def translate_arithmetic(self, cmd: str) -> str:
        """Returns a translated .vm line for arithmetic commands - add, sub, etc."""
        kwargs = {'opname': cmd, 'op': ARITHMETIC_OPS[cmd]['op']}
        if cmd in ['eq', 'gt', 'lt']:
            kwargs['label'] = LBL_IF_ELSE.format(fname=self.fname, cmd=cmd, mark=self.service_mark)
            self.service_mark += 1
        return ARITHMETIC_OPS[cmd]['template'].format(**kwargs)

    def translate_branching(self, cmd: str, label: str) -> str:
        """Returns a translated .vm line for branching commands - label, goto, and if-goto."""
        return TMPL_BRANCHING[cmd].format(fname=self.fname, func=self.func, label=label)

    def translate_func_flow(self, cmd: str, func: str, arg: str) -> str:
        """Returns a translated .vm line for function flow commands - function, call, return."""
        return self.fname

    def compile(self) -> str:
        """Returns a string of assembly commands, as translated from the specified file."""
        asm_code = FILE_HEADER.format(fname=self.fname)
        with open(self.vm_fpath, 'r') as vm_file:
            for r in vm_file.readlines():
                if assembly_instruction := self.translate_instruction(r):
                    asm_code += assembly_instruction
                    if self.debug:
                        asm_code += DBG_INSTRUCTION
        return asm_code + FILE_FOOTER.format(fname=self.fname)
