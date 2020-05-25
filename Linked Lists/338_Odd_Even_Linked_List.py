class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def oddEvenList(self, head):
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
