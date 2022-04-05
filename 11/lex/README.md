## lex

This directory includes a rule file `rules.l` for `lex` utility, which generates a parser, written in **C** language. Very convenient!

Building a lexer with `lex` is done like this:
1. `lex rules.l` - this will output a file `lex.yy.c` which is used to build a lexer.
2. `gcc lex.yy.c -o lexer` - this will create executable file `lexer` which gets a file name (without extension; extension is appended as `.jack`) as input, tokenizes it, and outputs `xml` file.

Lexer usage: `./lexer <file_name_without_extension>`, for example `./lexer Main` or `./lexer Student`.
