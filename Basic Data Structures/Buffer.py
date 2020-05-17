class Buffer(object):

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
