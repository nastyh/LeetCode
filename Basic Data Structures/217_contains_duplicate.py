class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        O(n) both 
        """
        s = set()
        for num in nums:
            if num in s: return True
            else:
                s.add(num)
        return False

    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False 

    def containsDuplicate_dict(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for v in d.values():
            if v!=1: return True # at least one item repeats
        return False
    
    def containsDuplicate_dict_pythonic(self, nums: List[int]) -> bool:
        d=Counter(nums)
        return any(v > 1 for v in d.values()) # at least one item repeats

    def containsDuplicate_xor(self, nums: List[int]) -> bool:
        """
        O(n) and O(1). O(n) b/c we need to go over the list to XOR everything
        xor of a number with itself gives 0
        xor of a zero with a number gives a number
        sort nums
        If dups exist, they will be next to each other
        then we will arrive to a situation when we get number ^ same number.
        It returns 0, thus there is a duplicate, return False
        """
        nums.sort()
        for ix in range(1, len(nums)):
            if nums[ix-1] ^ nums[ix] == 0:
                return True
        return False
    
