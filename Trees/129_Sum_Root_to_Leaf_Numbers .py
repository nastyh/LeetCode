# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sumNumbers(self, root):  # O(n) both
        ans = 0
        res = []
        def _helper(root, paths):
            if not root: return []
            if not root.left and not root.right:
                res.append(paths)
            else:
                if root.left: _helper(root.left, paths + [root.left.val])
                if root.right: _helper(root.right, paths + [root.right.val])
            return res

        vals = _helper(root, [root.val]) if root else None
        if vals:
            for l in vals:
                curr_val = int(''.join([str(i) for i in l]))
                ans += curr_val
        return ans
        # alternative that is slightly more Pythonic
        # if vals:
        #     for element in vals:
        #         ans += sum([v * 10 ** k for k, v in enumerate(list(reversed(element)))])
        # return ans

    def sumNumbers_comprehension(self, root):  # takes O(n) space. Create a list of lists, enumerate and iterate calculating the total sum
        res = []

        def _helper(root, paths):
            if not root: return []
            if root and not root.left and not root.right:
                res.append(paths)
            else:
                if root.left: _helper(root.left, paths + [root.left.val])
                if root.right: _helper(root.right, paths + [root.right.val])
            return res
        digits = _helper(root, [root.val]) if root else None
        s = []
        if digits:
            for element in digits:
                s.append(sum([v * 10 ** k for k, v in enumerate(list(reversed(element)))]))    
        return sum(s)

    
    def sumNumbers_stack(self, root):
        res = 0
        stack = [(root, 0) ]
        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if not root.left and not root.right:
                    res += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))        
        return res


    def sumNumbers_BFS(self, root):
        if not root: return
        q, res = [], 0
        q.append((root, 0))
        while q:
            t, curr_num = q.pop()
            curr_num = curr_num * 10 + t.val
            if not t.left and not t.right:
                res += curr_num
            if t.left:
                q.append((t.left, curr_num))
            if t.right:
                q.append((t.right, curr_num))
        return res

    
    def sumNumbers_Morris_Preorder(self, root):  #  O(n) and O(1)
        root_to_leaf = curr_number = 0
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right 
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right            
        return root_to_leaf


    def sumNumbers_DFS(self, root):  #  O(N), O(h)
        if not root: return 0
        def _helper(root, cum_sum):
            cum_sum = cum_sum * 10 + root.val
            if root and not root.left and not root.right:
                return cum_sum              
            else:
                return _helper(root.left, cum_sum) + _helper(root.right, cum_sum)
        return _helper(root, 0)


    def sumNumbers_DFS_another(self, root):   #  O(N), O(h)
        if not root: return 0
        def _helper(root, cum_sum):
            if not root: return cum_sum
            cum_sum = cum_sum * 10 + root.val
            if root and not root.left and not root.right:
                return cum_sum
            if root.left: l = _helper(root.left, cum_sum)
            if root.right: r = _helper(root.right, cum_sum)
            return l + r
        return _helper(root, 0)

    
    def sumNumbers_global(self, root):  # another DFS, this time with a global variable O(N), O(h)
        if not root: return 0
        if root and not root.left and not root.right: return root.val
        res = 0
        def _helper(root, curr_path_val):
            nonlocal res
            if not root: return
            if root and not root.left and not root.right:
                res += curr_path_val
            if root.left: _helper(root.left, curr_path_val * 10 + root.left.val)
            if root.right: _helper(root.right, curr_path_val * 10 + root.right.val)
        _helper(root, root.val)
        return res       


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(9)
    l.right = TreeNode(0)
    l.left.left = TreeNode(5)
    l.left.right = TreeNode(1)
    print(l.sumNumbers(l))
    print(l.sumNumbers_comprehension(l))
    print(l.sumNumbers_BFS(l))
    print(l.sumNumbers_DFS(l))
    print(l.sumNumbers_DFS_another(l))
    print(l.sumNumbers_global(l))
    m = TreeNode(1)
    m.left = TreeNode(2)
    m.right = TreeNode(3)
    # print(m.sumNumbers(m))
