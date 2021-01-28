# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

    # a bit easier to understand
    def deleteDuplicates_alt(self, head):  # O(n) and O(1)
        """
        Non-transparent thing here is when we find the same values and repoint pointers,
        we only move current. 
        And if the values are different, we move both pointers at the same time
        """
        if head == None:
            return head
        current = head.next
        prev = head
        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next  # move only current. Don't write prev = prev.next
            else:
                current = current.next
                prev = prev.next

        return head

