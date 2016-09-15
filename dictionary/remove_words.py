# -*- coding: utf-8 -*-
from collections import defaultdict


def remove_words_less_than_n(texts, n=1):
    """
    Remove words that appear less than n.
    :param texts:
    :param n:
    :return: texts
    """
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > n]
             for text in texts]

    return texts
