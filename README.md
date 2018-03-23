# protext: Simplified Japanese Text Processing

protext is a Python library for processing Japanese text.
It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

```python
from protext import ProText

text = """
"""

doc = ProText(text)
doc.tags

doc.noun_phrases
```

## Features

* Noun phrase extraction
* Part-of-speech tagging
* Tokenization (splitting text into words and sentences)
* Parsing
* Word inflection (pluralization and singularization) and lemmatization
* WordNet integration
* Word Embeddings

## Installation

To install protext, simply run:

```bash
$ pip install protext
$ python -m protext.download_corpora
```

## License

MIT licensed. See the bundled LICENSE file for more details.
