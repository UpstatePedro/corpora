"""Handles computations for calculating aggregate statistics from text data"""
from collections import Counter


def word_count(text: list[str]) -> Counter:
    """Calculates the number of occurrences for each word in a body of text"""
    return Counter(text)


def most_common_words(text: list[str], n: int) -> list[tuple]:
    """Calculates the frequency with which each word appears in the text, and returns the top `n` results as a list of
    (word, count) tuples"""
    counts = word_count(text)
    return counts.most_common(n)


class WordFrequencyCalculator:
    """
    Calculates a summary of top-n word frequencies from a collection of documents,
    given their filenames, sentence components, and word lists
    """

    def __init__(self, document_sentences: dict, document_words: dict):
        self._document_sentences = document_sentences
        self._document_words = document_words
        self._all_words = self._combine_word_bags()  # put all words in one bag

    def summarise(self, limit: int = None):
        word_counts = most_common_words(self._all_words, n=limit)
        summary = tuple({'word': word[0], 'documents': {}} for word in word_counts)
        for document in self._document_sentences.keys():
            for sentence in self._document_sentences.get(document):
                for word_summary in summary:
                    if word_summary.get('word') in sentence:
                        word_summary['documents'].setdefault(document, []).append(sentence)
        return summary


    def _combine_word_bags(self) -> list[str]:
        """Combines the word bags for each document into one combined word bag"""
        word_bags = self._document_words.values()
        return [word for word_bag in word_bags for word in word_bag]

