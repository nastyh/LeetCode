from collections import deque
class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

    def visible_nodes(root):
    # Just count the number of levels
    if not root: return 0
    if root and not root.left and not root.right:
        return 1
    d = deque()
    d.append((root, 1))
    while d:
        t, curr_level = d.popleft()
        if t.left or t.right:
            curr_level += 1
        if t.left:
            d.append((t.left, curr_level))
        if t.right:
            d.append((t.right, curr_level))
    return curr_level
        