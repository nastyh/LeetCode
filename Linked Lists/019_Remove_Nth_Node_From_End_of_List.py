# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None=

    def removeNthFromEnd(self, head, n):
        ix = 0
        curr = head
        while curr:
            curr = curr.next
            ix += 1
        k = ix - n

        prev, curr = None, head
        while k != 0:
            prev = curr
            curr = curr.next # current points to the element that we need to remove
            k -= 1

        if prev == None: # means we're removing the first element in the list
            return head.next
        else:
            prev.next = curr.next
            curr.next= None
        return head

    
    def removeNthFromEnd_one_pass(self, head, n):
        """
        First, obvious edge cases
        Then create dummy, left, and right 
        Move right n steps
        Then start moving both left and right till right gets to the end
        As a result, left will end up on a node prior to a node we want to delete
        Relink it to the element after the node we want to remove 
        """
        if not head: return None
        if head and not head.next: return head.next
        dummy = ListNode(-1)
        dummy.next = head
        l, r  = dummy, dummy
        for _ in range(n):
            r = r.next
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next


    def removeNthFromEnd_pythonic(self, head, n):  # a bit cleaner
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


    def removeNthFromEnd_brute_force(self, head, n):
        def _helper(node):  # counts the number of elements recursively
            if not node: return 0
            if node and not node.next: return 1
            return _helper(node.next) + 1 
        num_of_elements = _helper(head)
        if num_of_elements == 1: return None  # edge case 
        if n == num_of_elements: return head.next # edge case 
        prev, curr = None, head
        for _ in range(num_of_elements - n):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        return head 
        

    def removeNthFromEnd_delayed_pointer(self, head, n):  # One pass, O(n)
        """
        two edge cases 
        move the right pointer to the right while it's one element past the element we want to delete
        then there is an edge case (situation like [1, 2], 2). In this case, r becomes None. We need to repoint head and return it immediately
        After that, start moving both pointers together.
        
        """
        if not head: return
        if head and not head.next: return None
        l, r = head, head
        for _ in range(n + 1):
            if not r: 
                head = head.next
                return head
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    print(l.removeNthFromEnd_delayed_pointer(l, 2))
    