Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def partition(self, head, x):  # O(n) and O(1)
        """
        Two dummy nodes to find all nodes with values < x and all nodes with values > x
        It's done in the while loop 
        Then we need to connect two lists somehow
        We have two helper pointers for this. 
        Once two lists are built, we point pre.next to the start of the post list. To track the start of the post list, we have post_helper
        """
        pre, post = ListNode(-1), ListNode(-1)
        pre_helper, post_helper = pre, post
        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                post.next = head
                post = post.next
            head = head.next
        pre.next = post_helper.next
        post.next = None  # need to do it otherwise it might be pointing to anything (like to the node in the pre list)
        return pre_helper.next 