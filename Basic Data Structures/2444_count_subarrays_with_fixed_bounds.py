class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        Brute force won't do so
        We could focus on each index i and count how many valid subarrays end at i.
        A valid subarray must contain both minK and maxK, and must not contain any element out of the range [minK, maxK].
        we need to know the farthest left we can start considering a subarray from.

        O(n)
        O(1)
        """
        if minK > maxK: return 0
        res = 0
        last_bad_ix = -1 # the most recent value out of the range [minK, maxK],
        last_min_ix = - 2 #  the most recent index with value equal to minK.
        last_max_ix = - 2 # the most recent index with value equal to maxK.

        for ix, element in enumerate(nums):
            if element < minK or element > maxK:
                last_bad_ix = ix # If nums[ix] is out of the range [minK, maxK], update last_bad_ix
            if element == minK:
                last_min_ix = ix 
            if element == maxK:
                last_max_ix = ix 
            # The number of valid subarrays ending at index i equals min(last_min_ix, maxlast_max_ixPosition) - leftBound.
            # If the result is negative, it means there is no valid subarray ending at i. Increment answer by the number of valid subarrays.
            right = min(last_min_ix, last_max_ix)
            if right > last_bad_ix: 
                res += right - last_bad_ix
        return res
    
    def countSubarrays_another(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        O(n) and O(1)
        """
        starting = 0
        min_ix, max_ix = 0, 0
        min_found, max_found = False, False 
        res = 0
        for ix, num in enumerate(nums):
            if num == minK:
                min_found = True 
                min_ix = ix
            if num == maxK:
                max_found = True 
                max_ix = ix 
            if num < minK or num > maxK:
                min_found = max_found = False 
                starting = ix + 1 
            elif min_found and max_found:
                res += min(min_ix, max_ix) - starting + 1
        return res 

    def countSubarrays_one_more(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not minK <= num <= maxK:
                bad_idx = i
            if num == minK:
                left_idx = i
            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)
        return res
            
