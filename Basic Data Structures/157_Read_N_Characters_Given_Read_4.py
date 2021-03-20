def read(buf, n):  # O(n) to copy N characters and O(1) to keep the buffer of 4 elements
    """
    At any point buf4, will maximum of 4 characters or count returned from the read4
    Can read utmost 4 chars at a time, so create an array of size 4 and pass it to the function read4(buf4). 
    That read4 function will fill buf4 and returns the count how many characters it filled.
    take those buf4 chars filled and append it to my final buf.
    """
    i = 0
    while i < n: 
        buf4 = ['','','','']
        count = read4(buf4) # Read file into buf4.
        if not count: break # EOF
        count = min(count, n - i)
        buf[i:] = buf4[:count] # Copy from buf4 to buf.
        i += count
    return i


def read_alt(buf, n):
    cnt = 0
    tmp = []
    while cnt < n:
        buf4 = [None] * 4
        rv = read4(buf4)
        cnt += rv
        tmp.extend(buf4)
        if rv < 4:
            break
    buf[:] = [a for a in tmp[:n] if a]
    return len(buf)