import pytest
from src.ternary_search_tree import TernarySearchTree

@pytest.fixture
def tst():
    tree = TernarySearchTree()
    with open('data/insert_words.txt') as f:
        for w in f:
            tree.insert(w.strip())
    return tree

@pytest.mark.parametrize("word,expected", 
    [(w.strip(), True) for w in open('data/insert_words.txt')] +
    [(w.strip(), False) for w in open('data/not_insert_words.txt')]
)
def test_search(tst, word, expected):
    assert tst.search(word) is expected