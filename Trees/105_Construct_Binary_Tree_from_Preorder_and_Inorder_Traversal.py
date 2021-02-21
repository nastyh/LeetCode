# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def buildTree(self, preorder, inorder):  # O(N) and O(N)
        if len(inorder) == 0:
            return None
        root_val = preorder.pop(0)
        inorder_ix_of_root = inorder.index(root_val)
        l = self.buildTree(preorder, inorder[:inorder_ix_of_root])
        r = self.buildTree(preorder, inorder[inorder_ix_of_root + 1:])
        res = TreeNode(root_val)
        res.left = l
        res.right = r
        return res


    def buildTree_Iter(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not len(preorder) or not len(inorder):
        return None
    root = TreeNode()
    #create a hash table of indexes and use it instead of array for faster access
    inorder_index = {inorder[i]:i for i in range(0, len(inorder))}
    #a stack of nodes and its corresponding ranges
    nodes = [[root, 0, len(preorder) - 1]]

    for i in range(len(preorder)):
        curr_node, l, h = nodes.pop()
        curr_node.val = preorder[i]
        #find the index of the node in inorder, then use the divide and conquere technique
        mid = inorder_index[curr_node.val]

        if mid < h:
            curr_node.right = TreeNode()
            #appent the right subtree first, as stack follows LIFO approach
            nodes.append([curr_node.right, mid + 1, h])
        if l < mid:
            curr_node.left = TreeNode()
            #this will be popped before the right subtree
            nodes.append([curr_node.left, l, mid - 1])
    return root

    def buildTree_iter_another(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)

        pre = 1
        ino = 0
        while (pre < len(preorder)):
            curr = TreeNode(preorder[pre])
            pre += 1
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino += 1
            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr

            stack.append(curr)
        return root

