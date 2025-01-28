# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(n^2) traverse the sorted portion and insert, both take n
        O(1) nothing extra 
        
        dummy node is used to simplify insertion at the head of the list
        For each node, check if it is already in the correct position relative to its next node.
        If not, extract the node and find its correct position in the sorted part of the list (starting from the dummy node).
        Use a pointer (prev) to locate the correct position in the sorted list.
        Insert the node at the correct position by adjusting pointers.

        """
        if not head or not head.next: # edge
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = head
        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                to_insert = curr.next
                curr.next = to_insert.next

                prev = dummy
                while prev.next and prev.next.val < to_insert.val:
                    prev = prev.next
                
                to_insert.next = prev.next
                prev.next = to_insert 
        return dummy.next
