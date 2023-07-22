"""Test configurations for terms and expressions."""

import xml.etree.ElementTree as etree
from p10.code.lexer import tokenize


TESTDATA__PARSE_TERM = {
    # ----------------------------- Integer -----------------------------------
    '0': dict(
        tokens=tokenize('0'),
        expected=etree.fromstring('<term><integerConstant> 0 </integerConstant></term>'),
    ),
    '1': dict(
        tokens=tokenize('1'),
        expected=etree.fromstring('<term><integerConstant> 1 </integerConstant></term>'),
    ),
    '42': dict(
        tokens=tokenize('42'),
        expected=etree.fromstring('<term><integerConstant> 42 </integerConstant></term>'),
    ),
    # ------------------------------ Keyword ----------------------------------
    'int': dict(
        tokens=tokenize('int'),
        expected=etree.fromstring('<term><keyword> int </keyword></term>'),
    ),
    'true': dict(
        tokens=tokenize('true'),
        expected=etree.fromstring('<term><keyword> true </keyword></term>'),
    ),
    'null': dict(
        tokens=tokenize('null'),
        expected=etree.fromstring('<term><keyword> null </keyword></term>'),
    ),
    # ------------------------------ String -----------------------------------
    'string_1': dict(
        tokens=tokenize('"Hello world!"'),
        expected=etree.fromstring('<term><stringConstant> Hello world! </stringConstant></term>'),
    ),
    # ------------------------ varName [ expression ] -------------------------
    'a[i]': dict(
        tokens=tokenize('a[i]'),
        expected=etree.fromstring("""
            <term>
                <identifier> a </identifier>
                <symbol> [ </symbol>
                <expression>
                    <term>
                        <identifier> i </identifier>
                    </term>
                </expression>
                <symbol> ] </symbol>
            </term>"""),
    ),
    'a[2 + 3]': dict(
        tokens=tokenize('a[2+3]'),
        expected=etree.fromstring("""
            <term>
                <identifier> a </identifier>
                <symbol> [ </symbol>
                <expression>
                    <term>
                        <integerConstant> 2 </integerConstant>
                    </term>
                    <symbol> + </symbol>
                    <term>
                        <integerConstant> 3 </integerConstant>
                    </term>
                </expression>
                <symbol> ] </symbol>
            </term>"""),
    ),
    # ------------------------------ Identifier  ------------------------------
    'foo': dict(
        tokens=tokenize('foo'),
        expected=etree.fromstring('<term><identifier> foo </identifier></term>')),
    'Main': dict(
        tokens=tokenize('Main'),
        expected=etree.fromstring('<term><identifier> Main </identifier></term>')),
    # --------------------------- Subroutine call -----------------------------
    # TODO: ADD!
    # TODO: ADD!
    # TODO: ADD!
    # ---------------------------- ( expression )  ----------------------------
    '(a*9)': dict(
        tokens=tokenize('(a * 9)'),
        expected=etree.fromstring("""
            <term>
                <symbol> ( </symbol>
                <expression>
                    <term>
                        <identifier> a </identifier>
                    </term>
                    <symbol> * </symbol>
                    <term>
                        <integerConstant> 9 </integerConstant>
                    </term>
                </expression>
                <symbol> ) </symbol>
            </term>"""),
    ),
    # ---------------------------- Unary operator -----------------------------
    '-j': dict(
        tokens=tokenize('-j'),
        expected=etree.fromstring("""
            <term>
                <symbol> - </symbol>
                <term>
                    <identifier> j </identifier>
                </term>
            </term>""")
    ),
    '-2': dict(
        tokens=tokenize('-2'),
        expected=etree.fromstring("""
            <term>
                <symbol> - </symbol>
                <term>
                    <integerConstant> 2 </integerConstant>
                </term>
            </term>""")
    ),
}

TESTDATA__PARSE_EXPRESSION = {
    '4': dict(
        tokens=tokenize('4'),
        expected=etree.fromstring("""
            <expression><term><integerConstant> 4 </integerConstant></term></expression>"""),
    ),
    'y+size': dict(
        tokens=tokenize('y + size'),
        expected=etree.fromstring("""
            <expression>
                <term>
                    <identifier> y </identifier>
                </term>
                <symbol> + </symbol>
                <term>
                    <identifier> size </identifier>
                </term>
            </expression>"""),
    ),
    'key = 0': dict(
        tokens=tokenize('key=0'),
        expected=etree.fromstring("""
            <expression>
                <term>
                    <identifier> key </identifier>
                </term>
                <symbol> = </symbol>
                <term>
                    <integerConstant> 0 </integerConstant>
                </term>
            </expression>"""),
    ),
    '~(key = a)': dict(
        tokens=tokenize('~(key = a)'),
        expected=etree.fromstring("""
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
                                <identifier> a </identifier>
                            </term>
                        </expression>
                        <symbol> ) </symbol>
                    </term>
                </term>
            </expression>"""),
    ),
}

TESTDATA__PARSE_EXPRESSION_LIST = {
    '2, 3': dict(
        tokens=tokenize('2, 3'),
        expected=etree.fromstring("""
            <expressionList>
                <expression>
                    <term>
                        <integerConstant> 2 </integerConstant>
                    </term>
                </expression>
                <symbol> , </symbol>
                <expression>
                    <term>
                        <integerConstant> 3 </integerConstant>
                    </term>
                </expression>
            </expressionList>"""),
    ),
}

# ╔════════════════════════════════════════════════════════════════════════════════════════════╗
# ║                                        MISC                                                ║
# ╚════════════════════════════════════════════════════════════════════════════════════════════╝
TESTDATA__ADD_TOKENS_AND_ADVANCE = {
    'a[i]': dict(
        tokens=tokenize('a[i]'),
        expected='<__test__><identifier> a </identifier><symbol> [ </symbol>'
                 '<identifier> i </identifier><symbol> ] </symbol></__test__>'),
    # -------------------------------------------------------------------------
    '2 + 3': dict(
        tokens=tokenize('2 + 3'),
        expected='<__test__><integerConstant> 2 </integerConstant>'
                 '<symbol> + </symbol><integerConstant> 3 </integerConstant></__test__>'),
    # -------------------------------------------------------------------------
}
