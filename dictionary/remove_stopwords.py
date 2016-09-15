stoplist = set('for a of the and to in'.split())


def remove_stopwords(words):
    words = [word for word in words if word not in stoplist]

    return words
