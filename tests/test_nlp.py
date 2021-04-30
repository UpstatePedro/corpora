from src.core import nlp
import pytest



#################################
#   Module methods
#################################
def test_remove_stop_words():
    input_text = ['A', 'collection', 'of', 'words', 'some', 'of', 'which', 'should', 'not', 'be', 'included', 'in', 'the', 'output']
    expectation = ['collection', 'words', 'included', 'output']
    actual = nlp.remove_stop_words(input_text)
    assert actual == expectation


#################################
#   TxtFileTokeniser
#################################
@pytest.fixture()
def tokeniser():
    tokeniser = nlp.TxtFileTokeniser(
        target_dir='tests/fixtures',
        filename_pattern='.*.txt'
    )
    yield tokeniser


def test_filenames(tokeniser):
    expectation = ['example.txt', 'example2.txt']
    actual = tokeniser.corpus_files
    assert actual == expectation


def test_raw_text(tokeniser):
    expectation = "This is some te"
    actual = tokeniser.raw_text()[:15]
    assert actual == expectation


def test_raw_text_for_filename(tokeniser):
    expectation = "This is another"
    actual = tokeniser.raw_text(filenames=['example2.txt'])[:15]
    assert actual == expectation


def test_complete_sentences_length(tokeniser):
    expectation = 6
    actual = len(tokeniser.complete_sentences())
    assert actual == expectation


def test_complete_sentences_length_for_filename(tokeniser):
    expectation = 3
    actual = len(tokeniser.complete_sentences(filenames=['example.txt']))
    assert actual == expectation


def test_complete_sentences_content(tokeniser):
    expectation = "It has multiple sentences."
    actual = tokeniser.complete_sentences()[1]
    assert actual == expectation


def test_complete_sentences_content_for_filename(tokeniser):
    expectation = "Now we can handle multiple files."
    actual = tokeniser.complete_sentences(filenames=['example2.txt'])[1]
    assert actual == expectation


def test_tokenised_sentences_length(tokeniser):
    expectation = 6
    actual = len(tokeniser.tokenised_sentences())
    assert actual == expectation


def test_tokenised_sentences_length_for_filename(tokeniser):
    expectation = 3
    actual = len(tokeniser.tokenised_sentences(filenames=['example2.txt']))
    assert actual == expectation


def test_tokenised_sentences_content(tokeniser):
    expectation = ["It", "has", "multiple", "sentences", "."]
    actual = tokeniser.tokenised_sentences()[1]
    assert actual == expectation


def test_tokenised_words_length(tokeniser):
    expectation = 53
    actual = len(tokeniser.tokenised_words())
    assert actual == expectation


def test_tokenised_words_length_for_filename(tokeniser):
    expectation = 39
    actual = len(tokeniser.tokenised_words(filenames=['example.txt']))
    assert actual == expectation


def test_tokenised_words_content(tokeniser):
    expectation = [
        'This', 'is', 'some', 'text', '.', 'It', 'has', 'multiple', 'sentences', '.', 'It', 'also', 'has', 'many',
        'copies', 'of', 'several', 'words', ':', 'the', ',', 'the', ',', 'the', ',', 'the', ',', 'bla', ',', 'bla', ',', 'bla', ',', 'raa', ',', 'raa', ',', 'raa', '.'
    ]
    # wrap in list to convert `nltk.corpus.reader.util.StreamBackedCorpusView` to comparable types
    actual = list(tokeniser.tokenised_words(filenames=['example.txt']))
    assert actual == expectation


def test_filter_and_tokenise_words(tokeniser):
    expectation = [
        'text', 'multiple', 'sentences', 'also', 'many',
        'copies', 'several', 'words', 'bla', 'bla', 'bla', 'raa', 'raa', 'raa'
    ]
    # wrap in list to convert `nltk.corpus.reader.util.StreamBackedCorpusView` to comparable types
    actual = tokeniser.filter_and_tokenise_words(filenames=['example.txt'])
    # actual = list(tokeniser. (filenames=['example.txt']))
    assert actual == expectation


