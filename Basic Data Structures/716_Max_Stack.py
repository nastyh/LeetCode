from collections import defaultdict
from heapq import heappush, heappop, heapify
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

