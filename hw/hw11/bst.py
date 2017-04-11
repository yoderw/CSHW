class BSTNode:

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right=right

class BST:

    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            prev = None
            curr = self.root
            while curr:
                if key < curr.key:
                    prev = curr
                    curr = curr.left
                elif key > curr.key:
                    prev = curr
                    curr = curr.right
                else:
                    curr.value = value
                    return None
            new = BSTNode(key, value)
            if key < prev.key:
                prev.left = new
            else:
                prev.right = new

    def __getitem__(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            elif key == curr.key:
                return curr.value
        return None

    def __len__(self):
        def length(self, node):
            if node is None:
                return 0
            else:
                return 1 + length(node.left) + length(node.right)
        return length(self.root)
