from typing import Counter, List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        O(nlogn) to sort
        O(n) to create a copy of the sorted list 
        A subsequence can jump over elements. We need to find the k largest values in nums.
        They will give us the max sum. We will need to show them in the return statement
        sort the list and pick the k largest elements: they'are in our_candidates
        create need in the shape of value: how many times it exists in our_candidates

        iterate over original nums
        once we see a proper candidate, we will check -- by using need -- 
        how many times we encounter it the list of our preferred candidates
        need to use up all threes before moving on.
        """
        res = []
        sorted_nums = sorted(nums, reverse=True)
        our_candidates = sorted_nums[:k]
        need = Counter(our_candidates)
  
        for num in nums:
            if need[num] > 0:
                res.append(num)
                need[num] -= 1 
                if len(res) == k:
                    break
        return res
