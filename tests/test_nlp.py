from src.core.nlp import TxtFileTokeniser
import pytest
#################################
#   TxtFileTokeniser
#################################
@pytest.fixture()
def setup_tokeniser():
    tokeniser = TxtFileTokeniser(
        target_dir='tests/fixtures',
        filename_pattern='example.txt'
    )
    yield tokeniser


def test_raw_text(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = "This is some te"
    actual = tokeniser.raw_text[:15]
    assert expectation == actual


def test_complete_sentences_length(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = 3
    actual = len(tokeniser.complete_sentences)
    assert expectation == actual


def test_complete_sentences_content(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = "It has multiple sentences."
    actual = tokeniser.complete_sentences[1]
    assert expectation == actual


def test_tokenised_sentences_length(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = 3
    actual = len(tokeniser.tokenised_sentences)
    assert expectation == actual


def test_tokenised_sentences_content(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = ["It", "has", "multiple", "sentences", "."]
    actual = tokeniser.tokenised_sentences[1]
    assert expectation == actual


def test_tokenised_words_length(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = 31
    actual = len(tokeniser.tokenised_words)
    assert expectation == actual


def test_tokenised_words_content(setup_tokeniser):
    tokeniser = setup_tokeniser
    expectation = [
        'This', 'is', 'some', 'text', '.', 'It', 'has', 'multiple', 'sentences', '.', 'It', 'also', 'has', 'many',
        'copies', 'of', 'several', 'words', ':', 'bla', ',', 'bla', ',', 'bla', ',', 'raa', ',', 'raa', ',', 'raa', '.'
    ]
    # wrap in list to convert `nltk.corpus.reader.util.StreamBackedCorpusView` to comparable types
    actual = list(tokeniser.tokenised_words)
    assert expectation == actual
