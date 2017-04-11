class BSTNode:

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:

    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        new = BSTNode(key, value)
        if self.root is None:
            self.root = new
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
            else:
                return curr.value

    def __len__(self):
        def length(node):
            if node is None:
                return 0
            else:
                return 1 + length(node.left) + length(node.right)
        return length(self.root)

    def asList(self):
        def ls(node):
            if node is None:
                return []
            else:
                return ls(node.left) + [[node.key, node.value]] + ls(node.right)
        return ls(self.root)

    def __str__(self):
        print("{", end="")
        curr = self.root
        def printer(node):
            if node is None:
                print("", end="")
            else:
                printer(node.left)
                if node is self.root:
                    print(str(node.key) + ": " + str(node.value), end="")
                else:
                    print(", " + str(node.key) + ": " + str(node.value), end="")
                printer(node.right)
        printer(self.root)
        print("}")
