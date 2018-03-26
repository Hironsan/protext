from .utils import maybe_download


def load_data(path='jawiki-neologd.id'):
    url = 'https://storage.googleapis.com/chakki/datasets/public/jawiki/jawiki-neologd-20180320.tar.gz'
    path = maybe_download(path, origin=url, extract=True)
    print(path)

    with open(path) as f:
        for line in f:
            yield list(map(int, line.strip().split()))


def get_word_index(path='jawiki-neologd.dic'):
    url = ''
    path = maybe_download(path, origin=url, extract=True)

    word_index = {}
    with open(path) as f:
        for line in f:
            id, word, _ = line.rstrip().split('\t')
            word_index[word] = id

    return word_index
