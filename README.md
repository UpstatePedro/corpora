# corpora

> Summarise text in a collection of docs by finding the most common words

## Getting started

### Python Virtual Environment

This project is tested against Python 3.9. Other versions may work, but this is not guaranteed.

This project uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage python dependencies and create reproducible 
environments. The instructions below assume you have installed pipenv in your local environment.

To install the virtual environment, please run (from the project root):

`$ pipenv install`

Once pipenv has created / updated the virtual env dependencies, please run the command below:

`$ pipenv run download-nltk-extras`

This will download some additional resources that NLTK will use to remove common stop-words from the results.

## Usage

For now, this project provides only a CLI to analyse a local directory containing text files. We expect a flat directory
structure containing only `.txt` files. eg:

```
- target directory
    - example_1.txt
    - example_2.txt
    - example_3.txt
```

#### CLI

The best way to get started with the CLI is to pull up its docs in the terminal:

`$ python corpora_cli.py --help`

### Typical usage

`$ python corpora_cli.py --target_dir ~/path/to/some/text/`

`--limit n` will limit the number of words included in the results to 'n'
`--format shortform` request different formatting of the output. At present, `shortform` is the only option, and is probably a good place to get started.
`--normalise_case` include this if you wish to treat words with the same spelling, but different capitalisation, as a single word

```bash
# Output when providing the `--format shortform` option:
[
  {"word": "Word one", "documents": 6, "sentences": 131},
  {"word": "Word two", "documents": 6, "sentences": 180},
]
```

## Extensions: what would I do with more time?

1. Consider more efficient solutions to the in-memory approach
1. Accommodate larger corpora that do not fit into memory
1. Dockerise the project to enable faster startup for new users
1. Enable users to apply stemming to account for different forms of the same 'base' being used
1. Provide more options for output formatting (eg. output to csv, json etc.)
