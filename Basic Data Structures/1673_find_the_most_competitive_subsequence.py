from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        O(n) both to run and keep the stack
        iterate through the array and maintain a stack that is as "small" as possible.
        if the current number is smaller than the last number in our stack—and if we can
        remove that last number without running out of elements to build a k-length
        subsequence—we pop from the stack
        Otherwise, if our stack hasn't reached length k, we add the current number.
        """
        st = []
        n = len(nums)
        for i, num in enumerate(nums):
            # While there are elements in the stack, and the current element is less than the last element in the stack,
            # and we have enough remaining elements to fill the subsequence to length k, pop from the stack.
            while st and st[-1] > num and (len(st) - 1 + (n - i)) >= k:
                st.pop()
            if len(st) < k:
                st.append(num)
                
        return st