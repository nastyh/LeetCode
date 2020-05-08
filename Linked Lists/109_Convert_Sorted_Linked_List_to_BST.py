# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []     # first create a normal list from the linked list
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

# the list is sorted, the median element is the root. Everything to the left: left tree. Everything to the right: right tree

        def _treeBuild(l):
            if not l:
                return None
            m_ix = len(l) // 2
            node = TreeNode(l[m_ix])
            node.left = _treeBuild(l[:m_ix])
            node.right = _treeBuild(l[m_ix+1:])
            return node



        return _treeBuild(nums)

