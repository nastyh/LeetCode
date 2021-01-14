from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def str2tree(self, s):  # O(n) both
        """
        Using stacks
        If a number is present in num, create a TreeNode and append to the stack
        If there is a closing bracket, in case of a number in a stack, it will be used to create a TreeNode.
        If the parent at the top of the stack has a left child, attach the node to the parent's left child.
        Otherwise, attach the node to the parent's right child
        If a number is not present in num, it means that the node at the top of the stack has already been assigned to its children
        Pop the node from the stack
        Check if the current topmost element of stack has a left child
        if true, attach the node to the left
        if false, attch the node to the right
        return top most element of the stack
        """
        num = ''
		stack = []
		for i in s:
			if i.isdigit() or i == '-': 
				num += i
			elif i=='(': 
				if num: 
					node = TreeNode(num)
					num=''
					stack.append(node)
			else:
				if num:
					node = TreeNode(num)
					num =''
					if stack[-1].left == None:
						stack[-1].left = node 
					elif stack[-1].right == None:
						stack[-1].right = node 
				else: 
					node = stack.pop()
					if stack[-1].left == None:
						stack[-1].left = node
					else:
						stack[-1].right = node
		return stack[-1] if stack else TreeNode(num) if s else None

    
    def str2tree_dict(self, s):
        """
        The depth of each node in the tree is equal to to it's depth inside the parenthesis.
        The expression is in a preorder format, meaning parent of current node at depth L, is the last node at depth L-1 prioritizing the left child.
        Pass on the expression and add every numerical value to our defaultdict object and update its parents when necessary.
        """
        if not s: return None
        tree = defaultdict(list)
        depth = 0
        cur=''
        for x in s:
            if x in'()':
                if cur:
                    node = TreeNode(cur,None,None)
                    if depth-1 in tree and tree[depth - 1]:
                        parent = tree[depth - 1][-1]
                        if not parent.left: parent.left = node
                        else: parent.right = node
                    tree[depth].append(node)
                depth += 1 if x=='(' else -1
                cur = ''
            else:
                cur=cur + x
        if cur: return TreeNode(cur)        
        return tree[0][0]