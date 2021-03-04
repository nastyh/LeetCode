class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def oddEvenList(self, head):
        """
        Idea is to have two lists: one with odd elements, another with even elements
        Then you need to connect the end of the odd list to the beginning of the even list
        """
        if not head: return None
        if head and not head.next: return head
        odd, even = head, head.next
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head

    def oddEvenList_another(self, head):
        odds = ListNode(-1)
        evens = ListNode(-1)
        oddsHead = odds
        evensHead = evens
        isOdd = True

        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            isOdd = not isOdd
            head = head.next
        evens.next = None
        odds.next = evensHead.next
        return oddsHead.next
