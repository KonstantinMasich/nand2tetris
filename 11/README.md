## Implementation details

**Note**: this implementation of compiler is different from the one proposed in the course, to be shorter and faster to write. Though the main idea is the same, of course.

* `lexer.py` - another name for a tokenizer. "Scanner", "lexer", "tokenizer", "lexical analyzer" mean basically the same thing.<br>
  Implementation is different from the book's proposed approach, as I used regular expressions and string manipulations to get the job done.
* `compiler.py` - compiler, which gets tokens input (`lexer`'s outpu) and translates it to a series of VM commands.
  Parser is implemented in a similar way to what the book proposes.
* No `main.py` here: everything is done from the tests.

## lex
There's a set of rules for `lex` in **lex** directory.

## Compiler

The compiler is based on Parser from the previous chapter (10), but instead of building a parse tree, it outputs VM commands. 

1. Builds **symbol table** and keeps track of a current scope.
2. Performs translation form Jack to VM language and outputs the result into a file.

No linking (multiple files into one) is done.

### Scope and symbol table

Scope is only changed (from class to subroutine and back to class) during execution of `compile_subroutine_dec`. Symbol table is only relevant during subroutine declaration processing (i.e. not on subroutine call - only on declaration). 

Symbol table is updated "on the fly" in two places:
1. In `compile_class_var_dec`, when we add class attributes to the table
2. In `compile_subroutine_dec`'s sub-methods, when we add subroutine arguments local variables to the table.

Variables are looked up first at the subroutine-level symbol table, and then in class-level symbol table.

### Compiling constants
* **Integer** literals are processed with a simple `push constant`.
* **String** literals are processed by calling `String.new` with a length of a string, and then pushing each symbol's ASCII code and calling `String.appendChar`.
* **Boolean** literals are represented simply as -1 for True, and 0 for False.
* **Null** literals are represented simply as 0.
* **This** is processed as `push pointer 0` - the address of a current object.

### Compiling identifiers
* **Variables** are looked up in the current scope, and pushed onto the stack.
* **Subroutine calls**, like `Foo.bar()` or `bar()`, invoke `compile_subroutine_call` method.
* **Addressing array elements**, like `arr[i]`, is done by first compiling the expression inside `[...]` braces, which pushes onto the stack some value, and then adding this value to array pointer `arr`.
