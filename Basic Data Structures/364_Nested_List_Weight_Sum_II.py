import math
from collections import deque
def depthSumInverse_bfs(nestedList):  # O(n) both
    """
    max depth is the number of the closing brackets at the end of nestedList
    Works generally, doesn't work for the LeetCode implementation
    """
    max_depth = 0
    d, res = deque(), 0
    for ch in str(nestedList)[::-1]:
        if ch == ']':
            max_depth += 1
        else:
            break
    for element in nestedList:
        d.append((element, max_depth))
    while d:
        t, depth = d.popleft()
        if isinstance(t, int):
            res += t * depth
        else:
            for other in t:
                d.append((other, depth - 1))
    return res


def depthSumInverse(nestedList):
    max_d = -math.inf
    def _helper(curr, numofList, depth):
        nonlocal max_d
        max_d = max(max_d, depth)
        for obj in curr:
            if isinstance(obj, int):
                numofList.append((depth, obj))
                continue
            _helper(obj, numofList, depth + 1)
    numofList = []
    _helper(nestedList, numofList, 1)
    res = 0
    for depth, num in numofList:
        res += (max_d - depth + 1) * num
    return res


def depthSum_bfs_leetcode(nestedList):
    dic = {}
    level = 0
    q = collections.deque()
    q.append(nestedList)
    res = 0
    while q:
        size = len(q)
        level += 1
        sums = 0
        for _ in range(size):
            nl = q.popleft()
            for n in nl:
                if n.isInteger():
                    sums += n.getInteger()
                else:
                    q.append(n.getList())
        dic[level] = sums
    for k, v in dic.items():
        res += (level + 1 - k) * v
    return res


if __name__ == '__main__':
    print(depthSumInverse([[1, 1], 2, [1, 1]]))
    print(depthSumInverse_bfs([[1, 1], 2, [1, 1]]))
    print(depthSumInverse_bfs([1, [4, [6]]]))
