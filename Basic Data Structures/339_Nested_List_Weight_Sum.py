def depthSum(nestedList):  # plain vanilla implementation from scratch
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


if __name__ == '__main__':
    print(depthSum([[1, 1], 2,[1, 1]]))