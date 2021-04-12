from collections import deque
def constructArray(n, k):  # O(n) and O(1)
    """
    Increasing or decreasing list gives at least 1 distinct abs difference
    Jumping min-max list 1, n, 2, n-1, 3, n-2, ... (e.g. 1, 5, 2, 4, 3) or max-min list n, 1, n-1, 2, n-2, 3, ... (e.g. 5, 1, 4, 2, 3)
    gives maximum n - 1 distinct absolute differences.
    We can use k elements from the second algorithm and n-k elements from the first one (e.g. (1, 5, 2), (3, 4))
    or n-k elements from the first algorithm and k elements from the second one (e.g. (1, 2), (5, 3, 4)).
    """
    i, j = 1, n; ret = [i] 
    while i < j:
        if (k > 1) ^ (ret[-1] == i):
            i += 1; ret.append(i)
        else:
            ret.append(j); j -= 1
        k -= 1
    return ret


def constructArray_deque(n, k):
    """
    Consecutively use the smallest and largest available numbers from a deque of [1, 2, ... n] to form your unique pairs.
    You'll get a sequence n-1, n-2, n-3, etc. Stop when you hit k-1. Then fill the rest with consecutive values which will all have a difference of 1.
    This will get you k unique values.
    """
    dq = deque(range(1, n + 1))
	res = []
	for i in range(k):
		pop = dq.popleft if i & 1 else dq.pop
		res.append(pop())
	res.extend(reversed(dq) if k & 1 else dq)  # to make sure the diff stays 1
	return res


def constructArray_another(n, k):
     ans = list(range(1, n - k))
    for i in range(k + 1):
        if i % 2 == 0:
            ans.append(n - k + i // 2)
        else:
            ans.append(n - i // 2)
    return ans