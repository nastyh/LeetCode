from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def findTarget(self, root, k):  # O(n) and O(n)
        """
        traverse, have a sorted list, use two pointers
        """
        nums = []
        def _trav(node):
            if not node: return
            _trav(node.left)
            nums.append(node.val)
            _trav(node.right)
        _trav(root)
        l, r = 0, len(nums) - 1
        while l < r:  # should be <, otherwise will fail on one- and two-element lists
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return False

    
    def findTarget_bfs(self, root, k):
        if not root: return False
        s = set()
        d = deque()
        d.append(root)
        while d:
            t = d.popleft()
            complement = k - t.val
            if complement in s:
                return True
            else:
                s.add(t.val)
            if t.left:
                d.append(t.left)
            if t.right:
                d.append(t.right)
        return False


if __name__ == '__main__':
    l = TreeNode(5)
    l.left = TreeNode(3)
    l.right = TreeNode(6)
    l.left.left = TreeNode(2)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(7)
    print(l.findTarget(l, 9))
    print(l.findTarget(l, 28))
    print(l.findTarget_bfs(l, 9))
    print(l.findTarget_bfs(l, 28))