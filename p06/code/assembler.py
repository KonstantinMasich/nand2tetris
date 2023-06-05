import re
import typing
from .const import DEST, COMP, JUMP, C_INSTR, PREDEFINED_SYMBOLS

# ╔══════════════════════╗
# ║ Python version: 3.11 ║
# ╚══════════════════════╝


class Assembler:
    """Translates from assembly language of Nand2Tetris to Hack machine code."""

    def __init__(self):
        self.symbols = dict(PREDEFINED_SYMBOLS)  # Symbol table
        self.asm_instructions = []               # Clean assembly instructions

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                  TRANSLATION METHODS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def _build_symbol_table(self):
        """Passes over the code and builds symbol table.
        Namely, assigns a line muber to each tag ("pseudo-instruction", like (LOOP), etc.) and
        assigns a free memory location to each variable.
        """
        # 1. Process labels and what looks like a label. Our options are:
        #    A. If we encounter label definition (MY_LABEL), we assign a line number to it.
        #    B. If we encounter a "@" reference, we don't know yet what does it refer to.
        #       Indeed, "@hello" may refer to the label (HELLO) or to a variable @HELLO.
        #       So for now we simply assign a None value to it, and will return to it later.
        # NOTE: important - note that we do not increment line number counter for label
        #       pseudo-instructions! This is because they are not real instructions!
        line_num = 0
        for instr in self.asm_instructions:
            match tuple(instr):
                case '(', *rest, ')' if (label := ''.join(rest)):
                    self.symbols[label] = line_num
                case '@', *rest if not (name := ''.join(rest)).isdigit():  # Skip @19, @394, ...
                    self.symbols.setdefault(name)
                    line_num += 1
                case _:
                    line_num += 1
        # 2. Process variable names. Now we know that every key in self.symbols with None
        #    value must be a variable. Go over the variables and assign a memory register
        #    to them, starting with 16 (i.e. right after R15):
        none_symbols = {sym: val for sym, val in self.symbols.items() if val is None}
        var_symbols  = {sym: reg for reg, sym in enumerate(none_symbols, 16)}
        self.symbols.update(var_symbols)

    def _build_a_instr(self, cmd: str) -> str:
        """Returns an A-instruction for Hack platform as translated from the
        specified assembly command.

        :param cmd: assembly command, like 'A=D+1' or '@THIS' or '@MY_LABEL'
        :return: Hack language instruction, like 0000001110100011
        """
        return self.to_16bit_binary(self.symbols.get(cmd[1:], cmd[1:]))

    def _build_c_instr(self, cmd: str) -> str:
        """Returns a C-instruction for Hack platform as translated from the
        specified assembly command.

        :param cmd: assembly command, like 'A=D+1' or '@THIS' or '@MY_LABEL'
        :return: Hack language instruction, like 0000001110100011
        :raises ValueError: in case of undefined command.
        """
        match re.split('[;=]', cmd):
            case dest, comp, jump:
                pass
            case dest, comp if comp in COMP:
                jump = ''
            case comp, jump if jump in JUMP:
                dest = ''
            case _:
                raise ValueError(f'Undefined assembly command {cmd}!')
        a = '1' if 'M' in comp else '0'
        dest, comp, jump = DEST[dest], COMP[comp], JUMP[jump]
        return C_INSTR.format(a=a, dest=dest, comp=comp, jump=jump)

    def compile_file(self, asm_fname: str, hack_fname: str = None) -> typing.Generator | None:
        """Translates the specified .asm file into Hack machine language, and either writes
        the resulting code into .hack file (if one is provided), or returns a generator
        expression with Hack machine code instructions.

        :param asm_fname: input file path (.asm)
        :param hack_fname: output file path (.hack). If not provided, then genexpr is returned
        :return: genexpr with Hack commands if asm_fname is not provided, otherwise None
        """
        self.symbols, self.asm_instructions = dict(PREDEFINED_SYMBOLS), []
        with open(asm_fname) as asm_file:
            # 1. Clean instructions (delete comments, whitespaces, etc):
            self.asm_instructions = [
                instr for line in asm_file.readlines()
                if (instr := self._get_clean_instruction(line))
            ]
            # 2. Build symbol table:
            self._build_symbol_table()
            # 3. Pseudo-instructions (labels) were processed during construction
            #    of the symbol table. Delete pseudo-instructions from clean code:
            self.asm_instructions = [instr for instr in self.asm_instructions
                                     if not instr.startswith('(')]
            # 4. Compile to Hack and write to file or return genexpr with Hack lines:
            hack_lines = (
                self._build_a_instr(line) if line.startswith('@') else self._build_c_instr(line)
                for line in self.asm_instructions
            )
            if hack_fname:
                with open(hack_fname, 'w') as asm_file:
                    asm_file.writelines('\n'.join(hack_lines))
            else:
                return hack_lines

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                          UTILS                                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    @staticmethod
    def to_16bit_binary(num: str) -> str:
        """Returns the given number in 16-bit binary string
        representation, like 0110110001100011."""
        if len(result := '{:016b}'.format(int(num))) == 16:
            return result
        raise ValueError(f'Overflow detected: {num} is too large to cast to 16-bit binary!')

    @staticmethod
    def _get_clean_instruction(instr: str) -> str:
        """Returns a clean assembly instruction, or empty string if input was
        a blank or comment line.

        :param instr: full instruction string, like M=M+1  // Some comment line.
        :return: clean instruction string, like M=M+1
        """
        return instr.replace(' ', '').replace('\n', '').split('//')[0]
