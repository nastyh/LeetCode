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




