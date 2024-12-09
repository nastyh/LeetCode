class Solution:
    def isArraySpecial_prefix_sum(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        O(n) both
        odd_cnt is the cumulative count of instances when when the sum is odd
        pref will be a prefix sum list in a sence that shows how many instances prior 
        to the current element have different parity 
        """
        pref, odd_cnt, res = [0], 0, []
        for a, b in pairwise(nums): # first and second, second and third, etc. It's from itertools
            if (a + b) % 2 == 1:
                odd_cnt += 1
            pref.append(odd_cnt)
        for a, b in queries:
            res.append(pref[b] - pref[a] == b - a)
        return res
        
    def isArraySpecial_binary_search(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        O(M + NlogM) where M is the size of nums and N the size of queries
        O(M)
        perform an initial traversal of nums, identify the indices of elements that break
        or violate the special array property. Find the indices of elements nums[i]
        that have the same parity (even or odd) as its previous element:
        if nums[i] % 2 == nums[i-1] % 2 is true, then nums[i] is a violating element.
        After finding these violating indices, we know that any subarray containing
        any of these indices is not a special array. Conversely, if a subarray
        contains no violating indices, then it is a special array.
        perform binary search on the violating indices to see if any violating indices
        fall between the range [start + 1, end]. Note that we start our search at start + 1
        instead of start because the violating indices are defined relative to the element to their left.
        Therefore, the first element of our subarray (at index start) is never a violating element,
        and our search should begin at start + 1.
        """
        def _helper(st, end, violating_list):
            l, r = 0, len(violating_list) - 1
            while l <= r: 
                m = l + (r -l) // 2
                violating_ix = violating_list[m]
                if violating_ix < st:
                    l = m + 1
                elif violating_ix > end: 
                    r = m - 1
                else:
                    return True
            return False 

        res, violating_indices = [False] * len(queries), []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                violating_indices.append(i)
        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            found_violating_index = _helper(
                start + 1, end, violating_indices
            )

            if found_violating_index:
                res[i] = False
            else:
                res[i] = True

        return res