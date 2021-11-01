# coding: utf-8

import sys

# ╔═════════════════════╗
# ║ Python version: 3.9 ║
# ╚═════════════════════╝


class Compiler:
    """
    Hack compiler: translates .asm files to .hack files. Does all the work in 2 passes:
        1st pass: cleaning instructions and building symbol table.
        2nd pass: translating instructions to Hack machine code.
    """

    # ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                       TEMPLATES AND CODES                                       ║
    # ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
    COMP = {
        '0'  : '101010', '1'  : '111111', '-1' : '111010', 'D'  : '001100',
        'A'  : '110000', 'M'  : '110000', '!D' : '001101', '!A' : '110001',
        '!M' : '110001', '-D' : '001111', '-A' : '110011', '-M' : '110011',
        'D+1': '011111', 'A+1': '110111', 'M+1': '110111', 'D-1': '001110',
        'A-1': '110010', 'M-1': '110010', 'D+A': '000010', 'D+M': '000010',
        'D-A': '010011', 'D-M': '010011', 'A-D': '000111', 'M-D': '000111',
        'D&A': '000000', 'D&M': '000000', 'D|A': '010101', 'D|M': '010101'
    }
    DEST = {
        '' : '000', 'M' : '001', 'D' : '010', 'DM' : '011', 'MD' : '011',
        'A': '100', 'AM': '101', 'AD': '110', 'ADM': '111'
    }
    JMP = {
        ''   : '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
        'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
    }
    C_INSTR = '111{a}{comp}{dest}{jmp}'

    
    # ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                       COMPILATION METHODS                                       ║
    # ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
    def __init__(self, asm_file: str, hack_file: str = None):
        self.asm_fname  = asm_file   # Asm filename
        self.hack_fname = hack_file  # Hack filename
        self.asm_lines  = []         # Parsed, clean asm lines, like AD=M+1 or 0;JMP
        self.hack_lines = []         # Translated hack lines, like 0000001011000011
        self.symbols    = {
            'SP': 0, 'LCL': 1, 'ARG':  2, 'THIS':  3, 'THAT':  4, 
            'R0': 0, 'R1' : 1, 'R2' :  2, 'R3'  :  3, 'R4'  :  4, 'R5' :  5, 'R6' :  6, 'R7' :  7,
            'R8': 8, 'R9' : 9, 'R10': 10, 'R11' : 11, 'R12' : 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SCREEN': 16384, 'KBD': 24576
        }

    def _get_instruction(self, line: str):
        """Returns a clean assembly instruction, or empty string if it was a blank or comment line."""
        return line.replace(' ', '').replace('\n', '').split('//')[0]

    def _build_symbol_table(self):
        labels = {}
        # 1. Build initial table, working only on clean instructions (i.e. not blank or comment lines):
        with open(self.asm_fname, 'r') as f:
            lineno = 0
            for line in f.readlines():
                if instr := self._get_instruction(line):
                    # Case A: pseudo-instruction, i.e. (LOOP), (START), etc. Add it to the labels:
                    if instr.startswith('('):
                        labels[instr[1:-1]] = lineno
                        continue
                    # Case B: @-instruction which is not numeric, like @var, @LOOP, etc. We don't know
                    #         what to do with it at this point, so we simply add it to the symbol table
                    #         with value None for now:
                    elif instr.startswith('@') and not (addr := instr[1:]).isdigit():
                        if addr not in self.symbols:
                            self.symbols[addr] = None
                    # Append the clean instruction to asm_lines and increment lineno. Notice that line
                    # number counter is incremented only for the clean instruction lines!
                    self.asm_lines.append(instr)
                    lineno += 1
        # 2. Add labels to symbols dict:
        self.symbols = {**self.symbols, **labels}
        # 3. Take care of variables: iterate over symbols that still have a None value, and simply give
        #    them value of 16, then 17, 18, 19, etc. in incrementing order. Note that python dictionary 
        #    keep elements order, which guarantees that keys are stored in the same order that variables
        #    were encountered in the .asm file:
        last_var_addr = 16
        for symbol, addr in self.symbols.items():
            if addr is None:
                self.symbols[symbol] = last_var_addr
                last_var_addr += 1

    def _translate(self):
        """Builds instructions in Hack machine code as translated from assembly lines."""
        for line in self.asm_lines:
            # Case 1. A-instruction:
            if line.startswith('@'):
                addr = self.symbols.get(line[1:], line[1:])
                self.hack_lines.append(Compiler.to_bin(addr))
            # Case 2. C-instruction:
            else:
                p_dest, p_rest = line.split('=')   if '=' in line   else ('', line.split('=')[0])
                p_comp, p_jmp  = p_rest.split(';') if ';' in p_rest else (p_rest, '')
                a_bit = '1' if 'M' in p_comp else '0'
                self.hack_lines.append(self.C_INSTR.format(
                    a=a_bit, dest=self.DEST[p_dest], comp=self.COMP[p_comp], jmp=self.JMP[p_jmp])
                )

    def compile(self):
        """Processes the specified .asm file, and writes the machine code into .hack file."""
        self._build_symbol_table()
        self._translate() 
        hack_f = f'{self.asm_fname[:-4]}.hack' if not self.hack_fname else self.hack_fname
        with open(hack_f, 'w') as f:
            for line in self.hack_lines:
                f.write(f'{line}\n')


    # ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                            HELPERS                                              ║
    # ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝
    @staticmethod
    def to_bin(num: str) -> int:
        return '{:016b}'.format(int(num))


if __name__ == '__main__':
    asm_fname, hack_fname = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None
    Compiler(asm_fname, hack_fname).compile()

