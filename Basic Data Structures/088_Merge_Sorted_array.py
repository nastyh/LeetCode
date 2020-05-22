class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [None] * (m + n)
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[k] = nums1[i]
                i += 1
                k += 1
            else:
                res[k] = nums2[j]
                j += 1
                k += 1

        while i < m:
            res[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            res[k] = nums2[j]
            j += 1
            k += 1

        return res

