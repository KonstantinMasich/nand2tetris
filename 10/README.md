## Implementation details

**Note**: this implementation of compiler is different from the one proposed in the course, to be shorter and faster to write. Though the main idea is the same, of course.

 * `lexer.py` - another name for a tokenizer. "Scanner", "lexer", "tokenizer", "lexical analyzer" mean basically the same thing.<br>
    Implementation is different from the book's proposed approach, as I used regular expressions and string manipulations to get the job done. 
 * `parser.py` - parser, which builds parse tree. In the book this is called "CompilationEngine", but since all it does is building a parse tree (i.e. it doesn't really do any compilation/optimizations) I called it "parser" instead of "compiler". It also follows the "lexer + parser" pair, like lex + yacc. Similarly, its methods are called `_parse_XXX` instead of `_compile_XXX`, but the essence is the same.<br>
    Parser is implemented in a similar way to what the book proposes.
 * `config.py` - holds various constants, regular expressions and templates for formatting.
 * `main.py` - main module.


Note that another name for <font color='brown'>lexer</font> is "lexical analyzer" and for <font color='brown'>parser</font> it's "syntax analyzer".

![lex_syn_scheme](../img/10_lex_syn_scheme.png "Analysis scheme")

### Building a parser
While building a lexer is very straightforward, building a parser is a more complex task.
* I recommend not to start from high-level methods like `compileClass` or `compileSubroutineDec`; instead, start from low-level methods. Start by building a term processing method (`compileTerm` in the book).
* Make it work with the simplest terms. Then, on a certain stage, you'll need to implement `compileExpression` method, which invokes `compileTerm` by the way. So, do it, and move on like this - all the way up to `compileClass`.
* Try to gradually test each new piece of functionality that you add to `compileTerm`. When I was building the parser, this is exactly what I did - wrote tests for various cases, where the expected output was taken from course XML files, and the actual output was produced by the functions that I implemented. A test is passed when expected and actual outputs do match. 

### Statements and expressions
Loosely speaking, expression is something that evaluates to a value, like `x+1`, `2+2` or `foo() + bar()`; statements are the smallest standalone element of an imperative programming language. A program is formed by a sequence of one or more statements. A statement will have internal components (e.g., expressions) - from Wiki.<br>
In Jack language statements are "let statement", "if statement", "while statement", "do statement" and "return statement".


### Example of a parse tree
```
<class>
  <keyword> class </keyword>
  <identifier> Main </identifier>
  <symbol> { </symbol>
  <classVarDec>
    <keyword> static </keyword>
    <keyword> boolean </keyword>
    <identifier> test </identifier>
    <symbol> ; </symbol>
  </classVarDec>
  <subroutineDec>
    <keyword> function </keyword>
    <keyword> void </keyword>
    <identifier> main </identifier>
    <symbol> ( </symbol>
    <parameterList>
</parameterList>
    <symbol> ) </symbol>
    <subroutineBody>
      <symbol> { </symbol>
      <varDec>
        <keyword> var </keyword>
        <identifier> SquareGame </identifier>
        <identifier> game </identifier>
        <symbol> ; </symbol>
      </varDec>
      <statements>
        <letStatement>
          <keyword> let </keyword>
          <identifier> game </identifier>
          <symbol> = </symbol>
          <expression>
            <term>
              <identifier> game </identifier>
            </term>
          </expression>
          <symbol> ; </symbol>
        </letStatement>
        <doStatement>
          <keyword> do </keyword>
          <identifier> game </identifier>
          <symbol> . </symbol>
          <identifier> run </identifier>
          <symbol> ( </symbol>
          <expressionList>
</expressionList>
          <symbol> ) </symbol>
          <symbol> ; </symbol>
        </doStatement>
        <doStatement>
          <keyword> do </keyword>
          <identifier> game </identifier>
          <symbol> . </symbol>
          <identifier> dispose </identifier>
          <symbol> ( </symbol>
          <expressionList>
</expressionList>
          <symbol> ) </symbol>
          <symbol> ; </symbol>
        </doStatement>
        <returnStatement>
          <keyword> return </keyword>
          <symbol> ; </symbol>
        </returnStatement>
      </statements>
      <symbol> } </symbol>
    </subroutineBody>
  </subroutineDec>
  <subroutineDec>
    <keyword> function </keyword>
    <keyword> void </keyword>
    <identifier> more </identifier>
    <symbol> ( </symbol>
    <parameterList>
</parameterList>
    <symbol> ) </symbol>
    <subroutineBody>
      <symbol> { </symbol>
      <varDec>
        <keyword> var </keyword>
        <keyword> boolean </keyword>
        <identifier> b </identifier>
        <symbol> ; </symbol>
      </varDec>
      <statements>
        <ifStatement>
          <keyword> if </keyword>
          <symbol> ( </symbol>
          <expression>
            <term>
              <identifier> b </identifier>
            </term>
          </expression>
          <symbol> ) </symbol>
          <symbol> { </symbol>
          <statements>
</statements>
          <symbol> } </symbol>
          <keyword> else </keyword>
          <symbol> { </symbol>
          <statements>
</statements>
          <symbol> } </symbol>
        </ifStatement>
        <returnStatement>
          <keyword> return </keyword>
          <symbol> ; </symbol>
        </returnStatement>
      </statements>
      <symbol> } </symbol>
    </subroutineBody>
  </subroutineDec>
  <symbol> } </symbol>
</class>
```
