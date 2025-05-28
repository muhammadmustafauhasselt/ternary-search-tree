"""
Ternary Search Tree (TST) for academic testing.
- tst.search(prefix) returns True for all prefixes and full words.
- tst.search(prefix, exact=True) returns True for fully-inserted words only.
- len(tst) only counts the fully-inserted words, not the prefixes.
- tst.search('') returns True if exact=False, False if exact=True.
"""

class TSTNode:
    """Node of a Ternary Search Tree."""

    def __init__(self, char: str):
        """Initialize the node with a character."""
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False
        self.is_prefix = False

class TernarySearchTree:
    """Ternary Search Tree implementation."""

    def __init__(self):
        """Initialize an empty Ternary Search Tree."""
        self.root = None

    def insert(self, word: str):
        """Insert a word into the TST."""
        if not isinstance(word, str) or not word:
            return
        for i in range(1, len(word) + 1):
            self._insert_prefix(word[:i], is_full_word = (i == len(word)))

    def _insert_prefix(self, word: str, is_full_word: bool):
        """Insert a prefix into the TST."""
        def _insert(node, word, idx):
            c = word[idx]
            if node is None:
                node = TSTNode(c)
            if c < node.char:
                node.left = _insert(node.left, word, idx)
            elif c > node.char:
                node.right = _insert(node.right, word, idx)
            else:
                if idx + 1 < len(word):
                    node.is_prefix = True
                    node.eq = _insert(node.eq, word, idx + 1)
                else:
                    if is_full_word:
                        node.is_end = True
                    node.is_prefix = True
            return node
        self.root = _insert(self.root, word, 0)

    def search(self, word: str, exact: bool = False) -> bool:
        """
        Search for a word or prefix in the TST.
        If exact is True, only return True for fully inserted words.
        If exact is False (default), return True for any word or prefix.
        For '' (empty string), returns:
          - True if exact=False
          - False if exact=True
        """
        if word == '':
            return not exact

        if not isinstance(word, str) or not word:
            return False

        def _search(node, word, idx):
            if node is None:
                return False
            c = word[idx]
            if c < node.char:
                return _search(node.left, word, idx)
            elif c > node.char:
                return _search(node.right, word, idx)
            else:
                if idx + 1 == len(word):
                    return node.is_end if exact else (node.is_end or node.is_prefix)
                return _search(node.eq, word, idx + 1)
        return _search(self.root, word, 0)

    def __len__(self):
        """Return the number of full words stored in the TST."""
        def _count(node):
            if node is None:
                return 0
            count = _count(node.left) + _count(node.eq) + _count(node.right)
            if node.is_end:
                count += 1
            return count
        return _count(self.root)

    def __contains__(self, word):
        """Check if a word is in the TST (exact match)."""
        return self.search(word, exact=True)

    def __iter__(self):
        ""
