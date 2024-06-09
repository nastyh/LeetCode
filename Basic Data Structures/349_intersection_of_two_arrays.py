class Solution:
    def intersection_pythonic(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        O(nums1 + nums2) both
        figure out which is shorter since the best answer won't be longer than the shorter string
        Both into sets
        Return everything from the shorter set if it exists in the longer set 
        """
        if len(nums1) <= len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1
        sh_set, long_set = set(shorter), set(longer)
        return [ch for ch in sh_set if ch in long_set]

    def intersection_pythonic_set(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(m+n) both 
        return list(set(nums1) & set(nums2))


    def intersection_dict1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        O(nums1 + nums2) both
        works even w/o checking what is longer
        See in the question that nums1 is always shorter so this is why
        """
        d1, d2 = Counter(nums1), Counter(nums2)
        res = []
        for k in d1: 
            if k in d2:
                res.append(kk)
        return res

    def intersection_dict2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        O(nums1 + nums2) both
        more pythonic 
        """
        d1, d2 = Counter(nums1), Counter(nums2)
        return [k for k in d1.keys() if k in d2.keys()]

    def intersection_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(nlogn(n))
        # O(len(both)) for the set  
        nums1.sort()
        nums2.sort()
        i, j = 0, 0 
        intersect = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return [el for el in intersect]

    
