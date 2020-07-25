# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ix = 0
        curr = head
        while curr:
            curr = curr.next
            ix +=1
        k = ix - n

        prev, curr = None, head
        while k !=0:
            prev = curr
            curr = curr.next # current points to the element that we need to remove
            k -=1

        if prev == None: # means we're removing the first element in the list
            return head.next
        else:
            prev.next = curr.next
            curr.next= None
        return head

