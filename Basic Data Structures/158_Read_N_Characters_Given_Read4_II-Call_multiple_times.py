class Solution(object):  # O(n) both
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
			buf[count:count + 4] = tmp4
			count += t
		if count > n:
			self.remain = deque(tmp4[t - (count - n):t])    # Copy overflow characters TO queue
			count = n
		return count

    
# with a queue

class Solution(object):  # O(nR) n times and R is time complexity of read4. O(f) where f is the size of the file 
    
    def __init__(self):
        self.buffer = collections.deque()
    
    def read(self, buf, n):
        buf4 = [None] * 4
        while len(self.buffer) < n:
            num = read4(buf4)
            if num == 0:
                break
            self.buffer.extend(buf4[:num])
            
        i = 0
        while i < n and self.buffer:
            buf[i] = self.buffer.popleft()
            i += 1
            
        return i