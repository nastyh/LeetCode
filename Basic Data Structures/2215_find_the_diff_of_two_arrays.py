class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]: # O(n) both
        # two passes, sets to make sure we don't readd the elements we've seen
        res, d1, d2 = [[], []], set(), set()
        for el in nums1:
            if el not in d1:
                d1.add(el)
                if el not in nums2:
                    res[0].append(el)
        for el in nums2:
            if el not in d2:
                d2.add(el)
                if el not in nums1:
                    res[1].append(el)
        return res