# src/b_tree.py

"""B-Tree implementation module."""

class BTreeNode:
    """Node of a B-Tree."""

    def __init__(self, t, leaf=False):
        """Initialize a BTreeNode."""
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf
        self.keys = []
        self.children = []

    def insert_non_full(self, key):
        """Insert a key into a non-full node."""
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        """Split the child of this node at index i."""
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t-1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

    def search(self, key):
        """Search for a key in the subtree rooted at this node."""
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and key == self.keys[i]:
            return True
        if self.leaf:
            return False
        return self.children[i].search(key)

class BTree:
    """B-Tree data structure."""

    def __init__(self, t=10):
        """Initialize a B-Tree."""
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        """Insert a key into the B-Tree."""
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, False)
            s.children.append(r)
            s.split_child(0)
            self.root = s
            s.insert_non_full(key)
        else:
            r.insert_non_full(key)

    def search(self, key):
        """Search for a key in the B-Tree."""
        return self.root.search(key)
