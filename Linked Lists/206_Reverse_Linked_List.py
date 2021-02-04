# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head

        cur = head
        prev = None

        while cur:
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        return prev

#     def reverseList(self, head: ListNode) -> ListNode: # iteratively
#         if head is None: #edge cases
#             return None
#         if head.next is None:
#             return head

#         s = []
#         while head:
#             s.append(head)
#             head = head.next

#         res = ListNode(-1)
#         head = res
#         while s:
#             curr = s.pop()
#             head.next = ListNode(curr.val)
#             head = head.next
#         return res.next

    def reverseList(self, head): # recursively
        if head is None: #edge cases11
            return None
        if head.next is None: # base case
            return head
        orig_head = self.reverseList(head.next) # keeps the last element now, i.e. 5
        head.next.next = head
        head.next = None
        return orig_head
