import os.path
from typing import Union
import pathlib
import nltk
from nltk.corpus import PlaintextCorpusReader


class TxtFileTokeniser:
    """Wrapper around the NLTK PlaintextCorpusReader, providing an API for tokenising a corpus into
     sentences & words.
    """

    def __init__(self, target_dir: Union[str, pathlib.Path], filename_pattern: str = None):
        self._target_dir = pathlib.Path(target_dir)
        self._filename_pattern = filename_pattern if filename_pattern else '.*'
        # Not using dependency injection here because this class is intended to be tightly coupled with the nltk reader
        self._corpus = PlaintextCorpusReader(str(self._target_dir), self._filename_pattern)

    @property
    def raw_text(self):
        """Returns the raw text contained within the corpus"""
        return self._corpus.raw()

    @property
    def complete_sentences(self):
        """Returns the text contained within the corpus in the form of a list of sentences,
        where each sentence is a single string"""
        return nltk.sent_tokenize(self._corpus.raw())

    @property
    def tokenised_sentences(self):
        return self._corpus.sents()

    @property
    def tokenised_words(self):
        return self._corpus.words()
