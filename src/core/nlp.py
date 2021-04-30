import pathlib
from typing import Union

import nltk
from nltk.corpus import PlaintextCorpusReader, stopwords


def remove_stop_words(words: list[str], stop_words: list[str] = stopwords.words('english')):
    """Filters words out from a list wherever they appear in the stop_words"""
    stop_words_lookup = {
        stop_word: False
        for stop_word in stop_words
    }
    return list(filter(lambda word: stop_words_lookup.get(word.lower(), True), words))


def filter_words_for_alphanumerics(word_tokens):
    """Remove non-alphanumeric elements from a list of strings"""
    alphanumeric_words = [word for word in word_tokens if word.isalnum()]
    return alphanumeric_words


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

    def filter_and_tokenise_words(self, filenames: list[str] = None):
        """Removes non-alphanumeric & stop-words from the corpus' words"""
        word_tokens = self.tokenised_words(filenames=filenames)
        alphanumeric_words = filter_words_for_alphanumerics(word_tokens)
        filtered_words = remove_stop_words(alphanumeric_words)
        return filtered_words
