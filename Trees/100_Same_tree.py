from collections import deque
# Definition for a binary tree node.
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p and q: return False
        if p and not q: return False
        if p.val != q.val:
            return False   
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    
    def isSameTree_iter(self, p, q):
        stack = [(p, q)]
        while stack:
            first, second = stack.pop()
            if not first and not second: pass
            elif not first or not second: return False
            else:
                if first.val != second.val: return False
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        return True
        

if __name__ == '__main__':
    a = Tree(1)
    a.left = Tree(2)
    a.right = Tree(3)
    b = Tree(1)
    b.left = Tree(2)
    b.right = Tree(3)
    c = Tree(1)
    c.left = Tree(2)
    c.right = Tree(3)
    d = Tree(1)
    d.left = Tree(2)
    d.right = Tree(6)
    # print(a.isSameTree(a, b))
    # print(a.isSameTree(c, d))
    print(a.isSameTree_iter(a, b))
    print(a.isSameTree_iter(c, d))


