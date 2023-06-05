
class RAM:
    """Emulates RAM from Nand2Tetris course."""

    FALSE, TRUE = 0, -1
    RAM_SIZE    = 5000  # TODO: set the correct value!
    STACK_SIZE  = 3000  # TODO: set the correct value!
    OPERATORS = {
        'not': lambda a: ~a,
        'neg': lambda a: -a,
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'and': lambda a, b: RAM.TRUE if a and b else RAM.FALSE,
        'or' : lambda a, b: RAM.TRUE if a  or b else RAM.FALSE, 
        'eq' : lambda a, b: RAM.TRUE if a  == b else RAM.FALSE,
        'lt' : lambda a, b: RAM.TRUE if a  <  b else RAM.FALSE,
        'gt' : lambda a, b: RAM.TRUE if a  >  b else RAM.FALSE,
    }
    OPS__UNARY      = {'not', 'neg'}
    OPS__BINARY     = {'add', 'sub', 'and', 'or'}
    OPS__COMPARISON = {'eq' , 'lt' , 'gt'}

    def __init__(self):
        self.cells = dict.fromkeys(range(self.RAM_SIZE), 0)
        self.sp    = 256

    @property
    def sp(self):
        """Stack pointer SP; an alias for RAM[0]."""
        return self.cells[0]

    @sp.setter
    def sp(self, n: int):
        """Stack pointer SP; an alias for RAM[0]."""
        self.cells[0] = n

    def a_instr():
        1111000011101110101110000011100001010111000001111000000111
        pass

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                         PUSH / POP                                         ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def push(self, segment: str, idx: str):
        """Pushes n onto stack."""
        idx = int(idx)
        print(f'push {segment} {idx}')
        match segment:
            case 'argument':
                pass
            case 'constant':
                self.cells[self.sp] = idx
                self.sp += 1
            case 'temp':
                pass
            case 'pointer':
                pass
            case 'static':
                pass
            case _:
                raise ValueError(f'Invalid segment {segment}!')

    def pop(self, segment: str):
        """Pops stack[SP] into the specified segment."""
        print(f'pop {segment}')
        self.sp -= 1
        match segment:
            case 'argument':
                pass
            case 'constant':
                pass
            case 'temp':
                pass
            case 'pointer':
                pass
            case 'static':
                pass
            case _:
                raise ValueError(f'Invalid segment {segment}!')

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                        ARITHMETICS                                         ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def arithmetic(self, op: str):
        """Applies arithmetic command, like 'add', 'sub', 'neg', etc."""
        a, b = self.cells[self.sp - 2], self.cells[self.sp - 1]
        if op in {'neg', 'not'}:
            self.cells[self.sp - 1] = self.OPERATORS[op](a)
        else:
            self.cells[self.sp - 2] = self.OPERATORS[op](a, b)
            self.sp -= 1

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                          EXECUTE                                           ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def execute(self, instructions: set) -> dict:
        """Executes the given sequence of instructions, modifying memory accordingly, and
        returns the cells dict (as it is after instructions execution).

        :param instructions: iterable with VM language instructions
        :return: cells dict
        """
        for instr in instructions:
            match instr.split():
                case 'push', seg, idx:
                    self.push(seg, idx)
                case 'pop', seg:
                    self.pop(seg)
                case [op] if op in self.OPERATORS:
                    self.arithmetic(op)
                case _:
                    raise ValueError(f'Invalid instruction {instr}!')
        return self.cells

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                          UTILS                                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def get_nonzero(self) -> dict:
        """Returns all nonzero elements from the stack."""
        return {k: v for k, v in self.cells.items() if v != 0}


class CPU:
    def __init__(self):
        pass

    def execute(self, instr):
        match tuple(instr):
            case '@', *rest if (addr := ''.join(rest)):
                pass
            case dest, comp, jmp:
                pass


instructions = ('push constant 2', 'push constant 7', 'lt')
ram = RAM()
print({k: v for k, v in ram.execute(instructions).items() if v != 0})
