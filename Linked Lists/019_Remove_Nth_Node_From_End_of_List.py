# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(head, n):
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


def removeNthFromEnd_pythonic(head, n):  # a bit cleaner
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        prev, curr = None, head
        for _ in range(l - n):
            prev = curr
            curr = curr.next 
        if prev == None:
            return head.next
        else:
            prev.next = curr.next
            curr.next = None
        return head   
