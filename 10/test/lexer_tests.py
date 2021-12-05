import sys
import os
import unittest
sys.path.insert(0, f'{os.path.dirname(__file__)[:-5]}/jack_compiler')
import lexer
import config


class LexerTests(unittest.TestCase):

    def test_clean_code(self):
        with open('jack_src_code/comments_src.jack', 'r') as cmt_file, \
             open('jack_src_code/no_comments_src.jack', 'r') as no_cmt_file:
            code        = cmt_file.readlines()
            clean_code  = lexer.clean_code(''.join(code))
            correct_ans = ''.join([x.replace('\n', '') for x in no_cmt_file.readlines()])
            self.assertEqual(correct_ans.replace(' ', ''), clean_code.replace(' ', ''))

    def test_get_token_type(self):
        for symbol in config.T_SYMBOLS:
            self.assertEqual('symbol', lexer.get_token_type(symbol))
        for kw in config.T_KEYWORDS:
            self.assertEqual('keyword', lexer.get_token_type(kw))
        for num in [-10, -1, 0, 1, 10, 15, 100, 1000, int(3e7)]:
            self.assertEqual('integerConstant', lexer.get_token_type(str(num)))
        for s in ['"Hello world!"', '"String constant"']:
            self.assertEqual('StringConstant', lexer.get_token_type(s))
        for identifier in ['Main', 'foo', 'bar', 'foo_bar', 'a', 'i', 'x']:
            self.assertEqual('identifier', lexer.get_token_type(identifier))


if __name__ == '__main__':
    unittest.main()
