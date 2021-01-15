from collections import deque
def depthSum(nestedList):  # plain vanilla implementation from scratch, O(n) both
    if len(nestedList) == 0: return 0
    res = 0
    def _helper(nestedList, depth):
        nonlocal res
        for item in nestedList:
            if isinstance(item, int):
                res += item * depth
            else:
                _helper(item, depth + 1)
    _helper(nestedList, 1)
    return res


def depthSum_bfs(nestedList):  # BFS from scratch, O(n) both
    if len(nestedList) == 0: return 0
    d = deque()
    res = 0
    for element in nestedList:
        d.append((element, 1))
    while d:
        t, depth = d.popleft()
        if isinstance(t, int):
            res += t * depth
        else:
            for smaller_element in t:
                d.append((smaller_element, depth + 1))
    return res


def depthSum_leetcode(nestedList):  # using Leetcode's implementation
    def dfs(nestedList, depth):
        total = 0
        for element in nestedList:
            if element.isInteger():
                total += (element.getInteger() * depth)
            else:
                total += dfs(element.getList(), depth + 1)
        return total
    return dfs(nestedList, 1)


def depthSum_bfs_leetcode(nestedList):
    res = 0
    d = deque([])
    for x in nestedList:
        d.append((x, 1))
    while d: 
        item, level = d.popleft()
        if item.isInteger():
            res += item.getInteger() * level
        else:
            for val in item.getList():
                stack.append((val, level + 1))
    return res
        

if __name__ == '__main__':
    print(depthSum([[1, 1], 2,[1, 1]]))
    print(depthSum_bfs([[1, 1], 2,[1, 1]]))
    print(depthSum_bfs([1, [4, [6]]]))
    print(depthSum_bfs([0]))