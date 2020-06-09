# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Straightforward: helper function returns a reversed list, then we compare two lists element by element
    def isPalindrome(head):
        if not head or not head.next: return True
        def _helper(node):
            curr = node
            prev = None
            while curr:
                next_n = curr.next
                curr.next = None
                prev = curr
                curr = next_n
            return prev

        reversed_l = _helper(head)
        while head:
            if head.val != reversed_l.val:
                return False
            head = head.next
            reversed_l = reversed_l.next
        return True


    # A more complex one: find the middle, reverse the second half of the list, compare with the first half
    def  isPalindrome_alt(head):
        if not head or not head.next: return True

        def _endOfFirst(node):
            slow, fast = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def _reverseList(node):
            curr = node
            prev = None
            while curr:
                next_n = curr.next
                curr.next = None
                prev = curr
                curr = next_n
            return prev

        first_half_end = _endOfFirst(head)
        second_half_start = _reverseList(first_half_end.next) # now the second half is reversed

        # checking if it's a palindrome
        isPal = True
        first = head
        second = second_half_start
        while isPal and second:
            if first.val != second.val:
                isPal = False
            first = first.next
            second = second.next

        # we can restore the list; kind of a good tone
        first_half_end.next = _helper(second_half_start)

        return isPal



if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)
    print(l.isPalindrome())
    print(l.isPalindrome_alt())
