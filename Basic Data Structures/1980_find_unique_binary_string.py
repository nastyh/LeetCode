from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        O(n) both
        If you have a list of two digits ['10', '11']
        Go over each element
        if the first digit in the first number is 1, append 0 and vice versa
        If the second digits in the second number is 1, append 0 and vice versa
        Build the answer and return
        strategy is applicable because both the length ofansand the length of each string
        in nums are larger than or equal ton, the number of strings in nums.
        Therefore, we can find one unique position for each string innums.
        """
        res = []
        for i in range(len(nums)):
            if nums[i][i] == '1':
                res.append('0')
            else:
                res.append('1')
        return "".join(res)
    
    def findDifferentBinaryString_pythonic(self, nums: List[str]) -> str:
        n = len(nums)
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
    
    def findDifferentBinaryString_recursion(self, nums: List[str]) -> str:
        """
        O(n^2) to generate all combinations
        O(n) for the recursion stack
        Generate all combinations
        """
        n = len(nums)
        nums = set(nums)
        def _helper(curr):
            """
            curris the current string we have. First, we check if curr.length = n.
            If it is, we need to stop adding characters and assess if we have an answer. Ifcurris innums, we return an empty string. If it isn't, we return curr.
            IfaddZerois not an empty string, we can immediately return it as the answer without needing to make the additional
            call to _helper(curr + "1"). If addZerois an empty string, it means all possible paths from adding a"0"lead to invalid answers,
            and thus _helper(curr + "1")must generate a valid answer, since it's guaranteed that a valid answer exists.
            """
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""
            add_zero = _helper(curr + "0")
            if add_zero:
                return add_zero
            return _helper(curr + "1")
        return _helper("")
