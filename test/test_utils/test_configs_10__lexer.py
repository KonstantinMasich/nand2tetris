from p10.code.const import TokenType


TESTDATA__REMOVE_COMMENTS = {
    # -------------------------------------------------------------------------
    'inline_1': dict(
        code = """let a = b;//Comment number 1""",
        expected = """let a = b;"""
    ),
    'inline_2': dict(
        code = """let a = b; // Comment    number 2""",
        expected = """let a = b; """
    ),
    'inline_3': dict(
        code = """let a = b;         //Comment    number     3    """,
        expected = """let a = b;         """
    ),
    'inline_4': dict(
        code = """let a = b; // Comment number 4
        let c = d;
        """,
        expected = """let a = b; 
        let c = d;
        """,
    ),
    # -------------------------------------------------------------------------
    'multiline_1': dict(
        code = """
        /** Multiline comment 1 */
        let a = b;
        let b = c;
        """,
        expected = """
        
        let a = b;
        let b = c;
        """
    ),
    'multiline_2': dict(
        code = """
        /** 
                Multiline   comment     2
        */
        let a = b;
        let b = c;
        """,
        expected = """
        
        let a = b;
        let b = c;
        """
    ),
    'multiline_3': dict(
        code = """
        /** 
                Multiline   
            comment     
                3

        */
        let a = b;
        let b = c;
        """,
        expected = """
        
        let a = b;
        let b = c;
        """
    ),
    'multiline_4': dict(
        code = """
                /** 
                Multiline   
        comment     4
                */
        let a = b;
        let b = c;
        """,
        expected = """
                
        let a = b;
        let b = c;
        """
    ),
    # -------------------------------------------------------------------------
}


TESTDATA__GET_TOKEN_TYPE = {
    'keyword_1': dict(token =    'int', expected = TokenType.KEYWORD),
    'keyword_2': dict(token =  'class', expected = TokenType.KEYWORD),
    'keyword_3': dict(token =  'while', expected = TokenType.KEYWORD),
    'keyword_4': dict(token = 'return', expected = TokenType.KEYWORD),
    'keyword_5': dict(token =   'void', expected = TokenType.KEYWORD),
    # -------------------------------------------------------------------------
    'symbol_1': dict(token = '{', expected = TokenType.SYMBOL),
    'symbol_2': dict(token = '}', expected = TokenType.SYMBOL),
    'symbol_3': dict(token = '[', expected = TokenType.SYMBOL),
    'symbol_4': dict(token = ';', expected = TokenType.SYMBOL),
    'symbol_5': dict(token = '.', expected = TokenType.SYMBOL),
    # -------------------------------------------------------------------------
    'integer_1': dict(token =     '0', expected = TokenType.INTEGER),
    'integer_2': dict(token =     '1', expected = TokenType.INTEGER),
    'integer_3': dict(token =    '12', expected = TokenType.INTEGER),
    'integer_4': dict(token = '19202', expected = TokenType.INTEGER),
    'integer_5': dict(token = '23320', expected = TokenType.INTEGER),
    # -------------------------------------------------------------------------
    'string_1': dict(token =       '"Hello"', expected = TokenType.STR_CONST),
    'string_2': dict(token = '"Hello world"', expected = TokenType.STR_CONST),
    'string_3': dict(token = '"Hello_world"', expected = TokenType.STR_CONST),
    # -------------------------------------------------------------------------
    'identifier_1': dict(token =    'a', expected = TokenType.IDENTIFIER),
    'identifier_2': dict(token =    'b', expected = TokenType.IDENTIFIER),
    'identifier_3': dict(token = 'main', expected = TokenType.IDENTIFIER),
    'identifier_4': dict(token =  'foo', expected = TokenType.IDENTIFIER),
    'identifier_5': dict(token =  'bar', expected = TokenType.IDENTIFIER),
}
