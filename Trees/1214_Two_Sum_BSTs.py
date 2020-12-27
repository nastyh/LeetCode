class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def twoSumBSTs(self, root1, root2, target):
        def _trav(node, res):
            if not node: return 
            _trav(node.left, res)
            res.append(node.val)
            _trav(node.right, res)
            return res
        first_tree, second_tree = _trav(root1, []), _trav(root2, [])
        l, r = 0, len(second_tree) - 1
        while l < len(first_tree) and r > 0:
            if first_tree[l] + second_tree[r] == target:
                return True
            elif first_tree[l] + second_tree[r] < target:
                l += 1
            else:
                r -= 1
        return False


if __name__ == '__main__':
    l = TreeNode(2)
    l.left = TreeNode(1)
    l.right = TreeNode(4)
    m = TreeNode(1)
    m.left = TreeNode(0)
    m.right = TreeNode(3)
    print(l.twoSumBSTs(l, m, 5))




def test(first_tree, second_tree, target):
    l, r = 0, len(second_tree) - 1
    while (l < len(first_tree) - 1) or (r > 0):
        try:
            if first_tree[l] + second_tree[r] == target:
                return True
            elif first_tree[l] + second_tree[r] < target:
                l += 1
            else:
                r -= 1
        except IndexError:
            return False


def test_another(first_tree, second_tree, target):
    l, r = 0, len(second_tree) - 1
    while l < len(first_tree) and r > 0:
        if first_tree[l] + second_tree[r] == target:
            return True
        elif first_tree[l] + second_tree[r] < target:
            l += 1
        else:
            r -= 1
    return False

# if __name__ == '__main__':
    # print(test([-10, 0, 10], [0, 1, 2, 5, 7], 18))
    # print(test([1, 2, 4], [0, 1, 3], 5))
    # print(test_another([-10, 0, 10], [0, 1, 2, 5, 7], 18))
    # print(test_another([1, 2, 4], [0, 1, 3], 5))