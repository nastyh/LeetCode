class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1

        res = []
        for i in short:
            if i in long:
                res.append(i)
                long.remove(i)
        return res
