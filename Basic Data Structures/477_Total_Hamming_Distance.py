def totalHammingDistance(nums): # O(n) and O(log2(V)) ~ O(1)
    """
    The * operator turns the list of 32-bit wide binary strings returned by map into individual arguments to the zip method.
    The zip method vectorizes the string arguments to create a list of vectors (each of which is a vector b of particular bits
    from every element in the input array; There are 32 such vectors of size len(nums) each, in this list ).
    """
    return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))


def totalHammingDistance_prefix(nums):
    ans = 0
    freq = [0]*32 # count of "1" (32-bit "overkill")
    for k, x in enumerate(nums): 
        x = bin(x)[2:].zfill(32) # 32-bit binary  
        for i in range(32): 
            if x[i] == "0": ans += freq[i] # count of 1 
            else: # x[i] == "1"
                ans += k - freq[i] # count of 0
                freq[i] += 1 # update count 
    return ans 