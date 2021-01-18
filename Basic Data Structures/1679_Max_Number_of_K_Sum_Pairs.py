from collections import defaultdict
def maxOperations_dict(nums, k):  # O(n) both
	dic = defaultdict(int)
	count = 0
	for n in nums:
		if k - n in dic and dic[k - n] > 0:
			dic[k - n] -= 1
			count += 1
		else:
			dic[n] += 1
	return count


def maxOperations_sort(nums, k):  # O(nlogn) and O(1)
	nums.sort()
	s, e = 0, len(nums) - 1
	count = 0

	while s < e:
		add = nums[s] + nums[e]
		if add == k:
			count += 1
			s += 1
			e -= 1
		elif add > k:
			e -= 1
		else:
			s += 1
	return count