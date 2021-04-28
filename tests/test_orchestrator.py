import pytest

from src.core import orchestrator


def test_summarise_directory():
    """Returns a summary representation of the text found in the directory provided"""
    target_dir = "tests/fixtures/"
    actual = orchestrator.summarise_directory(target_dir, limit=2)

    expected = (
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

    assert expected == actual
