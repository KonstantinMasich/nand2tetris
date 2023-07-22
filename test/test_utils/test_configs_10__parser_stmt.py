"""Test configurations for statements."""

import xml.etree.ElementTree as etree
from p10.code.lexer import tokenize


TESTDATA__PARSE_LET_STATEMENT = {
    'let i = i * (-j);': dict(
        tokens=tokenize('let i = i * (-j);'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let j = j / (-2);': dict(
        tokens=tokenize('let j = j / (-2);'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let i = i | j;': dict(
        tokens=tokenize('let i = i | j;'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let a = 18;': dict(
        tokens=tokenize('let a = 18;'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let x = x + 2;': dict(
        tokens=tokenize('let x = x + 2;'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let a[1] = a[2];': dict(
        tokens=tokenize('let a[1] = a[2];'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: ");': dict(
        tokens=tokenize('let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: ");'),
        expected=etree.fromstring("""
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
            </letStatement>"""),
    ),
}

TESTDATA__PARSE_IF_STATEMENT = {
    'if (key) {let direction = direction;}': dict(
        tokens=tokenize('if (key) {let direction = direction;}'),
        expected=etree.fromstring("""
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
            </ifStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'complex-1': dict(
        tokens=tokenize('if (i) { let s = i; } else { let i = i | j; }'),
        expected=etree.fromstring("""
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
            </ifStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'complex-2': dict(
        tokens=tokenize('if (((y + size) < 254) & ((x + size) < 510)) { do erase(); }'),
        expected=etree.fromstring("""
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
            </ifStatement>"""),
    ),
}


TESTDATA__PARSE_WHILE_STATEMENT = {
    'while (~(key = 0)) {}': dict(
        tokens=tokenize('while (~(key = 0)) {}'),
        expected=etree.fromstring("""
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
            </whileStatement>"""),
    ),
}

TESTDATA__PARSE_DO_STATEMENT = {
    'do foo();': dict(
        tokens=tokenize('do foo();'),
        expected=etree.fromstring("""
            <doStatement>
                <keyword> do </keyword>
                <identifier> foo </identifier>
                <symbol> ( </symbol>
                <expressionList></expressionList>
                <symbol> ) </symbol>
                <symbol> ; </symbol>
            </doStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'do Output.printInt(sum / length);': dict(
        tokens=tokenize('do Output.printInt(sum / length);'),
        expected=etree.fromstring("""
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
            </doStatement>"""),
    ),
}

TESTDATA__PARSE_RETURN_STATEMENT = {
    'return;': dict(
        tokens=tokenize('return;'),
        expected=etree.fromstring("""
            <returnStatement>
                <keyword> return </keyword>
                <symbol> ; </symbol>
            </returnStatement>"""),
    ),
    # -------------------------------------------------------------------------
    'return x;': dict(
        tokens=tokenize('return x;'),
        expected=etree.fromstring("""
            <returnStatement>
                <keyword> return </keyword>
                <expression>
                    <term>
                        <identifier> x </identifier>
                    </term>
                </expression>
                <symbol> ; </symbol>
            </returnStatement>"""),
    ),
}
