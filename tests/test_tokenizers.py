# -*- coding: utf-8 -*-
import unittest

from protext.tokenizers import JanomeTokenizer
from protext.tokenizers import MeCabTokenizer


class JanomeTokenizerTest(unittest.TestCase):

    def setUp(self):
        self.sent = 'Janomeは形態素解析器'
        self.tokenizer = JanomeTokenizer()

    def test_tokenize(self):
        tokens = self.tokenizer.tokenize(self.sent)

    def test_filter_by_pos(self):
        tokens = self.tokenizer.filter_by_pos(self.sent)
        surfaces = [token.surface for token in tokens]
        self.assertEqual(surfaces, ['Janome', '形態素', '解析', '器'])

    def test_noun_phrases(self):
        tokens = self.tokenizer.noun_phrases(self.sent)
        surfaces = [token.surface for token in tokens]
        self.assertEqual(surfaces, ['Janome', '形態素解析器'])


class MeCabTokenizerTest(unittest.TestCase):

    def setUp(self):
        self.sent = '太郎は花子に花束をあげました。'
        self.tokenizer = MeCabTokenizer()

    def test_tokenize(self):
        tokens = self.tokenizer.tokenize(self.sent)

    def test_filter_by_pos(self):
        tokens = self.tokenizer.filter_by_pos(self.sent)
        surfaces = [token.surface for token in tokens]
        self.assertEqual(surfaces, ['太郎', '花子', '花束'])
