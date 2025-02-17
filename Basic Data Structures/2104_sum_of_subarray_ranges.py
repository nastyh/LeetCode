from typing import List


class Solution:
    def subArrayRanges_monotonic_stack(self, nums: List[int]) -> int:
        """
        O(n) both 
        calculate the sum of subarray ranges by determining,
        for each element, how many subarrays have that element as the minimum and as the maximum.
        Then, the total sum is the contribution from all maximums minus the contribution from all minimums.
        First Loop: Computes contributions when an element acts as the minimum.
        Second Loop: Computes contributions when an element acts as the maximum.
        """
        n, res, st = len(nums), 0, []
        for r in range(n+1):
            """
            The stack is maintained so that the indices are in increasing order of their corresponding values in nums.
            """
            while st and (r == n or nums[st[-1]] >= nums[r]):
                mid = st.pop() # potential min
                l = -1 if not st else st[-1]
                """
                The number of subarrays in which nums[mid] is the minimum is calculated
                (mid−l)×(r−mid)
                We then subtract the contribution of this element as a minimum from res 
                """
                res -= nums[mid] * (mid-l) * (r-mid)
            st.append(r)
        st.clear()
        for r in range(n+1):
            """
            stack is maintained in decreasing order of the values in nums.
            mid is the index of the element considered as a potential maximum.
            """
            while st and (r == n or nums[st[-1]] <= nums[r]):
                mid = st.pop()
                l = -1 if not st else st[-1]
                res += nums[mid] * (mid - l) * (r - mid)
            st.append(r)
        return res 

    def subArrayRanges_brute_force(self, nums: List[int]) -> int:
        """
        O(n^2)
        O(1)
        Just generate all possible subarrays
        each i is the starting index of a subarray
        iterate inside from i to the end
        get curr_min and curr_max, update res
        """
        n = len(nums)
        res = 0
        for i in range(n):
            cur_min = cur_max = nums[i]
            # Extend the subarray starting at index i
            for j in range(i, n):
                cur_min = min(cur_min, nums[j])
                cur_max = max(cur_max, nums[j])
                res += cur_max - cur_min
        return res
        