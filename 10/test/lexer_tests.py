import unittest
import lexer
import config


class LexerTests(unittest.TestCase):

    def test_get_token_type(self):
        for symbol in config.T_SYMBOLS:
            self.assertEqual('symbol', lexer.get_token_type(symbol))
        for kw in config.T_KEYWORDS:
            self.assertEqual('keyword', lexer.get_token_type(kw))
        for num in [-10, -1, 0, 1, 10, 15, 100, 1000, int(3e7)]:
            self.assertEqual('integerConstant', lexer.get_token_type(str(num)))
        for s in ['"Hello world!"', '"String constant"']:
            self.assertEqual('stringConstant', lexer.get_token_type(s))
        for identifier in ['Main', 'foo', 'bar', 'foo_bar', 'a', 'i', 'x']:
            self.assertEqual('identifier', lexer.get_token_type(identifier))


if __name__ == '__main__':
    unittest.main()
