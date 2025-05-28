"""
Benchmark.py
"""

import time
from src.ternary_search_tree import TernarySearchTree
from src.b_tree import BTree

# pylint: disable=redefined-outer-name

def load_words(filename, limit=None):
    """Load words from a file, optionally limiting the count."""
    with open(filename, encoding="utf-8") as f:
        words = [w.strip() for w in f if w.strip()]
    return words if limit is None else words[:limit]

def benchmark(tree, words, structure_name="TST"):
    """Benchmark insertion and search operations for the given tree."""
    print(f"\nBenchmarking {structure_name} with {len(words)} words")
    start_insert = time.time()
    for word in words:
        tree.insert(word)
    insert_time = time.time() - start_insert

    start_search = time.time()
    found = sum(tree.search(word) for word in words)
    search_time = time.time() - start_search

    print(f"Insert Time: {insert_time:.4f} seconds")
    print(f"Search Time: {search_time:.4f} seconds")
    print(f"Found {found}/{len(words)} words.")

if __name__ == "__main__":
    words = load_words("data/corncob_lowercase.txt")
    tst = TernarySearchTree()
    benchmark(tst, words, "TST")
    btree = BTree(t=10)
    benchmark(btree, words, "B-Tree")
