from src.core import formatting


def test_shortform_summary():
    longform_summary = (
        {
            'word': 'bla',
            'documents': {
                'example.txt': ["It also has many copies of several words: the, the, the, the, bla, bla, bla, raa, raa, raa."],
                'imaginary.txt': [
                    "The, bla, bla, bla, raa, raa, raa."
                    "Holy bla!"
                ]
            }
        },
        {
            'word': 'raa',
            'documents': {
                'example.txt': ["It also has many copies of several words: the, the, the, the, bla, bla, bla, raa, raa, raa."]
            }
        }
    )
    expected = (
        {'word': 'bla', 'documents': 2, 'sentences': 2},
        {'word': 'raa', 'documents': 1, 'sentences': 1}
    )
    actual = formatting.WordFrequencyShortFormFormatter(summary=longform_summary).format()
    assert actual == expected
