def isMonotonic(A):  # O(n) both
    if len(A) <= 1: return True
    res = [A[i + 1] - A[i] for i in range(len(A) - 1)]
    return True if all([i >= 0 for i in res]) or all([i <= 0 for i in res]) else False

def isMonotonic_mono(A):  # O(n) and O(1)
    if len(A) <= 1: return True
    if len(set(A)) == 1: return True
    inc = decr = True
    for i in range(len(A) - 1):
        if A[i + 1] > A[i]:
            decr = False
        if A[i + 1] < A[i]:
            inc = False
    return inc != decr 


def isMonotonic_2_pass(A):  # O(n) and O(1)
    """
    First pass to find what type it's supposed to be. The sign of the first !=0 difference defines the type
    Then we do a second pass where we check depending on a_type 
    """
    if len(A) <= 1: return True
    a_type = 0
    for i in range(1, len(A)):
        if A[i] - A[i - 1] != 0:
            a_type = A[i] - A[i - 1]
            break
    for i in range(1, len(A)):
        if a_type > 0:
            if A[i] - A[i - 1] < 0:
                return False
        else:
            if A[i] - A[i - 1] > 0:
                return False
    return True


if __name__ == '__main__':
    print(isMonotonic([1, 2, 2, 3]))
    print(isMonotonic([6, 5, 4, 4]))
    print(isMonotonic([1, 3, 2]))
    print(isMonotonic([5, 3, 2, 4, 1]))
    print(isMonotonic([2, 2, 2, 1, 4, 5]))
    print(isMonotonic([3, 1, 9]))
    print("Second\n")
    print(isMonotonic_mono([1,2,2,3]))
    print(isMonotonic_mono([6, 5, 4, 4]))
    print(isMonotonic_mono([1, 3, 2]))
    print(isMonotonic_mono([5, 3, 2, 4, 1]))
    print(isMonotonic_mono([2, 2, 2, 1, 4, 5]))
    print(isMonotonic_mono([3, 1, 9]))
