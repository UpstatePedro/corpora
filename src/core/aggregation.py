"""Handles computations for calculating aggregate statistics from text data"""
from collections import Counter


def word_count(text: list[str], all_lowercase: bool = False) -> Counter:
    """Calculates the number of occurrences for each word in a body of text"""
    if all_lowercase:
        text = [word.lower() for word in text]
    return Counter(text)


def most_common_words(text: list[str], n: int, all_lowercase: bool = False) -> list[tuple]:
    """Calculates the frequency with which each word appears in the text, and returns the top `n` results as a list of
    (word, count) tuples"""
    counts = word_count(text, all_lowercase=all_lowercase)
    return counts.most_common(n)


class WordFrequencyCalculator:

    def __init__(self, sentences_by_document: dict, words_by_document: dict, all_lowercase: bool = False):
        """Calculates a summary of top-n word frequencies from a collection of documents,
        given their filenames, sentence components, and word lists

        :param sentences_by_document: A dict of structure {document_name: [<complete sentences>]}
        :param words_by_document: A dict of structure {document_name: [<word tokens>]}
        :param all_lowercase: Boolean flag to convert all word tokens to lower case before counting frequencies
        """
        self._sentences_by_document = sentences_by_document
        self._words_by_document = words_by_document
        self._all_words = self._combine_word_bags()  # put all words in one bag
        self._all_lowercase = all_lowercase

    def summarise(self, limit: int = None):
        word_counts = most_common_words(self._all_words, n=limit)
        summary = tuple({'word': word[0], 'documents': {}} for word in word_counts)
        for document in self._sentences_by_document.keys():
            for sentence in self._sentences_by_document.get(document):
                for word_summary in summary:
                    if word_summary.get('word') in sentence:
                        word_summary['documents'].setdefault(document, []).append(sentence)
        return summary

    def _combine_word_bags(self) -> list[str]:
        """Combines the word bags for each document into one combined word bag"""
        word_bags = self._words_by_document.values()
        return [word for word_bag in word_bags for word in word_bag]
