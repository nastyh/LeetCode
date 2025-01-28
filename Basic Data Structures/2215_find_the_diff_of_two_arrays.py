class Solution:
    def findDifference_pythonic(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        diff1 = [num for num in s1 if num not in s2]
        diff2 = [num for num in s2 if num not in s1]
        return [diff1, diff2]

    
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
