from typing import List

class Solution:
    def xorAllNums_brute_force(self, nums1: List[int], nums2: List[int]) -> int:
        """
        O(len(nums1)*len(nums2))
        O(len(nums3)) 
        Times out 
        Just do what it asks: xor two lists
        then xor the resulting list to get a number
        """
        nums3 = []
        for num1 in nums1:
            for num2 in nums2:
                nums3.append(num1^num2)
        res = nums3[0]
        for num in nums3[1:]:
            res ^= num
        return res
    
    def xorAllNums_optimized(self, nums1: List[int], nums2: List[int]) -> int:
        """
        O(n + m), where lenghts of nums1 and nums2
        O(1)
        a xor a = 0 
        a xor a = a 
        xor is also commutative and associative, so we can xor inside nums1, inside nums2
        and then the results
        
        if nums2 has an even number of elements, XORing nums1 with every element in num2
        will result in 0 b/c
        x ^ x ^ y ^ y.. = 0 where every element in nums2 cancels out when XORed an even num
        of times 
        Same: if nums2 has an even number of elements, XORing all pairs involving nums2 also results in 0
        The result depends only on the XOR of all elements in nums1 and nums2 if both arrays have odd lengths.
        If either array has an even length, the result is 0
        """
        xor1 = 0
        xor2 = 0
        # xor everything in nums1
        for num in nums1:
            xor1 ^= num
        # xor everything in nums2
        for num in nums2:
            xor2 ^= num
        if len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
            return xor1 ^ xor2
        elif len(nums1) % 2 == 1:
            return xor2
        elif len(nums2) % 2 == 1:
            return xor1
        else:
            return 0

