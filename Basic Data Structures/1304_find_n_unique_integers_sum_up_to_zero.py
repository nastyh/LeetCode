from typing import List


class Solution:
    def sumZero_clean(self, n: int) -> List[int]:
        """
        O(n) both to go over and create a list
        Idea is that if n is odd, our res should be symmetrical around 0
        if n == 5, we will have [-2, -1, 0, 1, 2]
        If n is even, we don't include 0 in res, so for 
        n = 4 we have [-2, -1, 1, 2]
        Start with res = []
        if n is odd, we can extend it as range(0, n//2+1) -- gives the right part 
        if n is even, we can extend it without a zero as range(1, n//2+1) -- still gives us the right part
        then for both cases we need to take the part that is [1, n//2+1], change the sign and add these numbers
        The result will be in an order positives, negatives, but it's still ok 
        """
        res = []
        if n % 2 == 1:
            res.extend(x for x in range(0, n//2 + 1))
        else:
            res.extend(x for x in range(1, n//2 + 1))
        res.extend(-x for x in range(1, n//2 + 1))
        return res



    def sumZero(self, n: int) -> List[int]:
        """
        O(n) and O(n)
        Generate a sequence of numbers from 1 to ( n-1 ).
        The sum of these numbers: n * (n - 1) // 2
        Append the negative of this sum as the last element to ensure that the total sum of the array is zero.
        """
        res = [x for x in range(1, n)]
        res.append(-1 * (n * (n-1)) // 2)
        return res