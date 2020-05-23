class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums2_index=0
        nums1_index = 0
        while nums2_index < n and nums1_index < m:
            if nums2[nums2_index] <= nums1[nums1_index]:
                nums1.insert(nums1_index, nums2[nums2_index])
                m += 1
                nums2_index += 1
            nums1_index += 1
        while nums2_index < n:
            nums1.insert(m, nums2[nums2_index])
            m += 1
            nums2_index += 1
        for _ in range(n):
            nums1.pop()


        # res = [None] * (m + n)
        # i, j, k = 0, 0, 0

        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         res[k] = nums1[i]
        #         i += 1
        #         k += 1
        #     else:
        #         res[k] = nums2[j]
        #         j += 1
        #         k += 1

        # while i < m:
        #     res[k] = nums1[i]
        #     i += 1
        #     k += 1

        # while j < n:
        #     res[k] = nums2[j]
        #     j += 1
        #     k += 1

        # return res

