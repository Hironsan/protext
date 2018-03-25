# -*- coding: utf-8 -*-


class Word(object):
    
    def __init__(self, surface, pos, pos_detail1, pos_detail2, pos_detail3,
                 infl_type, infl_form, base_form, reading='', phonetic=''):
        self.surface = surface          # 表層形
        self.pos = pos                  # 品詞
        self.pos_detail1 = pos_detail1  # 品詞細分類1
        self.pos_detail2 = pos_detail2  # 品詞細分類2
        self.pos_detail3 = pos_detail3  # 品詞細分類3
        self.infl_type = infl_type      # 活用型
        self.infl_form = infl_form      # 活用形
        self.base_form = base_form      # 原型
        self.reading = reading          # 読み
        self.phonetic = phonetic        # 発音

    @property
    def embedding(self):
        """The word embedding for this word.

        Returns:
            word embedding, array-like object.
        """
        return None

    @property
    def synsets(self):
        """The list of Synset objects for this Word.

        Returns:
            list of Synsets.
        """
        return self.get_synsets(pos=None)

    @property
    def definitions(self):
        """The list of definitions for this word. Each definition corresponds to a synset.

        Returns:
            list of definitions.
        """
        return self.define(pos=None)

    def get_synsets(self, pos=None):
        """Return a list of Synset objects for this word.

        Args:
            pos: A part-of-speech tag to filter upon. If ``None``, all
            synsets for all parts of speech will be loaded.

        Returns:
            list of Synsets
        """
        return _wordnet.synsets(self.string, pos)

    def define(self, pos=None):
        """Return a list of definitions for this word. Each definition
        corresponds to a synset for this word.

        Args:
            pos: A part-of-speech tag to filter upon. If ``None``, definitions
            for all parts of speech will be loaded.

        Returns:
            List of strings
        """
        return [syn.definition() for syn in self.get_synsets(pos=pos)]
