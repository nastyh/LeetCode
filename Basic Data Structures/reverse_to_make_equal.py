"""
Given two arrays A & B of Length N,
determine if there is a way to make A equal to B by
reversing any subarrays from array B any number of times.
"""
def are_they_equal(A, B):
    a_length = int(len(A))
    A.sort()
    B.sort()

    for i in range(a_length):
        if A[i] != B[i]:
            return False
    return True 

def are_they_equal_another(A, B):
    """
    O(n) and O(2n)
    """
    n = len(A)
    d1, d2 = {}, {}

    for i in range(n):
        if A[i] not in d1:
            d1[A[i]] = 1
        else:
            d1[A[i]] += 1
        
        if B[i] not in d2:
            d2[B[i]] = 1
        else:
            d2[B[i]] += 1
    return d1 == d2

def are_they_equal_pythonic(A, B):
    d = Counter(A)
    for el in B:
        d[el] -= 1
    return not any(filter(lambda x: x!=0, d.values()))