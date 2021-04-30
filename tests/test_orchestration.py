import pytest

from src.core import orchestration


def test_summarise_directory():
    """End-to-end test case: a summary of the most common words found in the text inside the directory provided"""
    target_dir = "tests/fixtures/"
    actual = orchestration.summarise_directory(target_dir, limit=2)
    expected = (
        {
            'word': 'bla',
            'documents': {
                'example.txt': ["It also has many copies of several words: the, the, the, the, bla, bla, bla, raa, raa, raa."]
            }
        },
        {
            'word': 'raa',
            'documents': {
                'example.txt': ["It also has many copies of several words: the, the, the, the, bla, bla, bla, raa, raa, raa."]
            }
        }
    )
    assert actual == expected
