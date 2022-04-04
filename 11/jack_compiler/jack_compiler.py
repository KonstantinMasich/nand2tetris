

class Compiler:
    T_BINARY_OP = {'+': 'add', '-': 'sub', '*': 'call Math.multiply 2', '/': 'call Math.divide 2',
                   '&': 'and', '|': 'or', '>': 'gt', '<': 'lt', '=': 'eq'}
    T_UNARY_OP  = {'-': 'neg', '~': 'not'}

    def __init__(self, tokens: list, fname: str = ''):
        self.tokens    = tokens                      # List of pairs [['class': 'keyword'], [_, _],...]
        self.fname     = fname                       # Output filename
        self.res       = []                          # End result - a list with VM instructions
        self.n         = len(tokens)                 # Total amount of tokens
        self.i         = 0                           # Current token index
        self.labels    = {'if': -1, 'while': -1}     # Labels counter, for labels like IF-ELSE0, etc.
        self.classname = ''                          # Class name
        self.symbols   = {'class': {}}               # Symbol table
        self.scope     = 'class'                     # Current working scope; mainly for tests
        # Statement compilation methods:
        self.__COMPILE_STATEMENT_METHODS = {
            'let'   : self.compile_let_statement   ,
            'do'    : self.compile_do_statement    ,
            'while' : self.compile_while_statement ,
            'if'    : self.compile_if_statement    ,
            'return': self.compile_return_statement
        }
        # Helpers:
        self.in_constructor = False

    def compile(self):
        """Compiles the entire file and outputs VM commands into the specified file."""
        self.compile_class()
        if self.fname:
            with open(self.fname, 'w') as out_file:
                out_file.write('\n'.join(self.res))
        return self.res

    # ----------------------------------------------------------------------------------------------
    #                     Properties (shorthand, for convenience)
    # current token's (tokens[i]) value and type; and the next token's value, i.e. tokens[i+1]
    @property
    def curr(self):
        return self.tokens[self.i][0] if self.i <= self.n - 1 else None

    @property
    def curr_type(self):
        return self.tokens[self.i][1] if self.i <= self.n - 1 else None

    @property
    def next(self):
        return self.tokens[self.i + 1][0] if self.i < self.n - 1 else ''
    # ----------------------------------------------------------------------------------------------

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                 CLASS AND CLASS VARS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def compile_class(self):
        #    V                                v
        #  class Main { ...      ::      }   ___
        self.classname = self.next
        self.i += 3
        self.compile_class_var_dec()
        while self.curr in ('constructor', 'function', 'method'):
            self.compile_subroutine_dec()
        if self.curr == '}': self.i += 1

    def compile_class_var_dec(self):
        #     V                                      v
        #  static|field field_name      ::      ;   ___
        classvar_counters = {'static': 0, 'field': 0}
        while self.curr in ('static', 'field'):
            attr_kind, attr_type = self.curr, self.next
            self.i += 2
            while self.curr != ';':
                self.symbols['class'][self.curr] = {
                    'type': attr_type, 'kind': attr_kind, 'i': classvar_counters[attr_kind]
                }
                self.i += 2 if self.next == ',' else 1
                classvar_counters[attr_kind] += 1
            self.i += 1

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                   VARIABLES, PARAMETERS, FUNCTIONS DECLARATIONS AND CALLS                  ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def compile_subroutine_call(self):
        #      V                                         v
        #  subName|className.varName (      ::      )   ___
        n_args, increment = 0, 0
        # 1. Find out the exact structure of the call. Note that the short form like "do foo().."
        #    requires pushing "pointer 0" (this) before proceeding!
        if self.next == '.':
            obj_name, subroutine_name, increment = self.curr, self.tokens[self.i + 2][0], 3
        else:
            obj_name, subroutine_name, increment = self.classname, self.curr, 1
            self.res.append('push pointer 0')
            n_args += 1
        full_subroutine_name = f'{obj_name}.{subroutine_name}'
        # 2. If called subroutine is instance-related, like "car.drive()":
        if (obj_data := self.__var_lookup(obj_name)) is not None:
            full_subroutine_name = f'{obj_data["type"]}.{subroutine_name}'
            kind = 'this' if obj_data['kind'] == 'field' else obj_data['kind']
            self.res.append(f'push {kind} {obj_data["i"]}')
            n_args += 1
        self.i += increment
        n_args += self.compile_expression_list()             # Ends after the last ")"
        self.res.append(f'call {full_subroutine_name} {n_args}')

    def compile_subroutine_dec(self):
        #      V                                                   v
        #  function|method|constructor subName {      ::      }   ___
        subroutine_kind, subroutine_type, subroutine_name = (self.tokens[self.i + n][0] for n in range(3))
        self.labels = {'if': -1, 'while': -1}
        self.symbols[subroutine_name], self.scope = {'args': {}, 'locals': {}}, subroutine_name
        self.i += 3                                  # Now at "(" of arguments declarations
        self.compile_parameters_list(subroutine_kind)
        self.compile_subroutine_body(subroutine_kind, subroutine_name)
        self.scope = 'class'                         # In the end - after last "}" of subroutine

    def compile_subroutine_body(self, subroutine_kind: str, subroutine_name: str):
        #   V                                                    v
        #   { local variables... statements...      ::      }   ___
        self.i += 1
        lcl_count = 0
        # 1. Add local variables to symbol table and write function VM command:
        while self.curr == 'var':
            var_type = self.next
            self.i  += 2
            while self.curr != ';':
                if self.curr != ',':
                    self.symbols[self.scope]['locals'][self.curr] = {
                        'type': var_type, 'kind': 'local', 'i': lcl_count
                    }
                    lcl_count += 1
                self.i += 1
            self.i += 1                              # After the last ";" of local variables
        self.res.append(f'function {self.classname}.{subroutine_name} {lcl_count}')
        # 2. Add special treatment for constructors and methods:
        if subroutine_kind == 'constructor':
            n_fields = len([x for x in self.symbols['class'].values() if x['kind'] == 'field'])
            self.res.extend([f'push constant {n_fields}', 'call Memory.alloc 1', 'pop pointer 0'])
            self.in_constructor = True
        elif subroutine_kind == 'method':
            self.res.extend(['push argument 0', 'pop pointer 0'])
        # 3. Compile statements:
        self.compile_statements()
        self.i += 1                                  # Now after the last "}"

    def compile_parameters_list(self, subroutine_kind: str):
        #  V                                                v
        #  (  int a, Float b, Double c, ... , String s )   ___
        self.i += 1
        arg_count = 0 if subroutine_kind != 'method' else 1
        while self.curr != ')':
            self.symbols[self.scope]['args'][self.next] = {
                'type': self.curr, 'kind': 'argument', 'i': arg_count
            }
            arg_count += 1
            self.i    += 2
            if self.curr == ',':
                self.i += 1
        self.i += 1

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                     STATEMENTS                                             ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def compile_statements(self):
        #   V                            v
        #  let varName      ::      ;   ___
        while self.curr in self.__COMPILE_STATEMENT_METHODS:
            self.__COMPILE_STATEMENT_METHODS[self.curr]()

    def compile_let_statement(self):
        #   V                            v
        #  let varName      ::      ;   ___
        self.i += 1                                # At varName
        vardata = self.__var_lookup(self.curr)
        kind    = 'this' if vardata['kind'] == 'field' else vardata['kind']
        if self.next != '[':
            self.i += 2                            # Now at expression after "="
            self.compile_expression()              # Now at ";" of the expression
            self.i += 1                            # Now after ";" of the expression
            self.res.append(f'pop {kind} {vardata["i"]}')
        else:
            self.i += 2                            # Now at variable name
            self.compile_expression()
            self.res.extend([f'push {kind} {vardata["i"]}', 'add'])
            self.i += 2                            # Now after "=", at expression start
            self.compile_expression()
            self.i += 1
            self.res.extend(['pop temp 0', 'pop pointer 1', 'push temp 0', 'pop that 0'])

    def compile_if_statement(self):
        #   V                                  v
        #  if  (condition...      ::      }   ___
        self.labels['if'] += 1
        n_label = self.labels['if']
        self.i += 2                          # Now after "(" of condition
        if self.curr != ')':
            self.compile_expression()
            self.res.extend([f'if-goto IF_TRUE{n_label}', f'goto IF_FALSE{n_label}', f'label IF_TRUE{n_label}'])
        self.i += 2                         # Now after "{" of if-clause
        self.compile_statements()
        self.i += 1                         # Now after "}" of if-clause
        if self.curr == 'else':
            self.res.append(f'goto IF_END{n_label}')   # This is placed only if there is an "else" clause
        self.res.append(f'label IF_FALSE{n_label}')    # This is placed IN ANY CASE, regardless of "else" clause
        if self.curr == 'else':
            self.i += 2                     # Now after "}" of else clause
            self.compile_statements()
            self.res.append(f'label IF_END{n_label}')
            self.i += 1

    def compile_while_statement(self):
        self.labels['while'] += 1
        n_label = self.labels['while']
        self.res.append(f'label WHILE_EXP{n_label}')
        self.i += 2                          # Now after "(" of condition clause
        self.compile_expression()
        self.res.extend(['not', f'if-goto WHILE_END{n_label}'])
        self.i += 2                          # Now after "{" of while body
        self.compile_statements()
        self.res.extend([f'goto WHILE_EXP{n_label}', f'label WHILE_END{n_label}'])
        self.i += 1

    def compile_do_statement(self):
        #   V                                       v
        #  do Foo.Bar(arg1, arg2      ::     ) ;   ___
        self.i += 1                       # do
        self.compile_subroutine_call()    # Bar.foo(params)
        self.res.append('pop temp 0')
        self.i += 1

    def compile_return_statement(self):
        #     V                         v
        #  return ...      ::      ;   ___
        self.i += 1
        if self.curr == ';':
            self.res.append('push constant 0')
        else:
            self.compile_expression()
        self.res.append('return')
        self.i += 1

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                TERMS AND EXPRESSIONS                                       ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def compile_expression(self):
        # STARTS AT : after the first '('
        # ENDS AT   : ?
        self.compile_term()
        while self.curr in Compiler.T_BINARY_OP:
            opname = Compiler.T_BINARY_OP[self.curr]
            self.i += 1
            self.compile_term()
            self.res.append(opname)

    def compile_expression_list(self):
        """Returns amount of parsed expressions. Useful for counting args."""
        #  V                                                  v
        #  ( expression 1, expression2, ...      ::      )   ___
        n_exprs = 0
        self.i += 1  # Now after the first "(" symbol
        while self.curr != ')':
            self.compile_expression()
            n_exprs += 1
            if self.curr == ',':
                self.i += 1
        self.i += 1
        return n_exprs

    def compile_term(self):
        # Integer constant:
        if self.curr_type == 'integerConstant':
            self.res.append(f'push constant {self.curr}')
            self.i += 1
        # String constant:
        elif self.curr_type == 'stringConstant':
            self.res.extend(Compiler.__prepare_string_constant(self.curr))
            self.i += 1
        # Boolean:
        elif self.curr in ('true', 'false'):
            self.res.extend(['push constant 0', 'not'] if self.curr == 'true' else ['push constant 0'])
            self.i += 1
        # Special: THIS
        elif self.curr == 'this':
            self.res.append('push pointer 0')
            self.i += 1
        # Special: null
        elif self.curr == 'null':
            self.res.append('push constant 0')
            self.i += 1
        elif self.curr_type == 'identifier':
            # varName [ expression ]
            if self.next == '[':
                vardata = self.__var_lookup(self.curr)
                self.i += 2
                self.compile_expression()  # expression
                self.i += 1
                self.res.extend([f'push {vardata["kind"]} {vardata["i"]}', 'add'])
                self.res.extend(['pop pointer 1', 'push that 0'])
            # Subroutine call like bark(params) or Dog.bark(params)
            elif self.next in ('(', '.'):
                self.compile_subroutine_call()
            # varName
            else:
                var_data  = self.__var_lookup(self.curr)
                kind, idx = var_data['kind'], var_data['i']
                self.i   += 1
                self.res.append(f'push {"this" if kind=="field" else kind} {idx}')
        # ( expression )
        elif self.curr == '(':
            self.i += 1
            self.compile_expression()
            self.i += 1
        # unaryOp term
        elif self.curr in Compiler.T_UNARY_OP:
            op = Compiler.T_UNARY_OP[self.curr]
            self.i += 1
            self.compile_term()
            self.res.append(op)

    # ╔════════════════════════════════════════════════════════════════════════════════════════════╗
    # ║                                         HELPERS                                            ║
    # ╚════════════════════════════════════════════════════════════════════════════════════════════╝
    def __var_lookup(self, varname: str):
        """Looks up a specified variable, and returns its data, or None in case of error."""
        try:
            subroutine_scope = self.symbols[self.scope]
            if varname in subroutine_scope.get('args', []):
                return subroutine_scope['args'][varname]
            elif varname in subroutine_scope.get('locals', []):
                return subroutine_scope['locals'][varname]
            else:
                return self.symbols['class'][varname]
        except KeyError:
            return

    @staticmethod
    def __prepare_string_constant(s: str) -> list:
        """Returns a list of commands for creating a String object."""
        res = [f'push constant {len(s)}', 'call String.new 1']
        for symbol in s:
            res.append(f'push constant {ord(symbol)}')
            res.append('call String.appendChar 2')
        return res
