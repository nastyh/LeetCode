from collections import deque

class Buffer_deque:

    def __init__(self, capacity):
        self.buffer = deque()
        self.size, self.capacity = 0, capacity
    
    def write(self, chars):
        for i, c in enumerate(chars):
            if self.size >= self.capacity: return i
            self.buffer.append(c)
            self.size += 1
        return len(chars)
    
    def read(self, n: int) -> str:
        buffer=''
        while n > 0 and self.size > 0:
            buffer += self.buffer.popleft()
            n -= 1
            self.size -= 1
        return buffer


class Buffer_list:
 
    def __init__(self, size):
        self.size = size
        self.queue = []
    def write(self, content):
        count = 0
        for c in content:
            if len(self.queue) < self.size:
                self.queue.append(c)
                count += 1
        return count
    def read(self, n):
        res = ''
        for _ in range(min(n, len(self.queue))):
            res += self.queue.pop(0)
        return res


class Buffer:

    def __init__(self, k):
        self.k = k
        self.buf = [''] * k

        self.size = 0
        self.read_i = 0
        self.write_i = 0


    def write(self, string):
        i, n = 0, len(string)
        # while buffer is not full
        # full is read_i == write_i and self.size == k
        # NOT full is read_i != write_i or self.size != k

        while i < n and \
                (self.read_i != self.write_i or self.size != self.k):
            self.buf[self.write_i] = string[i]
            self.write_i = (self.write_i + 1) % self.k
            self.size += 1
            i += 1
        return i


    def read(self, n):
        """returns the string read.
        """
        i, ret = 0, ''
        # while buffer is NOT empty:
        while i < n and \
                (self.read_i != self.write_i or self.size):

            ret += self.buf[self.read_i]
            self.buf[self.read_i] = ''          # Debugging only

            self.read_i = (self.read_i + 1) % self.k
            self.size -= 1
            i += 1
        return ret


buf = Buffer(5)
assert buf.write('abc') == 3
assert buf.write('def') == 2
assert buf.read(3) == 'abc'
assert buf.write('xyzabc') == 3
assert buf.read(8) == 'dexyz'
assert buf.read(8) == ''
assert buf.write('abcdefg') == 5
assert buf.read(3) == 'abc'
