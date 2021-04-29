"""
Orchestration logic for processing text documents.
Provides the standard API through which ingestion, processing & formatting logic should be called.
"""
import pathlib
from typing import Union

from src.core.aggregation import WordFrequencyCalculator
from src.core.nlp import TxtFileTokeniser


def summarise_directory(target_dir: Union[str, pathlib.Path], limit: int = 5) -> tuple:
    """Processes a directory
    The summary will be a tuple of dicts, with each element representing the most common words in the corpus
    (in descending order of frequency).
    NB. If multiple words have the same frequency and straddle the word limit, the words included in the response is
    determined by the order in which they are encountered rather than alphabetical order.

    The summary takes the following structure:

    summary = (
        {
            'word': "bla",
            'documents': {
                'filename_1.txt': [
                    "Sentence containing 'bla'.",
                    "Another sentence that uses bla!"
                ],
                'filename_2.txt': [
                    "bla bla bla!!!"
                ]
            }
        },
        {
            'word': "raa",
            'documents': {
                'filename_1.txt': [
                    "A story about raa"
                ],
            }
        }
    )

    :param target_dir: The directory from which to read the text files for summarisation
    :param limit: The number of words to include in the results (sorted in order of frequency of occurrence)
    :return: tuple summary of the top words found in the text located in the specified directory
    """
    complete_sentences = {}
    tokenised_sentences = {}
    words = {}

    tokeniser = TxtFileTokeniser(target_dir=target_dir)
    for filename in tokeniser.corpus_files:
        complete_sentences.update({filename: tokeniser.complete_sentences(filenames=[filename])})
        tokenised_sentences.update({filename: tokeniser.tokenised_sentences(filenames=[filename])})
        word_tokens = tokeniser.tokenised_words(filenames=[filename])
        # Remove punctuation tokens from each word bag (assume we do not want these in the results):
        alphanumeric_words = [word for word in word_tokens if word.isalnum()]
        # TODO: Need to remove stop words:
        # from nltk.corpus import stopwords
        # stopwords.words('english')
        words.update({filename: alphanumeric_words})

    # Aggregate the word summaries and collate the output
    wf_calculator = WordFrequencyCalculator(
        sentences_by_document=complete_sentences,
        words_by_document=words
    )
    wf_summary = wf_calculator.summarise(limit=limit)
    return wf_summary
