from protext.tokenizers import JanomeTokenizer


class ProText(object):

    tokenizer = JanomeTokenizer()

    def __init__(self, text):
        self.text = text

    def entities(self):
        pass

    @property
    def tags(self):
        return [(token.surface, token.pos) for token in self.tokenizer.tokenize(self.text)]

    @property
    def nouns(self):
        return [token.surface for token in self.tokenizer.filter_by_pos(self.text)]

    @property
    def noun_phrases(self):
        return [token.surface for token in self.tokenizer.noun_phrases(self.text)]

    @property
    def readings(self):
        return [token.reading for token in self.tokenizer.tokenize(self.text)]

    def sentences(self):
        pass
