class Solution:
    def findDuplicates_brute_force(self, nums: List[int]) -> List[int]:  # O(n) both
        d = Counter(nums)
        return [k for k, v in d.items() if v == 2]

    def findDuplicates(self, nums: List[int]) -> List[int]:  # O(n) and O(1)
        #numbers are from 1 to n where n is the length of the list
        # it means that all integers in the list are positive
        # go thru the list and change the sign of the prev number to negative
        # if it's already negative, it means we've seen it. Add it to res
        res = []
        for n in nums:
            current = abs(n)  # since we need to access the index and it cannot be negative
            if nums[current - 1] < 0: # because indices are from zero but elements from 1 to n
                res.append(current)
            else:
                nums[current - 1] *= -1
        return res
