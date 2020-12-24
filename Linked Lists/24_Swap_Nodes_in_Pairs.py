# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
	def swapPairs(self, head):
		t = ListNode(-1)
		t.next = head
		prev = t
		if not head: return
		while head and head.next:
			first = head
			second = head.next
			prev.next = second
			first.next = second.next
			second.next = first
			prev = first
			head = first.next
		return t.next


	def swapPairs_alt(self, head):
		if not head: return
        first = head
        second = head.next
        while first and second:
            first.val, second.val = second.val, first.val
            first = second.next
            if not first: break
            second = second.next.next
        return head

	def swapPairs_rec(self, head):  # O(n) and O(n)
		if not head or not head.next:
            return head
        # Nodes to be swapped
        first_node = head
        second_node = head.next
        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node

        