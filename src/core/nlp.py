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
        self._corpus = PlaintextCorpusReader(str(self._target_dir), self._filename_pattern)
        self._corpus_files = self._corpus.fileids()

    @property
    def corpus_files(self):
        return self._corpus_files

    def raw_text(self, filenames: list[str] = None):
        """Returns the raw text contained within the corpus"""
        return self._corpus.raw(fileids=filenames)

    def complete_sentences(self, filenames: list[str] = None):
        """Returns the text contained within the corpus in the form of a list of sentences,
        where each sentence is a single string"""
        return nltk.sent_tokenize(self._corpus.raw(fileids=filenames))

    def tokenised_sentences(self, filenames: list[str] = None):
        """Returns the text contained within the corpus in the form of a list of sentences,
        where each sentence is a list of word strings"""
        return self._corpus.sents(fileids=filenames)

    def tokenised_words(self, filenames: list[str] = None):
        """Returns the text contained within a corpus in the form of a list of words"""
        return self._corpus.words(fileids=filenames)
