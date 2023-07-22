"""Test configurations for class-related stuff."""

import xml.etree.ElementTree as etree
from p10.code.lexer import tokenize


TESTDATA__PARSE_CLASS = {
    'simple-1': dict(
        tokens=tokenize('class Main {}'),
        expected=etree.fromstring("""
            <class>
                <keyword> class </keyword>
                <identifier> Main </identifier>
                <symbol> { </symbol>
                <symbol> } </symbol>
            </class>"""),
    ),
    # -------------------------------------------------------------------------
    'complex-1': dict(
        tokens=tokenize('class Square { field int x, y; field int size; }'),
        expected=etree.fromstring("""
            <class>
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
            </class>"""),
    ),
}

TESTDATA__PARSE_CLASS_VAR_DEC = {
    'field int size;': dict(
        tokens=tokenize('field int size;'),
        expected=etree.fromstring("""
            <classVarDec>
                <keyword> field </keyword>
                <keyword> int </keyword>
                <identifier> size </identifier>
                <symbol> ; </symbol>
            </classVarDec>"""),
    ),
    # -------------------------------------------------------------------------
    'static int x, y, z;': dict(
        tokens=tokenize('static int x, y, z;'),
        expected=etree.fromstring("""
            <classVarDec>
                <keyword> static </keyword>
                <keyword> int </keyword>
                <identifier> x </identifier>
                <symbol> , </symbol>
                <identifier> y </identifier>
                <symbol> , </symbol>
                <identifier> z </identifier>
                <symbol> ; </symbol>
            </classVarDec>"""),
    ),
}