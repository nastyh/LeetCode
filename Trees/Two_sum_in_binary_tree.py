from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def twoSum(self, root, target):  # BFS
        if not root: return (None, None)
        q = deque([root])
        prevLvl = {} 
        while q:
            lvl = []
            while q:
                lvl.append(q.popleft())
            for cur in lvl:
                prev = target - cur.val
                if prev in prevLvl:
                    return (prevLvl[prev].val, cur.val)
            for cur in lvl: 
                prevLvl[cur.val] = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return (None, None)


    def twoSum_alt(self, root, k):  # BFS as well
        d = defaultdict(list) # node.val -> level
        def diff_levels(i, j):
            return not (len(d[i]) == len(d[j]) == 1 and d[i] == d[j])
        q = deque()
        q.append((root, 0))
        level = 0
        while q:
            for _ in range(len(q)):
                t, l = q.popleft()
                d[t.val].append(l)
                if t.left:
                    q.append((t.left, l + 1))
                if t.right:
                    q.append((t.right, l + 1))
        for i in d:
            j = k - i
            if j in d and diff_levels(i, j):
                return [i, j]
        return []


if __name__ == '__main__':
    l = TreeNode(17)
    l.left = TreeNode(21)
    l.right = TreeNode(13)
    l.left.left = TreeNode(1)
    l.left.left.right = TreeNode(3)
    l.right.left = TreeNode(10)
    l.right.right = TreeNode(5)
    print(l.twoSum(l, 8))
    print(l.twoSum_alt(l, 8))