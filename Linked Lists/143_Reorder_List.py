# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reorderList(self, head: ListNode) -> None:
        """
        Find the middle, reverse the second part, merge two lists 
        """
        def _rev(node): # reversing the linked List; helper function
            prev, curr = None, node
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev
        def _merge(l1, l2):
            while l1:
                l1_next = l1.next
                l2_next = l2.next
                l1.next = l2
                if not l1.next:
                    break
                l2.next = l1.next
                l1 = l1.next
                l2 = l2.next
        # cut the list in the middle into two, reverse the second one, the first element of the first points to the first element of the second, it points to the second element of the first, etc.
        if not head or not head.next:
            return
        l1 = head
        slow, fast = head, head
        prev = None
        while fast and slow:
            prev = slow  # at the end, prev will keep the last element of the first list
            fast = fast.next.next
            slow = slow.next
        prev.next = None # splitting the list into two parts
        # now l1 keeps the head of the first list
        # prev.next keeps the end of the first list
        # slow keeps the head of the second list
        # fast keeps the end of the second list
        l2 = _rev(slow)
        _merge(l1, l2)
