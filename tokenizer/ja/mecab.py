# -*- coding: utf-8 -*-
from collections import namedtuple

import MeCab


class MeCabTokenizer(object):

    def __init__(self, user_dic_path='', sys_dic_path=''):
        option = '-Ochasen'
        if user_dic_path:
            option += ' -u {0}'.format(user_dic_path)
        if sys_dic_path:
            option += ' -u {0}'.format(sys_dic_path)
        self._t = MeCab.Tagger(option)

    def separate_words(self, sent):
        words = [token.surface for token in self.tokenize(sent)]

        return words

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