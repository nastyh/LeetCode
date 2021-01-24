# Merge two sorted lists
# 1->2->3 and 2->3->4 become 1->2->2->3->3->4

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def mergeLinkedLists(self, l1: Node, l2: Node):  # O(MN) both, where MN are the lenghts of the respective linked lists
        curr = Node(-1)
        res = curr
        if not l1 and not l2: # edge cases
            return None
        if l1 and not l2:
            return l1
        if not l1 and l2:
            return l2
        while l1 and l2:
            if l1.value <= l2.value:
                curr.next = l1.value  # -1 -> l1.value
                l1 = l1.next
            else:
                curr.next = l2.value # -1 -> l2.value
                l2 = l2.next
            curr = curr.next

            if l1:
                curr.next = l1
            else:
                curr.next = l2
        return res.next # because we don't want to return -1
