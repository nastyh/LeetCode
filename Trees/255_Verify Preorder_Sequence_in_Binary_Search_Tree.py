import math
def verifyPreorder(preorder):  # O(n) and O(n)
    chk, stack = None, []
    for n in preorder:
        while stack and n > stack[-1]:
            chk = stack.pop()
        if chk != None and n < chk:
            return False
        stack.append(n)
    return True

def verifyPreorder_const_space(preorder):  # O(n) and O(1)
    """
    preorder array can be reused as the stack thus achieve O(1) extra space, since the scanned items of preorder array is always more than or equal to the length of the stack.
    """
    lower = -math.inf
    i = 0
    for x in preorder:
        if x < lower:
            return False
        while i > 0 and x > preorder[i - 1]:
            lower = preorder[i - 1]
            i -= 1
        preorder[i] = x
        i += 1
    return True