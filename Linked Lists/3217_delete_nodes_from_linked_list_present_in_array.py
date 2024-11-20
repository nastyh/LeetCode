# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(n) both
        set for faster checks
        res is needed to be able to return the final result since res.next points to the head
        look at the values of curr. If the value in the set, need to skip this node. 
        Do it by pointing prev.next to what is after curr (curr.next)
        Else: move the whole construct to the right by making prev = curr
        In any case curr=curr.next needs for the loop going forward 
        """
        if not head: return None
        s = set(nums)
        res = ListNode(-1)
        res.next = head
        prev, curr = res, head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return res.next