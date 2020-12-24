def deleteDuplicates(head):
    dummy = ListNode(-1)
    dummy.next = head
    pred = dummy
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            pred.next = head.next
        else:
            pred = pred.next
        head = head.next
    return dummy.next
    
def deleteDuplicates_recursive(head):
    if head == None or head.next == None:
        return head
    currentValue = head.val
    if (currentValue != head.next.val):
        head.next = self.deleteDuplicates(head.next)
        return head
    while(head and head.val == currentValue):
        head = head.next
    return self.deleteDuplicates(head)