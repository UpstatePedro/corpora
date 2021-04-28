from src.core import aggregation
from src.core.aggregation import WordFrequencyCalculator


def test_word_counts():
    input_text = ['this', 'that', 'the', 'other', 'other']
    actual = aggregation.word_count(input_text)
    expected = {
        'this': 1,
        'that': 1,
        'the': 1,
        'other': 2
    }
    assert expected == actual


def test_most_common():
    """Confirm that the most common words are returned in order.
    If multiple words have the same frequency as the threshold for inclusion, they are selected based on the
    order in which the words are encountered in the text.
    """
    input_text = ['this', 'that', 'the', 'other', 'other']
    actual = aggregation.most_common_words(input_text, 2)
    expected = [
        ('other', 2),
        ('this', 1)
    ]
    assert expected == actual


################################################
#   Tests for WordFrequencyCalculator
################################################


def test_initialisation():
    sentences = {
        'example.txt': [
            "This is some text.",
            "It has multiple sentences.",
            "It also has many copies of several words: bla, bla, bla, raa, raa, raa."
        ]
    }
    words = {
        'example.txt': [
            "this", "is", "some", "text",
            "it", "has", "multiple", "sentences",
            "it", "also", "has", "many", "copies", "of", "several", "words",
            "bla", "bla", "bla", "raa", "raa", "raa"
        ]
    }
    calculator = WordFrequencyCalculator(
        sentences_by_document=sentences,
        words_by_document=words,
    )
    actual = calculator.summarise(limit=2)

    expectation = (
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

    assert expectation == actual


def test_combine_word_bags():
    sentences = {}  # Not relevant to this test
    words = {
        0: ['one'],
        1: ['two', 'three'],
        2: ['four']
    }
    calculator = WordFrequencyCalculator(
        sentences_by_document=sentences,
        words_by_document=words,
    )
    actual = calculator._combine_word_bags()
    expected = ['one', 'two', 'three', 'four']
    assert expected == actual
