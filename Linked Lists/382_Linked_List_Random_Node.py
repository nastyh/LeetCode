# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Plain vanilla implementation: traverse the list, collect the values to the list,
    sample from the list
    """
    def __init__(self, head: ListNode):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        ix = int(random.random() * len(self.nums))
        return self.nums[ix]
    
class Solution_reservoir_sampling:
    def __init__(self, head):
        self.head = head
    
    def getRandom(self):
        ans = self.head.val
        node, n = self.head.next, 2
        while node:
            u = random.random()
            if u<1/n:
                ans = node.val
            node, n = node.next, n+1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()