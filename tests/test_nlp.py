from src.core.nlp import TxtFileTokeniser
import pytest


#################################
#   TxtFileTokeniser
#################################
@pytest.fixture()
def tokeniser():
    tokeniser = TxtFileTokeniser(
        target_dir='tests/fixtures',
        filename_pattern='.*.txt'
    )
    yield tokeniser


def test_filenames(tokeniser):
    expectation = ['example.txt', 'example2.txt']
    actual = tokeniser.corpus_files
    assert expectation == actual


def test_raw_text(tokeniser):
    expectation = "This is some te"
    actual = tokeniser.raw_text()[:15]
    assert expectation == actual


def test_raw_text_for_filename(tokeniser):
    expectation = "This is another"
    actual = tokeniser.raw_text(filenames=['example2.txt'])[:15]
    assert expectation == actual


def test_complete_sentences_length(tokeniser):
    expectation = 6
    actual = len(tokeniser.complete_sentences())
    assert expectation == actual


def test_complete_sentences_length_for_filename(tokeniser):
    expectation = 3
    actual = len(tokeniser.complete_sentences(filenames=['example.txt']))
    assert expectation == actual


def test_complete_sentences_content(tokeniser):
    expectation = "It has multiple sentences."
    actual = tokeniser.complete_sentences()[1]
    assert expectation == actual


def test_complete_sentences_content_for_filename(tokeniser):
    expectation = "Now we can handle multiple files."
    actual = tokeniser.complete_sentences(filenames=['example2.txt'])[1]
    assert expectation == actual


def test_tokenised_sentences_length(tokeniser):
    expectation = 6
    actual = len(tokeniser.tokenised_sentences())
    assert expectation == actual


def test_tokenised_sentences_length_for_filename(tokeniser):
    expectation = 3
    actual = len(tokeniser.tokenised_sentences(filenames=['example2.txt']))
    assert expectation == actual


def test_tokenised_sentences_content(tokeniser):
    expectation = ["It", "has", "multiple", "sentences", "."]
    actual = tokeniser.tokenised_sentences()[1]
    assert expectation == actual


def test_tokenised_words_length(tokeniser):
    expectation = 45
    actual = len(tokeniser.tokenised_words())
    assert expectation == actual


def test_tokenised_words_length_for_filename(tokeniser):
    expectation = 31
    actual = len(tokeniser.tokenised_words(filenames=['example.txt']))
    assert expectation == actual


def test_tokenised_words_content(tokeniser):
    expectation = [
        'This', 'is', 'some', 'text', '.', 'It', 'has', 'multiple', 'sentences', '.', 'It', 'also', 'has', 'many',
        'copies', 'of', 'several', 'words', ':', 'bla', ',', 'bla', ',', 'bla', ',', 'raa', ',', 'raa', ',', 'raa', '.'
    ]
    # wrap in list to convert `nltk.corpus.reader.util.StreamBackedCorpusView` to comparable types
    actual = list(tokeniser.tokenised_words(filenames=['example.txt']))
    assert expectation == actual
