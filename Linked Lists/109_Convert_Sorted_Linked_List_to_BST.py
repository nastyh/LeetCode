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

    def sortedListToBST(self, head):  # O(N) both
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


    def sortedListToBST_another(self, head):  # O(NlogN) and O(logN)
        """
        Slow and fast pointer technique.
        We pass a list and need to find its middle. Every time  the list's length is cut in 2. 
        A recursion stack creates O(logN) space complexity. 
        """
        def _middle(head):
            prev, slow, fast = None, head, head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next 
            prev.next = None
            return slow
        if not head: return None
        if not head.next: return TreeNode(head.val)
        mid = _middle(head)
        res = TreeNode(mid.val) 
        res.left = self.sortedListToBST_another(head)
        res.right = self.sortedListToBST_another(mid.next)
        return res