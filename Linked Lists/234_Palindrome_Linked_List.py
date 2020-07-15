# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isPalindrome_list(head):  # save to a list and check
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res == res[::-1]


# Straightforward: helper function returns a reversed list, then we compare two lists element by element
    def isPalindrome(head):
        if not head or not head.next: return True
        def _helper(self, node):
            curr = node
            prev = None
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev
        def _compare(self, node1, node2):
            while node1 and node2 and (node1.val == node2.val):
                node1, node2 = node1.next, node2.next
            return node1 == node2
        reversed_l = self._helper(head)
        return self._compare(head, reversed_l)

    
  # The best one: find where the second half starts, reverse it, compare element by element, reverse back  
    def isPalindrome_another(head):
        def _reverseList(node):  # reverses a list
            curr = node
            prev = None
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev
        def _find_second(node):  # returns the end of a first half and the start of a second half
            prev, slow, fast = node, node, node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return [prev, slow]
        
        end_of_first = _find_second(head)[0]
        start_of_second = _find_second(head)[1]
        start_of_reversed = _reverseList(start_of_second)

        isPal = True
        while isPal and start_of_reversed:
            if head.val != start_of_reversed.val:
                isPal = False
            head = head.next
            start_of_reversed = start_of_reversed.next

        back = _reverseList(start_of_reversed)
        return isPal

    def _compare_test(self, node1, node2):
            while node1 and node2 and (node1.val == node2.val):
                node1, node2 = node1.next, node2.next
            return node1 == node2

    def _test_middle(self, node):
        prev, slow, fast = node, node, node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return [prev.val, slow.val]


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)
    m = ListNode(1)
    m.next = ListNode(2)
    m.next.next = ListNode(6)
    m.next.next.next = ListNode(2)
    m.next.next.next.next = ListNode(1)
    # print(l.isPalindrome_list())
    # print(l.isPalindrome())
    # print(l.isPalindrome_alt())
    print(m.isPalindrome_another())
    # print(l._test_middle(l))
