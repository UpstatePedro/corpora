"""
Test to get the CI/CD pipelines started before beginning development
"""
from src import cicd


def test_for_cicd():
    assert 1.5 == cicd.return_something(1.5)


def test_two():
    assert 2.0 == cicd.return_something(2.0)
