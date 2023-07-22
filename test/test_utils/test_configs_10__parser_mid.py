"""Test configurations for mid-level stuff: functions, methods, variables, etc."""

import xml.etree.ElementTree as etree
from p10.code.lexer import tokenize

TESTDATA__PARSE_PARAMETER_LIST = {
    ')': dict(
        tokens=tokenize(')'),
        expected=etree.fromstring("""<parameterList />"""),
    ),
    # -------------------------------------------------------------------------
    'int x': dict(
        tokens=tokenize('int x'),
        expected=etree.fromstring("""
            <parameterList>
                <keyword> int </keyword>
                <identifier> x </identifier>
            </parameterList>"""),
    ),
    'int Ax, int Ay, int Asize': dict(
        tokens=tokenize('int Ax, int Ay, int Asize'),
        expected=etree.fromstring("""
            <parameterList>
                <keyword> int </keyword>
                <identifier> Ax </identifier>
                <symbol> , </symbol>
                <keyword> int </keyword>
                <identifier> Ay </identifier>
                <symbol> , </symbol>
                <keyword> int </keyword>
                <identifier> Asize </identifier>
            </parameterList>"""),
    ),
}

TESTDATA__PARSE_VAR_DEC = {
    'var int i, j': dict(
        tokens=tokenize('var int i, j;'),
        expected=etree.fromstring("""
            <varDec>
                <keyword> var </keyword>
                <keyword> int </keyword>
                <identifier> i </identifier>
                <symbol> , </symbol>
                <identifier> j </identifier>
                <symbol> ; </symbol>
            </varDec>"""),
    ),
    # -------------------------------------------------------------------------
    'var boolean exit;': dict(
        tokens=tokenize('var boolean exit;'),
        expected=etree.fromstring("""
            <varDec>
                <keyword> var </keyword>
                <keyword> boolean </keyword>
                <identifier> exit </identifier>
                <symbol> ; </symbol>
            </varDec>"""),
    ),
}

TESTDATA__PARSE_SUBROUTINE_BODY = {
    'simple-1': dict(
        tokens=tokenize('{ var SquareGame game; }'),
        expected=etree.fromstring("""
            <subroutineBody>
                <symbol> { </symbol>
                <varDec>
                    <keyword> var </keyword>
                    <identifier> SquareGame </identifier>
                    <identifier> game </identifier>
                    <symbol> ; </symbol>
                </varDec>
                <statements />
                <symbol> } </symbol>
            </subroutineBody>"""),
    ),
    # -------------------------------------------------------------------------
    'complex-1': dict(
        tokens=tokenize('{do Memory.deAlloc(this); return;}'),
        expected=etree.fromstring("""
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
            </subroutineBody>"""),
    ),
}

TESTDATA__PARSE_SUBROUTINE_DEC = {
    'simple-1': dict(
        tokens=tokenize('function int foo() {}'),
        expected=etree.fromstring("""
            <subroutineDec>
                <keyword> function </keyword>
                <keyword> int </keyword>
                <identifier> foo </identifier>
                <symbol> ( </symbol>
                <parameterList />
                <symbol> ) </symbol>
                <subroutineBody>
                    <symbol> { </symbol>
                    <statements />
                    <symbol> } </symbol>
                </subroutineBody>
            </subroutineDec>"""),
    ),
    # -------------------------------------------------------------------------
    'complex-1': dict(
        tokens=tokenize('constructor Square new (int Ax, int Ay, int Asize) {}'),
        expected=etree.fromstring("""
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
                    <statements />
                    <symbol> } </symbol>
                </subroutineBody>
            </subroutineDec>"""),
    ),
}


TESTDATA__PARSE_SUBROUTINE_CALL = {
    'foo()': dict(
        tokens=tokenize('foo()'),
        expected=etree.fromstring("""
            <__temp__>
                <identifier> foo </identifier>
                <symbol> ( </symbol>
                <expressionList></expressionList>
                <symbol> ) </symbol>
            </__temp__>"""),
    ),
    # -------------------------------------------------------------------------
    'Screen.setColor(true)': dict(
        tokens=tokenize('Screen.setColor(true)'),
        expected=etree.fromstring("""
            <__temp__>
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
            </__temp__>"""),
    ),
    # -------------------------------------------------------------------------
    'game.run()': dict(
        tokens=tokenize('game.run()'),
        expected=etree.fromstring("""
            <__temp__>
                <identifier> game </identifier>
                <symbol> . </symbol>
                <identifier> run </identifier>
                <symbol> ( </symbol>
                <expressionList></expressionList>
                <symbol> ) </symbol>
            </__temp__>"""),
    ),
    # -------------------------------------------------------------------------
    'complex': dict(
        tokens=tokenize('Screen.drawRectangle((x + size) - 1, y, x + size, y + size)'),
        expected=etree.fromstring("""
            <__temp__>
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
            </__temp__>"""),
    ),
}
