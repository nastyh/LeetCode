class Solution(object):
	def __init__(self):
		self.remain = deque()                           # Queue to hold extra characters
	def read(self, buf, n):
		"""
		Copy from remaining queue at beginning, if needed
		Copy to remaining queue at end, if needed
		"""
		count = 0
		while self.remain and count < n:                # Copy overflow characters FROM queue
			buf[count] = self.remain.popleft()
			count += 1
		tmp4 = [''] * 4
		t = 1
		while count < n and t > 0:                      # Loop is same as Read Once
			t = read4(tmp4)
			buf[count:count+4] = tmp4
			count += t
		if count > n:
			self.remain = deque(tmp4[t-(count-n):t])    # Copy overflow characters TO queue
			count = n
		return count

    
# with a queue

from queue import Queue
class Solution:
    def __init__(self):
        self.queue = Queue()
        
    def read(self, buf, n):
        qnt = 1
        while self.queue.qsize() < n and qnt:
            bf = [''] * 4
            qnt = read4(bf)
            for i in range(qnt):
                self.queue.put(bf[i])
        i = 0
        while i < n and self.queue.qsize():
            buf[i] = self.queue.get()
            i += 1
        return i