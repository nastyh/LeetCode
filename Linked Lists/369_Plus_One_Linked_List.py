def plusOne(head):
    def _helper(node):
        if not node: return 1
        carry = _helper(node.next)
        s = node.val + carry
        node.val = s % 10
        return s // 10

    carry = _helper(head)
    if carry == 1:
        root = ListNode(1)
        root.next = head
        return root
    else:
        return head


def plusOne_alt(head):
    def reverse(l):
        prev = None
        while l:
            next_n = l.next
            l.next = prev
            prev = l
            l = next_n
        return prev
    revhead = reverse(head)
    cur = revhead
    num = 1 
    while num:
        num += cur.val
        cur.val = num % 10
        num //= 10
        if num and not cur.next: cur.next = ListNode()
        cur = cur.next
    return reverse(revhead)

