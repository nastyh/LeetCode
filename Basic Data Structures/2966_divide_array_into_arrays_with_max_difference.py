from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        O(nlogn) to sort and traverse once
        O(n), b/c sorting creates a copy of the list; but maybe we can say O(1)
        Sort 
        Consider triples as nums[0], nums[1], nums[2]. Then nums[3], nums[4], nums[5], etc
        We move in triplets instead of element by element b/c len(nums) is a multiple of 3 per question
        Then we take three elements. If right minus left > k, doesn't fit
        Otherwise, save a triplet in res
        """
        res = []
        nums.sort()
        for i in range(len(nums), 3):
            l, m, r = nums[i], nums[i+1], nums[i+2]
            if r - l > k:
                return []
            res.append([l, m, r])
        return res