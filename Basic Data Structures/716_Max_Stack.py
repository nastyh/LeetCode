from collections import defaultdict
from heapq import heappush, heappop, heapify

   # use linkedin list + heapq
class Node:
    def __init__(self, val: int, pre: 'Node', next: 'Node', cnt: int, removed: bool=False) -> None:
        self.val = val
        self.pre = pre
        self.next = next
        self.cnt = cnt
        self.removed = False

    def __lt__(self, other):
        if self.val == other.val:
            return self.cnt > other.cnt
        return self.val > other.val

class MaxStack:
    def __init__(self):
        self.head = Node(0, None, None, 0)
        self.tail = Node(0, None, None, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cnt = 0

        self.q = []
        heapq.heapify(self.q)

    def push(self, x: int) -> None:
        self.cnt += 1

        # insert to doubly list
        pretail = self.tail.pre
        node = Node(x, pretail, self.tail, self.cnt)
        pretail.next = node
        self.tail.pre = node

        # insert to heapq
        heapq.heappush(self.q, node)

    def pop(self) -> int:
        # delete from doubly list
        pretail = self.tail.pre
        if pretail == self.head:
            return -1
        
        prepretail = pretail.pre
        prepretail.next = self.tail
        self.tail.pre = prepretail

        # delete from heapq (lasy removal)
        pretail.removed = True
        
        return pretail.val


    def top(self) -> int:
        pretail = self.tail.pre
        if pretail == self.head:
            return -1
        return pretail.val

    def peekMax(self) -> int:
        # delete top lazy removed elements
        while len(self.q) > 0 and self.q[0].removed:
            t = heapq.heappop(self.q)

        if len(self.q) == 0:
            return -1
        return self.q[0].val

    def popMax(self) -> int:
        # delete top lazy removed elements
        while len(self.q) > 0 and self.q[0].removed:
            t = heapq.heappop(self.q)

        # delete from heapq
        node = heapq.heappop(self.q)
        node.removed = True

        # delete from doubly list
        prenode = node.pre
        nextnode = node.next
        prenode.next = nextnode
        nextnode.pre = prenode

        return node.val



class MaxStack:  # O(n)
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self._data = []

	def push(self, x: int) -> None:
		self._data.append(x)

	def pop(self) -> int:
		return self._data.pop()

	def top(self) -> int:
		return self._data[-1]

	def peekMax(self) -> int:
		return max(self._data)

	def popMax(self) -> int:
		target = max(self._data)
		for index in range(len(self._data)-1, -1, -1):
			if self._data[index] == target:
				return self._data.pop(index)


class DoubleLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None

class MaxStack_linked_list:  # finds max in O(logN) and does removal in O(1)
    """
    a double linked list as our "stack". This reduces the problem to finding which node to remove, since we can remove nodes in O(1) time.
    TreeMap can find the largest value, insert values, and delete values, all in O(\log N)O(logN) time.
    """
    def __init__(self):
        self.stack = DoubleLinkedList(float('-inf')) # init a dummy node
        self.last = self.stack                       # reference the stack tail
        self.heap = []
        self.hmap = defaultdict(list)
        

    def push(self, x: int) -> None:
        # O(1)
        node = DoubleLinkedList(x)
        # update the tail
        self.last.next = node
        node.pre = self.last
        self.last = node
        
        # push -x to the min heap
        heappush(self.heap, -x)
        
        # append node the the map entry
        self.hmap[x].append(node)
        
    def pop(self) -> int:
        # O(1)
        # pop from the stack and remove from map
        num = self.last.val
        self.last = self.last.pre
        self.last.next = None
        
        self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        return num

    def top(self) -> int:
        # O(1)
        return self.last.val

    def peekMax(self) -> int:
        # O(logN)
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the the poped elements from heap
        while -self.heap[0] not in self.hmap:
            heappop(self.heap)
        
        return -self.heap[0]

    def popMax(self) -> int:
        # O(logN)
        # get the top-most node from map
        num = self.peekMax()
        node = self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        
        # update the tail reference
        if node == self.last:
            self.last = self.last.pre
        
        # remove the node from stack
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        return num

