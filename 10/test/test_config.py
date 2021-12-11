
CONFIG__PARSE_TERM = {
    '14'  : '<class><term><integerConstant> 14 </integerConstant></term></class>',
    'true': '<class><term><keyword> true </keyword></term></class>',
    'null': '<class><term><keyword> null </keyword></term></class>',
    'this': '<class><term><keyword> this </keyword></term></class>',
    '"Hello world"': '<class><term><stringConstant> Hello world </stringConstant></term></class>',
    '(2 + 2)': """<class>
        <term>
            <symbol> ( </symbol>
            <expression>
                <term>
                    <integerConstant> 2 </integerConstant>
                </term>
                <symbol> + </symbol>
                <term>
                    <integerConstant> 2 </integerConstant>
                </term>
            </expression>
            <symbol> ) </symbol>
        </term>
        </class> """,
    'a[14 + 2]': """<class>
        <term>
            <identifier> a </identifier>
            <symbol> [ </symbol>
            <expression>
                <term>
                    <integerConstant> 14 </integerConstant>
                </term>
                <symbol> + </symbol>
                <term>
                    <integerConstant> 2 </integerConstant>
                </term>
            </expression>
            <symbol> ] </symbol>
        </term>
        </class>""",
    'a[i]': """<class> 
        <term>
            <identifier> a </identifier>
            <symbol> [ </symbol>
            <expression>
                <term>
                    <identifier> i </identifier>
                </term>
            </expression>
            <symbol> ] </symbol>
        </term>
        </class> """
}

CONFIG__PARSE_EXPRESSION = {
    'key = 0': """ <class>
        <expression>
            <term>
                <identifier> key </identifier>
            </term>
            <symbol> = </symbol>
            <term>
                <integerConstant> 0 </integerConstant>
            </term>
        </expression>
        </class> """,
    '~(key = 0)': """<class> 
        <expression>
            <term>
                <symbol> ~ </symbol>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <identifier> key </identifier>
                        </term>
                        <symbol> = </symbol>
                        <term>
                            <integerConstant> 0 </integerConstant>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
            </term>
        </expression>
        </class> """,
    '4': """<class>
        <expression>
            <term>
                <integerConstant> 4 </integerConstant>
            </term>
        </expression>
    </class> """,
    'y + size': """<class>
        <expression>
            <term>
                <identifier> y </identifier>
            </term>
            <symbol> + </symbol>
            <term>
                <identifier> size </identifier>
            </term>
        </expression>
    </class>"""
}

CONFIG__PARSE_SUBROUTINE_CALL = {
    'foo()': """<class>
        <identifier> foo </identifier>
        <symbol> ( </symbol>
        <expressionList></expressionList>
        <symbol> ) </symbol>
        </class>""",
    'Screen.setColor(true)': """<class>
        <identifier> Screen </identifier>
        <symbol> . </symbol>
        <identifier> setColor </identifier>
        <symbol> ( </symbol>
        <expressionList>
            <expression>
                <term>
                    <keyword> true </keyword>
                </term>
            </expression>
        </expressionList>
        <symbol> ) </symbol>
        </class>""",
    'Screen.drawRectangle((x + size) - 1, y, x + size, y + size)': """<class>
        <identifier> Screen </identifier>
        <symbol> . </symbol>
        <identifier> drawRectangle </identifier>
        <symbol> ( </symbol>
        <expressionList>
            <expression>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <identifier> x </identifier>
                        </term>
                        <symbol> + </symbol>
                        <term>
                            <identifier> size </identifier>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
                <symbol> - </symbol>
                <term>
                    <integerConstant> 1 </integerConstant>
                </term>
            </expression>
            <symbol> , </symbol>
            <expression>
                <term>
                    <identifier> y </identifier>
                </term>
            </expression>
            <symbol> , </symbol>
            <expression>
                <term>
                    <identifier> x </identifier>
                </term>
                <symbol> + </symbol>
                <term>
                    <identifier> size </identifier>
                </term>
            </expression>
            <symbol> , </symbol>
            <expression>
                <term>
                    <identifier> y </identifier>
                </term>
                <symbol> + </symbol>
                <term>
                    <identifier> size </identifier>
                </term>
            </expression>
        </expressionList>
        <symbol> ) </symbol> 
        </class>""",
    'game.run()': """<class>
        <identifier> game </identifier>
        <symbol> . </symbol>
        <identifier> run </identifier>
        <symbol> ( </symbol>
        <expressionList></expressionList>
        <symbol> ) </symbol>
        </class>""",
}

CONFIG__PARSE_LET_STATEMENT = {
    'let i = i * (-j);': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> i </identifier>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> i </identifier>
                </term>
                <symbol> * </symbol>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <symbol> - </symbol>
                            <term>
                                <identifier> j </identifier>
                            </term>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let j = j / (-2);': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> j </identifier>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> j </identifier>
                </term>
                <symbol> / </symbol>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <symbol> - </symbol>
                            <term>
                                <integerConstant> 2 </integerConstant>
                            </term>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let i = i | j;': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> i </identifier>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> i </identifier>
                </term>
                <symbol> | </symbol>
                <term>
                    <identifier> j </identifier>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let a = 18;': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> a </identifier>
            <symbol> = </symbol>
            <expression>
                <term>
                    <integerConstant> 18 </integerConstant>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let x = x + 2;': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> x </identifier>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> x </identifier>
                </term>
                <symbol> + </symbol>
                <term>
                    <integerConstant> 2 </integerConstant>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let a[1] = a[2];': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> a </identifier>
            <symbol> [ </symbol>
            <expression>
                <term>
                    <integerConstant> 1 </integerConstant>
                </term>
            </expression>
            <symbol> ] </symbol>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> a </identifier>
                    <symbol> [ </symbol>
                    <expression>
                        <term>
                            <integerConstant> 2 </integerConstant>
                        </term>
                    </expression>
                    <symbol> ] </symbol>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>""",
    'let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: ");': """<class>
        <letStatement>
            <keyword> let </keyword>
            <identifier> a </identifier>
            <symbol> [ </symbol>
            <expression>
                <term>
                    <identifier> i </identifier>
                </term>
            </expression>
            <symbol> ] </symbol>
            <symbol> = </symbol>
            <expression>
                <term>
                    <identifier> Keyboard </identifier>
                    <symbol> . </symbol>
                    <identifier> readInt </identifier>
                    <symbol> ( </symbol>
                    <expressionList>
                        <expression>
                            <term>
                                <stringConstant> ENTER THE NEXT NUMBER:  </stringConstant>
                            </term>
                        </expression>
                    </expressionList>
                    <symbol> ) </symbol>
                </term>
            </expression>
            <symbol> ; </symbol>
        </letStatement>
        </class>"""
}

CONFIG__PARSE_DO_STATEMENT = {
    'do Output.printInt(sum / length);': """<class>
        <doStatement>
            <keyword> do </keyword>
            <identifier> Output </identifier>
            <symbol> . </symbol>
            <identifier> printInt </identifier>
            <symbol> ( </symbol>
            <expressionList>
                <expression>
                    <term>
                        <identifier> sum </identifier>
                    </term>
                    <symbol> / </symbol>
                    <term>
                        <identifier> length </identifier>
                    </term>
                </expression>
            </expressionList>
            <symbol> ) </symbol>
            <symbol> ; </symbol>
        </doStatement>
        </class>""",
    'do foo();': """<class>
        <doStatement>
            <keyword> do </keyword>
            <identifier> foo </identifier>
            <symbol> ( </symbol>
            <expressionList></expressionList>
            <symbol> ) </symbol>
            <symbol> ; </symbol>
        </doStatement>
        </class>""",
}

CONFIG__PARSE_RETURN_STATEMENT = {
    'return;': """<class>
        <returnStatement>
        <keyword> return </keyword>
        <symbol> ; </symbol>
    </returnStatement>
    </class>""",
    'return x;': """<class>
        <returnStatement>
            <keyword> return </keyword>
            <expression>
                <term>
                    <identifier> x </identifier>
                </term>
            </expression>
            <symbol> ; </symbol>
        </returnStatement>
    </class>""",
}

CONFIG__PARSE_IF_STATEMENT = {
    'if (key) {let direction = direction;}': """<class>
        <ifStatement>
            <keyword> if </keyword>
            <symbol> ( </symbol>
            <expression>
                <term>
                    <identifier> key </identifier>
                </term>
            </expression>
            <symbol> ) </symbol>
            <symbol> { </symbol>
            <statements>
                <letStatement>
                    <keyword> let </keyword>
                    <identifier> direction </identifier>
                    <symbol> = </symbol>
                    <expression>
                        <term>
                            <identifier> direction </identifier>
                        </term>
                    </expression>
                    <symbol> ; </symbol>
                </letStatement>
            </statements>
            <symbol> } </symbol>
        </ifStatement>
    </class>""",
    'if (i) { let s = i; } else { let i = i | j; }': """<class>
        <ifStatement>
            <keyword> if </keyword>
            <symbol> ( </symbol>
            <expression>
                <term>
                    <identifier> i </identifier>
                </term>
            </expression>
            <symbol> ) </symbol>
            <symbol> { </symbol>
            <statements>
                <letStatement>
                    <keyword> let </keyword>
                    <identifier> s </identifier>
                    <symbol> = </symbol>
                    <expression>
                        <term>
                            <identifier> i </identifier>
                        </term>
                    </expression>
                    <symbol> ; </symbol>
                </letStatement>
            </statements>
            <symbol> } </symbol>
            <keyword> else </keyword>
            <symbol> { </symbol>
            <statements>
                <letStatement>
                    <keyword> let </keyword>
                    <identifier> i </identifier>
                    <symbol> = </symbol>
                    <expression>
                        <term>
                            <identifier> i </identifier>
                        </term>
                        <symbol> | </symbol>
                        <term>
                            <identifier> j </identifier>
                        </term>
                    </expression>
                    <symbol> ; </symbol>
                </letStatement>
            </statements>
            <symbol> } </symbol>
        </ifStatement>
    </class>""",
    'if (((y + size) < 254) & ((x + size) < 510)) { do erase(); }': """<class>
        <ifStatement>
            <keyword> if </keyword>
            <symbol> ( </symbol>
            <expression>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <symbol> ( </symbol>
                            <expression>
                                <term>
                                    <identifier> y </identifier>
                                </term>
                                <symbol> + </symbol>
                                <term>
                                    <identifier> size </identifier>
                                </term>
                            </expression>
                            <symbol> ) </symbol>
                        </term>
                        <symbol> &lt; </symbol>
                        <term>
                            <integerConstant> 254 </integerConstant>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
                <symbol> &amp; </symbol>
                <term>
                    <symbol> ( </symbol>
                    <expression>
                        <term>
                            <symbol> ( </symbol>
                            <expression>
                                <term>
                                    <identifier> x </identifier>
                                </term>
                                <symbol> + </symbol>
                                <term>
                                    <identifier> size </identifier>
                                </term>
                            </expression>
                            <symbol> ) </symbol>
                        </term>
                        <symbol> &lt; </symbol>
                        <term>
                            <integerConstant> 510 </integerConstant>
                        </term>
                    </expression>
                    <symbol> ) </symbol>
                </term>
            </expression>
            <symbol> ) </symbol>
            <symbol> { </symbol>
            <statements>
                <doStatement>
                    <keyword> do </keyword>
                    <identifier> erase </identifier>
                    <symbol> ( </symbol>
                    <expressionList></expressionList>
                    <symbol> ) </symbol>
                    <symbol> ; </symbol>
                </doStatement>
            </statements>
            <symbol> } </symbol>
    </ifStatement>
    </class>"""
}

CONFIG__PARSE_WHILE_STATEMENT = {
    'while (~(key = 0)) {}': """<class>
        <whileStatement>
            <keyword> while </keyword>
            <symbol> ( </symbol>
            <expression>
                <term>
                    <symbol> ~ </symbol>
                    <term>
                        <symbol> ( </symbol>
                        <expression>
                            <term>
                                <identifier> key </identifier>
                            </term>
                            <symbol> = </symbol>
                            <term>
                                <integerConstant> 0 </integerConstant>
                            </term>
                        </expression>
                        <symbol> ) </symbol>
                    </term>
                </term>
            </expression>
            <symbol> ) </symbol>
            <symbol> { </symbol>
            <statements></statements>
            <symbol> } </symbol>
        </whileStatement>
    </class>""",
}

CONFIG__PARSE_VAR_DEC = {
    'var int i, j;': """<class>
        <varDec>
            <keyword> var </keyword>
            <keyword> int </keyword>
            <identifier> i </identifier>
            <symbol> , </symbol>
            <identifier> j </identifier>
            <symbol> ; </symbol>
        </varDec>
    </class>""",
    'var boolean exit;': """<class>
        <varDec>
            <keyword> var </keyword>
            <keyword> boolean </keyword>
            <identifier> exit </identifier>
            <symbol> ; </symbol>
        </varDec>
    </class>""",
}

CONFIG__PARSE_PARAMETER_LIST = {
    ')': """<class>
        <parameterList>
        </parameterList>
    </class>""",
    'int x': """<class>
        <parameterList>
            <keyword> int </keyword>
            <identifier> x </identifier>
        </parameterList> 
    </class>""",
    'int Ax, int Ay, int Asize': """<class>
        <parameterList>
            <keyword> int </keyword>
            <identifier> Ax </identifier>
            <symbol> , </symbol>
            <keyword> int </keyword>
            <identifier> Ay </identifier>
            <symbol> , </symbol>
            <keyword> int </keyword>
            <identifier> Asize </identifier>
        </parameterList>
    </class>""",
}

CONFIG__PARSE_SUBROUTINE_BODY = {
    '{ var SquareGame game; }' : """<class>
        <subroutineBody>
            <symbol> { </symbol>
            <varDec>
                <keyword> var </keyword>
                <identifier> SquareGame </identifier>
                <identifier> game </identifier>
                <symbol> ; </symbol>
            </varDec>
            <statements>
            </statements>
            <symbol> } </symbol>
        </subroutineBody>
    </class>""",
    '{do Memory.deAlloc(this); return;}': """<class>
        <subroutineBody>
        <symbol> { </symbol>
        <statements>
            <doStatement>
                <keyword> do </keyword>
                <identifier> Memory </identifier>
                <symbol> . </symbol>
                <identifier> deAlloc </identifier>
                <symbol> ( </symbol>
                <expressionList>
                    <expression>
                        <term>
                            <keyword> this </keyword>
                        </term>
                    </expression>
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
    </class>""",
}

CONFIG__PARSE_SUBROUTINE_DEC = {
    'function int foo() {}' : """<class>
        <subroutineDec>
        <keyword> function </keyword>
        <keyword> int </keyword>
        <identifier> foo </identifier>
        <symbol> ( </symbol>
        <parameterList>
        </parameterList>
        <symbol> ) </symbol>
        <subroutineBody>
            <symbol> { </symbol>
            <statements>
            </statements>
            <symbol> } </symbol>
        </subroutineBody>
    </subroutineDec>
    </class>""",
    'constructor Square new (int Ax, int Ay, int Asize) {}' : """<class>
        <subroutineDec>
        <keyword> constructor </keyword>
        <identifier> Square </identifier>
        <identifier> new </identifier>
        <symbol> ( </symbol>
        <parameterList>
            <keyword> int </keyword>
            <identifier> Ax </identifier>
            <symbol> , </symbol>
            <keyword> int </keyword>
            <identifier> Ay </identifier>
            <symbol> , </symbol>
            <keyword> int </keyword>
            <identifier> Asize </identifier>
        </parameterList>
        <symbol> ) </symbol>
        <subroutineBody>
            <symbol> { </symbol>
            <statements></statements>
            <symbol> } </symbol>
        </subroutineBody>
    </subroutineDec>
    </class>""",
}

CONFIG__PARSE_CLASS_VAR_DEC = {
    'field int size;' : """<class>
        <classVarDec>
            <keyword> field </keyword>
            <keyword> int </keyword>
            <identifier> size </identifier>
            <symbol> ; </symbol>
        </classVarDec>
    </class>""",
    'static int x, y, z;': """<class>
    <classVarDec>
        <keyword> static </keyword>
        <keyword> int </keyword>
        <identifier> x </identifier>
        <symbol> , </symbol>
        <identifier> y </identifier>
        <symbol> , </symbol>
        <identifier> z </identifier>
        <symbol> ; </symbol>
    </classVarDec>
    </class>""",
}

CONFIG__PARSE_CLASS = {
    'class Main {}' : """<class>
        <keyword> class </keyword>
        <identifier> Main </identifier>
        <symbol> { </symbol>
        <symbol> } </symbol>
    </class>""",
    'class Square { field int x, y; field int size; }': """<class>
        <keyword> class </keyword>
        <identifier> Square </identifier>
        <symbol> { </symbol>
        <classVarDec>
            <keyword> field </keyword>
            <keyword> int </keyword>
            <identifier> x </identifier>
            <symbol> , </symbol>
            <identifier> y </identifier>
            <symbol> ; </symbol>
        </classVarDec>
        <classVarDec>
            <keyword> field </keyword>
            <keyword> int </keyword>
            <identifier> size </identifier>
            <symbol> ; </symbol>
        </classVarDec>
        <symbol> } </symbol>
    </class>""",
}
