def pathSum(nums):  # O(n) and O(n)
    ans = 0
    root = Node(nums[0] % 10)

    def dfs(node, running_sum = 0):
        if not node: return
        running_sum += node.val
        if not node.left and not node.right:
            self.ans += running_sum
        else:
            dfs(node.left, running_sum)
            dfs(node.right, running_sum)

    for x in nums[1:]:
        depth, pos, val = x / 100, x / 10 % 10, x % 10
        pos -= 1
        cur = root
        for d in xrange(depth - 2, -1, -1):
            if pos < 2**d:
                cur.left = cur = cur.left or Node(val)
            else:
                cur.right = cur = cur.right or Node(val)

            pos %= 2**d

    dfs(root)
    return ans


def pathSum_alt(nums):
    ans = 0
    values = {x / 10: x % 10 for x in nums}
    def dfs(node, running_sum = 0):
        if node not in values: return
        running_sum += values[node]
        depth, pos = divmod(node, 10)
        left = (depth + 1) * 10 + 2 * pos - 1
        right = left + 1
        if left not in values and right not in values:
            self.ans += running_sum
        else:
            dfs(left, running_sum)
            dfs(right, running_sum)
    dfs(nums[0] / 10)
    return ans