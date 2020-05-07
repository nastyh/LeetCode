# BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binTree:
    def __init__(self, value):
        self.root = Node(value)


    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)

    def printGlobal(self, strategy):
        print("Printing in this way: {}".format(strategy), sep="\n", end="\n")
        if strategy == "InOrder":
            self._printInOrder(self.root)
        if strategy == "PreOrder":
            self._printPreOrder(self.root)
        if strategy == "PostOrder":
            self._printPostOrder(self.root)

    def printInOrder(self): # wrapper function
        self._printInOrder(self.root)

    def _printInOrder(self, root): # helper function: left, root, right
        if root:
            self._printInOrder(root.left)
            print(root.value, end="->", sep='\n')
            self._printInOrder(root.right)

    def _printPreOrder(self, root): # helper function: root, left, right
        if root:
            print(root.value, end="->", sep='\n')
            self._printPreOrder(root.left)
            self._printPreOrder(root.right)

    def _printPostOrder(self, root): # helper function: left, right, root
        if root:
            self._printPostOrder(root.left)
            self._printPostOrder(root.right)
            print(root.value, end="->", sep='\n')


t = binTree(4)
t.insert(2)
t.insert(7)
t.printGlobal("PreOrder")
