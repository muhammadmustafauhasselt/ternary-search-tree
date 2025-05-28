"""Tests for TernarySearchTree using pytest."""

import pytest
from src.ternary_search_tree import TernarySearchTree

# pylint: disable=redefined-outer-name

@pytest.fixture
def tst():
    """Fixture to create and populate a TernarySearchTree."""
    tree = TernarySearchTree()
    with open('data/insert_words.txt', encoding="utf-8") as f:
        for w in f:
            tree.insert(w.strip())
    return tree

@pytest.mark.parametrize(
    "word,expected",
    [(w.strip(), True) for w in open('data/insert_words.txt', encoding="utf-8")] +
    [(w.strip(), False) for w in open('data/not_insert_words.txt', encoding="utf-8")]
)
def test_search(tst, word, expected):
    """Test the search method for inserted and non-inserted words."""
    assert tst.search(word) is expected


