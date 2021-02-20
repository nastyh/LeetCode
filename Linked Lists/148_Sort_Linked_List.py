def sortList(head):
    if not head or not head.next: return head
    def getSize(head):
        # Simply count the length of linked list
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter   
    def split(head, size):
        # given the head & size, return the the start node of next chunk
        for i in range(size - 1): 
            if not head: 
                break 
            head = head.next

        if not head: return None
        next_start, head.next = head.next, None  #disconnect   
        return next_start    
    def merge(l1, l2, dummy_start):
        # Given dummy_start, merge two lists, and return the tail of merged list
        curr = dummy_start
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2
        while curr.next: curr = curr.next  # Find tail
        # the returned tail should be the "dummy_start" node of next chunk
        return curr  

    total_length = getSize(head)
    dummy = ListNode(0)
    dummy.next = head
    start, dummy_start, size = None, None, 1
    
    while size < total_length:
        dummy_start = dummy
        start = dummy.next 
        while start:
            left = start
            right = split(left, size) # start from left, cut with size=size
            start = split(right, size) # start from right, cut with size=size
            dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start 
        size *= 2
    return dummy.next


class Solution:  # O(nlogn) and O(1)
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(head):
            if not head or not head.next : 
                return head                 # as we branch and move left, left ... when only one node is left, we return it
            
            left = slow = fast = head
            fast = fast.next                # for [1,2,3,4] as mid will be node 3, if this statement not used
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next               # slow is at middle, next elements are considered right
            slow.next = None                # this makes left has only left part
            
            left_sorted = mergeSort(left)
            right_sorted = mergeSort(right)
            return merge(left_sorted, right_sorted)
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            prev = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next            
                prev = prev.next
            prev.next = l1 or l2    # one of l1 and l2 can be non-null at this point
            return dummy.next
        return mergeSort(head)