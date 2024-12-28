"""
# Assume we have a File class whose constructor takes a filepath string as an argument. It has a single method called write, which persists bytes directly to disk.

# f = File('/tmp/my/file.txt')
# f.write(b"hello world")
# Write a wrapper class for the file object which allows us to buffer the writes in-memory. The wrapper class, BufferedFile is initialized with a File class object and a buffer size. It has two methods: write and flush. The data should be flushed to disk when the buffer is full, or on demand with a method called flush. All bytes must be stored in the buffer first before being written to disk. The buffer cannot use more memory than the max bytes allowed.

# Example usage:

# f = File('/tmp/my/file.txt')
# buf_size = 1000

# b = BufferedFile(f, buf_size)
# b.write(b"hello world")
# b.flush()
"""
class BufferedFile:
    """
    O(k) per write
    O(buffer_size  + k), k data is being written during a call
    """
    def __init__(self, file_obj, buffer_size):
        """
        Initializes the BufferedFile wrapper.

        :param file_obj: An instance of the File class.
        :param buffer_size: Maximum size of the in-memory buffer in bytes.
        """
        self.file_obj = file_obj
        self.buffer_size = buffer_size
        self.buffer = bytearray()

    def write(self, data):
        """
        Write data to the buffer. If the buffer exceeds the buffer_size,
        flush it to disk.

        :param data: Bytes to write to the buffer.
        """
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("Data must be bytes or bytearray")

        self.buffer.extend(data)

        # Flush to disk if buffer exceeds the buffer_size
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self):
        """
        Flush the buffer to the underlying file and clear the buffer.
        """
        if self.buffer:
            self.file_obj.write(self.buffer)
            self.buffer.clear()

# Example usage:
f = File('/tmp/my/file.txt')
buf_size = 1000

b = BufferedFile(f, buf_size)
b.write(b"hello world")
b.flush()