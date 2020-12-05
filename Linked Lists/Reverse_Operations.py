from collections import deque
def reverse(head):
  node = head
  evens = deque()
  while node is not None:
    is_even = node.data % 2 == 0
    if is_even:  # even, start pushing
      evens.append(node)

    if not is_even or node.next is None:  # not even, start popping
        while len(evens) > 1:
            evens[0].data, evens[-1].data = evens[-1].data, evens[0].data
            evens.pop()
            evens.popleft()
        evens.clear()
    node = node.next
  return head
