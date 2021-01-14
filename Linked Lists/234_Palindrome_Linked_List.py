# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def isPalindrome_list(self, head):  # save to a list and check
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res == res[::-1]


    def isPalindrome_optimal(self, head):  # O(n) and O(1)
        """
        Cover edge cases
        Find the middle element using the slow/fast pointer technique
        If the even number, then slow will point to the second middle element
        If the odd, number then exactly to the middle element
        Then we need to reverse the list starting from the middle
        Then we need to compare element by element the reversed list with the left half of the original list
        """
        def _rev(node):  # helper to reverse the list
            if not node: return
            if node and not node.next: return node
            prev, curr = None, node
            while curr:
                next_n = curr.next
                curr.next = prev
                prev = curr
                curr = next_n
            return prev
        
        if not head: return True
        if head and not head.next:
            return True
        checker, slow, fast = head, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_reversed = _rev(slow)
        _rev(slow)  # a nice thing to do: un-reverse the second half of the list not to be messy
        while right_reversed:
            if right_reversed.val == checker.val:
                right_reversed = right_reversed.next
                checker = checker.next
            else:
                return False
        return True


# Straightforward: helper function returns a reversed list, then we compare two lists element by element
    def isPalindrome(self, head):
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
    def isPalindrome_another(self, head):
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
