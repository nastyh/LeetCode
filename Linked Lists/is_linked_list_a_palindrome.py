class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def is_linked_list_a_palindrome_efficient(self, l: Node):
        """
        O(n)
        O(1)

        """
        # Step 1: Find the middle of the linked list
        """
        use a slow and fast pointer to find the middle of the linked list.
        The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
        When the fast pointer reaches the end, the slow pointer will be at the middle.
        """
        slow = fast = l
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        # Step 3: Compare the first half and the reversed second half
        first_half = l
        second_half = prev
        while second_half:  # Only need to compare until the end of the second half
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
    
    def is_linked_list_a_palindrome(self, l: Node):
        """
        O(n) both
        Make a string and check if it's a palindrome
        """
        res = ''
        while l:
            res += str(l.value) 
            l = l.next 
        return res == res[::-1]