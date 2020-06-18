def findShortestSubArray(nums):
	left, right, count = {}, {}, {}
	for i, x in enumerate(nums):
	    if x not in left: left[x] = i
	    right[x] = i
	    count[x] = count.get(x, 0) + 1

	ans = len(nums)
	degree = max(count.values())
	for x in count:
	    if count[x] == degree:
	        ans = min(ans, right[x] - left[x] + 1)

	return ans

if __name__ == '__main__':
	print(findShortestSubArray([1,2,2,3,1]))
	print(findShortestSubArray([1,2,2,3,1,4,2]))

        