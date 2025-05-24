import time
import random
import string
from tst import TernarySearchTree  # adjust if your class file is differently named

def generate_words(n, length=6):
    return [''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(n)]

def benchmark(tree, words):
    print(f"Benchmarking {len(words)} words")
    start_insert = time.time()
    for word in words:
        tree.insert(word)
    insert_time = time.time() - start_insert

    start_search = time.time()
    for word in words:
        tree.search(word)
    search_time = time.time() - start_search

    print(f"Insert Time: {insert_time:.4f} seconds")
    print(f"Search Time: {search_time:.4f} seconds")

if __name__ == "__main__":
    words = generate_words(100000)  # test with 100,000 random words
    tree = TernarySearchTree()
    benchmark(tree, words)
