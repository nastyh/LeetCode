from collections import deque
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

    def printNewLine(self, root): # print values: every level in its own line
        if not root:
            print()
        q = deque()

        q.append(root)

        while q:
            for _ in range(len(q)):
                t = q.popleft()
                print(t.val, end = ' ') # key here is to include end so that it won't jump to the next line
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            print()


        t = binTree(4)
        t.insert(2)
        t.insert(7)
        t.printGlobal("PreOrder")



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Iterative implementations
    def preorder_iter(self, root): # pre-order iteratively
        if not root:
            return None
        res, s = [], []
        s.append(root)
        while s:
            t = s.pop()
            res.append(t.val)
            if t.right: # key here is to put to the stack in an opposite order. So that left comes last but gets popped first
                s.append(t.right)
            if t.left:
                s.append(t.left)
        return res

    def inorder_iter(self, root): # in order iteratively
        # if not root:
        #     return []
        res, s = [], []
        while s or root:
            if root:
                s.append(root)   # keep pushing nodes to Stack s while you can
                root = root.left # move left
            else:
                root = s.pop() # start taking out from the stack
                res.append(root.val) # save to res
                root = root.right # switch to the right side
        return res

    def postorder_iter(self, root):
        res, s = [], []
        s.append(root)
        while s:
            t = s.pop()
            res.insert(0, t.val)
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        return res


#   -----------------SAME THING WITH AND WITHOUT A HELPER FUNCTION--------------
    # def inorder_list(self, root):
    #     res = []
    #     if not root:
    #         return res
    #     res.append(root.val)
    #     return self.inorder_list(root.left) + res + self.inorder_list(root.right)

    def inorder_list(self, root):
        res = []

        def _helper(node, li):
            if not node:
                return
            _helper(node.left, li)
            li.append(node.val)
            _helper(node.right, li)
            return li

        return _helper(root, res)
#    ---------------------------------------------------------------------------

    def depth_bfs(self, root):
        if not root: return 0
        depth = 1
        d = deque()
        d.append([root, depth])
        while d:
            t, curr_d = d.popleft()
            if t.left or t.right:
                curr_d += 1
            if t.left:
                d.append([t.left, curr_d])
            if t.right:
                d.append([t.right, curr_d])
        return curr_d




l = TreeNode(7)
l.left = TreeNode(3)
l.right = TreeNode(11)
l.left.left = TreeNode(1)
l.right.left = TreeNode(2)
l.left.right = TreeNode(9)
l.right.right = TreeNode(14)

# print(l.inorder_iter(l))
# print(l.postorder_iter(l))
# print(l.postorder_iter(l))
# print(l.inorder_list(l))
print(l.depth_bfs(l))
