from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        O((N1+N2)log⁡(N1+N2)), the lengths. Need to create a dict and sort it later 
        O(nums1+nums2) in the worst case if all nums are different due to the dict
        create a dict based off of the first array
        update using the second one
        sort the dict based on the keys
        build res
        """
        d, res = {}, []
        for pair in nums1:
            d[pair[0]] = pair[1]
        for pair in nums2:
            if pair[0] not in d:
                d[pair[0]] = pair[1]
            else:
                d[pair[0]] += pair[1]
        for k, v in sorted(d.items()):
            res.append([k, v])
        return res
    
    def mergeArrays_pointers(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        O(len(nums1)+len(nums2)) to go over both
        Same to build the answer in the worst case
        Two pointers
        process till you hit the end of the shorter one
        do what is asked
        then process the remainers 
        """
        l, r = 0, 0
        res = []
        while l < len(nums1) and r < len(nums2): # 'or' won't work here 
            if nums1[l][0] == nums2[r][0]: # best case
                res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]: 
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r+= 1
        # process the remaining portions if any 
        while l < len(nums1):
            res.append(nums1[l])
            l += 1
        while r < len(nums2):
            res.append(nums2[r])
            r += 1
        return res