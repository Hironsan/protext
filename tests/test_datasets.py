import unittest

from protext.datasets import jawiki


class TestDataset(unittest.TestCase):

    def test_jawiki_load_data(self):
        docs = jawiki.load_data()
        doc = docs.__next__()
        self.assertIsInstance(doc, list)
