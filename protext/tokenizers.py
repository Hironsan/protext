# -*- coding: utf-8 -*-
"""
Tokenizer implementations.
"""
from collections import namedtuple

import MeCab
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter, POSKeepFilter


class BaseTokenizer(object):

    token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,'
                                'infl_type, infl_form, base_form, reading, phonetic')

    def __init__(self, user_dic_path='', sys_dic_path=''):
        pass

    def tokenize(self, text):
        pass


class MeCabTokenizer(object):

    def __init__(self, user_dic_path='', sys_dic_path=''):
        option = '-Ochasen'
        if user_dic_path:
            option += ' -u {0}'.format(user_dic_path)
        if sys_dic_path:
            option += ' -u {0}'.format(sys_dic_path)
        self._t = MeCab.Tagger(option)

    def tokenize(self, sent):
        tokens = []
        self._t.parse('')  # for UnicodeDecodeError
        node = self._t.parseToNode(sent)

        while node:
            token = namedtuple('Token', 'surface, pos, pos_detail1, pos_detail2, pos_detail3,\
                                                     infl_type, infl_form, base_form, reading, phonetic')
            feature = node.feature.split(',')
            token.surface = node.surface    # 表層形
            token.pos = feature[0]          # 品詞
            token.pos_detail1 = feature[1]  # 品詞細分類1
            token.pos_detail2 = feature[2]  # 品詞細分類2
            token.pos_detail3 = feature[3]  # 品詞細分類3
            token.infl_type = feature[4]    # 活用型
            token.infl_form = feature[5]    # 活用形
            token.base_form = feature[6]    # 原型
            token.reading = feature[7]      # 読み
            token.phonetic = feature[8]     # 発音
            tokens.append(token)
            node = node.next

        return tokens

    def filter_by_pos(self, sent, pos='名詞'):
        tokens = [token for token in self.tokenize(sent) if token.pos == pos]

        return tokens


class JanomeTokenizer(BaseTokenizer):

    def __init__(self, user_dic_path='', user_dic_enc='utf8'):
        super(BaseTokenizer).__init__()
        self._t = Tokenizer(udic=user_dic_path, udic_enc=user_dic_enc)

    def analyze(self, text, tokenize):
        tokens = []
        for t in tokenize(text):
            poses = t.part_of_speech.split(',')
            token = self.token(*[t.surface] +
                                poses +
                                [t.infl_type, t.infl_form, t.base_form, t.reading, t.phonetic])
            tokens.append(token)

        return tokens

    def tokenize(self, text):
        return self.analyze(text, self._t.tokenize)

    def noun_phrases(self, text):
        token_filters = [CompoundNounFilter(), POSKeepFilter(['名詞'])]
        a = Analyzer(tokenizer=self._t, token_filters=token_filters)

        return self.analyze(text, a.analyze)

    def filter_by_pos(self, text, poses=('名詞',)):
        token_filters = [POSKeepFilter(poses)]
        a = Analyzer(tokenizer=self._t, token_filters=token_filters)

        return self.analyze(text, a.analyze)
