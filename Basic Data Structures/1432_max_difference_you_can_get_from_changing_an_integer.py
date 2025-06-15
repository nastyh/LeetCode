import math


class Solution:
    def maxDiff(self, num: int) -> int:
        """
        O(n) to iterate
        O(n) to keep for_a, for_b
        Maximize a:
        replace the first digit from left that is not 9 with 9 everywhere 
        Minimize b:
        if the first digit is not 1, replace it w/ 1
        Otherwise, scan from left to right for the first digit that is not 0 or 1, and replace it with 0.
        """
        for_a, for_b = [n for n in str(num)], [n for n in str(num)]
        digit_to_update = math.inf
        for n in str(num):
            if n != "9":
                digit_to_update = n 
                break 
        for k, v in enumerate(str(num)):
            if v == digit_to_update:
                for_a[k] = "9"

        if str(num)[0] != "1":
            digit_to_update = str(num)[0]
            for_b = ["1" if ch == digit_to_update else ch for ch in str(num)]
        else:
            for digit in str(num)[1:]:
                if digit != "0" and digit != "1":
                    for_b = ["0" if ch == digit else ch for ch in str(num)]
                    break 
        return int(''.join(for_a)) - int(''.join(for_b))
        
        