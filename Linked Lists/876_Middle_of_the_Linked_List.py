# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def middleNode(self, head):
        if not head:
            return None

            def _length(node):
                l, curr = 0, node
                while curr:
                    curr = curr.next
                    l += 1
                return l

            total_l = _length(head)
            m_ix = total_l // 2 + 1
            curr, i = head, 1
            while i != m_ix:
                curr = curr.next
                i += 1
            return curr


    def middleNode_2_pointers(self, head):
        if not head: return None
        if head and not head.next: return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    def middleNode_recur(head):
        def _helper(head, curr):
            if head:
                total, node = _helper(head.next, curr + 1)
                return total, node if total // 2 != curr else head
            return curr, None
        return _helper(head, 0)[1]




