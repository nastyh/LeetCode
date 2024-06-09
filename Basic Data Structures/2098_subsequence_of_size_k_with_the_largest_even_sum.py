class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        """
        O(nlogn) and O(n)
        if the sum of the top k elements is even, this is what we can return
        Otherwise we need to change one number: replace an odd with an even or vice versa
        replace the smallest even number from res by the largest odd number from the rest of the array, or
        replace the smallest odd number from res by the largest even number from the rest of the array.
        """
        nums.sort(reverse = True)
        n = len(nums)
        topkSum = sum(nums[:k])
        if topkSum % 2 == 0: 
            return topkSum
        minOdd = minEven = float('inf')
        for i in range(k):
            if nums[i] % 2 == 1:
                minOdd = min(minOdd, nums[i])
            else:
                minEven = min(minEven, nums[i])
        res = -1
        for i in range(k, n):
            if nums[i] % 2 == 1 and minEven != float('inf'):
                res = max(res, topkSum + nums[i] - minEven)
            if nums[i] % 2 == 0 and minOdd != float('inf'):
                res = max(res, topkSum + nums[i] - minOdd)

        return res