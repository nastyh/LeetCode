# checking if a given number is a power of two
import math
def isPower2(n):
    assert n > 0, "n should be positive"
    return 2**(math.log2(n)) == n

# using the formula a^(log(n)) == n; log has a base of a
