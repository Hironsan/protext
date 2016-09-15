from pprint import pprint

from gensim import corpora
from .remove_words import remove_words_less_than_n
from .remove_stopwords import remove_stopwords


documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


def tokenize(sent):
    words = [word for word in sent.lower().split()]

    return words


texts = [[word for word in tokenize(document)] for document in documents]
texts = [remove_stopwords(words) for words in texts]
texts = remove_words_less_than_n(texts)


pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('deerwester.dict')  # store the dictionary, for future reference
print(dictionary.token2id)
print(dict(dictionary.items()))
