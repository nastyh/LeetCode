import math


class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        O(N) to process
        O(1) nothing to store
        Go over the string and get the index of the last odd digit
        Take everything up to this index from the original num
        -math.inf is needed for cases like "4". You want to return an empty string here
        Taken care in the return statement 
        """
        last_odd_ix = -math.inf
        for ix in range(len(num)):
            if int(num[ix]) % 2 == 1:
                last_odd_ix = ix
        return num[:last_odd_ix+1] if last_odd_ix!= -math.inf else ""
    
    def largestOddNumber_pythonic(self, num: str) -> str:
        """
        O(N) to process
        O(1) nothing to store
        Just use built-in functions
        """
        return num.rstrip("02468")
    
    def largestOddNumber_from_right(self, num: str) -> str:
        """
        O(N) to process
        O(1) nothing to store
        Go from the end
        find the first odd number's index, break the loop
        build the answer: everything up to this index
        """
        rightmost_ix = -math.inf
        for ix in range(len(num) -1, -1, -1):
            if int(num[ix]) % 2 == 1:
                rightmost_ix = ix
                break 
        return num[:rightmost_ix + 1] if rightmost_ix != -math.inf else ""