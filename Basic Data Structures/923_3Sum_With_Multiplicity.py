from collections import defaultdict
def threeSumMulti(arr, target):  # O(NW) and O(W^2) where N is the length of the array and W is the number of unique elements in the array 
    """
    Keep counting the number of elements we have seen so far and keep ones and twos counters, which correspond to the number of ways given values
    can be constructed (as a sum) using one and two array elements respectively. So, we iterate over an array and do the following three steps as a pipeline:

    Update the total count by looking up the number of two-sums (twos) that if you add current value to would give you target.
    Update the number of twosums (twos) by looking at the numbers that have appeared before (ones).
    Update the counts of numbers that have
    """
	total = 0
	mod = 10 ** 9 + 7
	ones = defaultdict(int)
	twos = defaultdict(int)
	for t, v in enumerate(arr):  # O(N)
		total = (total + twos[target - v]) % mod
		for k, c in ones.items():  # O(W)
			twos[k + v] += c
		ones[v] += 1
	return total


def threeSumMulti_3sum_analogue(arr, target):  # O(N^2) and O(N)
    MOD = 10**9 + 7
    count = Counter(A)
    keys = sorted(count)
    ans = 0
    for i, x in enumerate(keys):
        T = target - x
        j, k = i, len(keys) - 1
        while j <= k:
            y, z = keys[j], keys[k]
            if y + z < T:
                j += 1
            elif y + z > T:
                k -= 1
            else: # x+y+z == T, now calculate the size of the contribution
                if i < j < k:
                    ans += count[x] * count[y] * count[z]
                elif i == j < k:
                    ans += count[x] * (count[x] - 1) / 2 * count[z]
                elif i < j == k:
                    ans += count[x] * count[y] * (count[y] - 1) / 2
                else:  # i == j == k
                    ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                j += 1
                k -= 1
    return ans % MOD