class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def swapNodes(self, head, k):  # O(n) but precisely: O(n + k). O(1)
        """
        Most optimal solution
        Have three pointers: l, slow, fast
        Move fast by k elements
        Then start moving both slow and fast simulten until fast reaches the end
        Slow will end up pointing to the node that is k elements from the end of the list
        Then move l to the right k times
        We need to swap a node at l with a node at slow
        """
        l = head
        slow, fast = head, head
        fast_countdown = k
        while fast_countdown != 1:
            fast = fast.next
            fast_countdown -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        l_countdown = k
        while l_countdown != 1:
            l = l.next
            l_countdown -= 1
        # temp = l.val
        # l.val = slow.val
        # slow.val = temp
        l.val, slow.val = slow.val, l.val
        return head