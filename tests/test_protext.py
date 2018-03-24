# -*- coding: utf-8 -*-
import unittest

from protext import ProText


class TestProText(unittest.TestCase):

    def setUp(self):
        text = 'Janomeは形態素解析器'
        self.doc = ProText(text)

    def test_words(self):
        words = ['Janome', 'は', '形態素', '解析', '器']
        self.assertEqual(self.doc.words, words)

    def test_tags(self):
        tags = [('Janome', '名詞'), ('は', '助詞'), ('形態素', '名詞'), ('解析', '名詞'), ('器', '名詞')]
        self.assertEqual(self.doc.tags, tags)

    def test_nouns(self):
        self.assertEqual(self.doc.nouns, ['Janome', '形態素', '解析', '器'])

    def test_noun_phrases(self):
        self.assertEqual(self.doc.noun_phrases, ['Janome', '形態素解析器'])

    def test_readings(self):
        self.assertEqual(self.doc.readings, ['*', 'ハ', 'ケイタイソ', 'カイセキ', 'キ'])
