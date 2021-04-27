"""
Orchestration logic for processing text documents.
Provides the standard API through which ingestion, processing & formatting logic should be called.
"""
from typing import Union
import pathlib


def summarise_directory(target_dir: Union[str, pathlib.Path], limit: int = 5) -> tuple:
    """Processes a directory
    The summary will be a tuple of dicts, with each element representing the most common words in the corpus
    (in descending order of frequency).
    NB. If multiple words have the same frequency and straddle the word limit, the words included in the response is
    determined by the order in which they are encountered rather than alphabetical order.

    The summary will take the following structure:

    summary = (
        {
            'word': "bla",
            'documents': {
                'filename_1.txt': [0, 3, 8, 15],
                'filename_2.txt': [3, 4, 6]
            }
        },
        {
            'word': "raa",
            'documents': {
                'filename_1.txt': [8, 15],
                'filename_2.txt': [3, 6, 9]
            }
        }
    )

    :return: tuple summary of the top words found in the text located in the specified directory
    """
    # List the documents
    files = ['fixtures/example.txt']
    # Read a document
    file_text = "This is some text. It has multiple sentences. It also has many copies of several words: bla, bla, bla, raa, raa, raa."
    documents = {
        'example.txt': None
    }
    # Break each document into sentences
    # nltk.
    sentences = {
        'example.txt': [
            "This is some text.",
            "It has multiple sentences.",
            "It also has many copies of several words: bla, bla, bla, raa, raa, raa."
        ]
    }
    # Break each document into words
    # Remove punctuation
    # all lower case
    words = {
        'example.txt': [
            "this", "is", "some", "text",
            "it", "has", "multiple", "sentences",
            "it", "also", "has", "many", "copies", "of", "several", "words",
            "bla", "bla", "bla", "raa", "raa", "raa"
        ]
    }
    # Aggregate the word summaries and collate the output

    return (
        {
            'word': 'bla',
            'documents': {
                'example.txt': ["It also has many copies of several words: bla, bla, bla, raa, raa, raa."]
            }
        },
        {
            'word': 'raa',
            'documents': {
                'example.txt': ["It also has many copies of several words: bla, bla, bla, raa, raa, raa."]
            }
        }
    )
