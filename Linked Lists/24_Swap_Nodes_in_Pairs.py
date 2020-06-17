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

	def swapPairs_rec(self, head):
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

        