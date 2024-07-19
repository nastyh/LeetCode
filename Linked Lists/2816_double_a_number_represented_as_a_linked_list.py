# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt_brute_force(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(n) both
        brute force
        traverse and save everything to the list 
        Go over the list and multiply by 2 and do all the
        necessary stuff with remainders 
        Build a linked list
        It will be in the reversed order so reverse using a helper function
        """
        def _helper(n):
            prev, curr = None, n
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev

        traversed = []
        while head:
            traversed.append(head.val)
            head = head.next
        print(f"values of traversed_list is f{traversed}")
        res = ListNode(-1)
        dummy = res
        carry = 0
        for e in reversed(traversed): 
            curr_el = e * 2
            to_append = (curr_el + carry) % 10
            carry = (curr_el + carry) // 10 
            res.next = ListNode(to_append)
            res = res.next
        if carry:
            res.next = ListNode(1)
        return _helper(dummy.next)

    def doubleIt_brute_optimized(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr, prev = head, dummy
        while curr:
            double = 2 * curr.val
            if double < 10:
                curr.val = double
            else:
                curr.val = double % 10
                prev.val += 1
            prev = curr
            curr = curr.next

        return dummy if dummy.val else dummy.next