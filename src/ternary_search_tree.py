"""
Ternary Search Tree (TST) for academic testing.
- tst.search(prefix) returns True for all prefixes and full words.
- tst.search(prefix, exact=True) returns True for fully-inserted words only.
- len(tst) only counts the fully-inserted words, not the prefixes.
- tst.search('') returns True if exact=False, False if exact=True.
"""

class TSTNode:
    def __init__(self, char: str):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False
        self.is_prefix = False

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word: str):
        if not isinstance(word, str) or not word:
            return
        for i in range(1, len(word)+1):
            self._insert_prefix(word[:i], is_full_word=(i == len(word)))

    def _insert_prefix(self, word: str, is_full_word: bool):
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
        def _count(node):
            if node is None:
                return 0
            count = _count(node.left) + _count(node.eq) + _count(node.right)
            if node.is_end:
                count += 1
            return count
        return _count(self.root)

    def __contains__(self, word):
        return self.search(word, exact=True)

    def __iter__(self):
        def _traverse(node, prefix):
            if node is not None:
                yield from _traverse(node.left, prefix)
                new_prefix = prefix + node.char
                if node.is_end:
                    yield new_prefix
                yield from _traverse(node.eq, new_prefix)
                yield from _traverse(node.right, prefix)
        yield from _traverse(self.root, "")

    def all_strings(self):
        return list(self.__iter__())

    def delete(self, word: str) -> bool:
        if not isinstance(word, str) or not word:
            return False

        def _delete(node, word, idx):
            if node is None:
                return None, False
            c = word[idx]
            if c < node.char:
                node.left, deleted = _delete(node.left, word, idx)
            elif c > node.char:
                node.right, deleted = _delete(node.right, word, idx)
            else:
                if idx + 1 == len(word):
                    if node.is_end:
                        node.is_end = False
                        return node, True
                    else:
                        return node, False
                else:
                    node.eq, deleted = _delete(node.eq, word, idx + 1)
            return node, deleted

        self.root, deleted = _delete(self.root, word, 0)
        return deleted
