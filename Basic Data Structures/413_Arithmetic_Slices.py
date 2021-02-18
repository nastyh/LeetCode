def numberOfArithmeticSlices(A):  # O(n) and O(1)
    count = comb = last_difference = 0
    for i in range(len(A) - 1):
        difference= A[i + 1] - A[i]
        if i != 0 and difference == last_difference: 
            comb += 1
            count += comb
        else:
            comb = 0
        last_difference = difference
    return count


def numberOfArithmeticSlices_dp(A):  # O(n) both 
    l=[0] * len(A)
    for i in range(2,len(A)):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            l[i] = 1 + l[i - 1]
    return sum(l)