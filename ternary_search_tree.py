"""
Ternary Search Tree (TST) implementation.
"""

class TSTNode:
    def __init__(self, char: str):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word: str):
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
                    node.eq = _insert(node.eq, word, idx + 1)
                else:
                    node.is_end = True
            return node

        if word:
            self.root = _insert(self.root, word, 0)

    def search(self, word: str) -> bool:
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
                    return node.is_end
                return _search(node.eq, word, idx + 1)
        return bool(word) and _search(self.root, word, 0)