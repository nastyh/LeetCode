def smallestRepunitDivByK(K):
    """
    To handle a case when the number doesn't exist, keep a set of seen remainders.
    If you've already seen a remainer, it means you're in the loop, so return -1
    """
    res = 1
    remainder = 1
    remainders = set()
    while res % K != 0:
        res = res * 10 + 1
        remainder = res % K
        if remainder not in remainders:
            remainders.add(remainder)
        else:
            return -1
    return len(str(res))


def smallestRepunitDivByK_optimized(K):
    """
    Same idea but space-optimized:
    if the while loop continues for more than K times, we're in the loop, return -1.
    Otherwise, return the result
    """
     remainder = 0
    for l in range(1,K + 1):
        remainder = (remainder * 10 + 1) % K
        if remainder == 0:
            return l
    return -1
