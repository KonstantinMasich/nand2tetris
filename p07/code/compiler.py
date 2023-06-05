import glob
from .const import ARITHMETIC_INSTRUCTIONS, TMPL__POP, TMPL__PUSH, SEG_ALIAS, SEG_BASE

# ╔══════════════════════╗
# ║ Python version: 3.11 ║
# ╚══════════════════════╝


class VMCompiler:
    """Translates from intermediate VM language (kind of like a bytecode) to
    assembly language for Nand2Tetris."""

    def __init__(self):
        self.fname, self.service_mark = 'null', 0

    def compile(self, vm_fname_or_dir: str):
        """Translates the specified .vm file or entire directory to Hack
        assembly language.

        :param vm_fname_or_dir: a .vm file or a directory with at least one .vm file.
        """
        match vm_fname_or_dir.split('.'):
            case _, 'vm':
                vm_fname  = vm_fname_or_dir
                asm_fname = vm_fname_or_dir.replace('.vm', '.asm')
                self._compile_file(vm_fname, asm_fname)
            case _:
                for vm_fname in glob.glob(f'{vm_fname_or_dir}/*.vm'):
                    asm_fname = vm_fname.replace('.vm', '.asm')
                    self._compile_file(vm_fname, asm_fname)

    def _compile_file(self, vm_fname: str, asm_fname: str = None):
        """Translates the specified .vm file into assembly language and writes the
        resulting assembly code into .asm file.

        :param vm_fname: input file path (.vm)
        :param asm_fname: output file path (.asm)
        """
        self.fname = vm_fname.split('/')[-1].replace('.vm', '')
        self.service_mark = 0
        with open(vm_fname) as vm_file:
            asm_lines = (
                asm_instr for line in vm_file.readlines()
                if (asm_instr := self._translate(line))
            )
        with open(asm_fname, 'w') as asm_file:
            asm_file.writelines('\n'.join(asm_lines))

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
