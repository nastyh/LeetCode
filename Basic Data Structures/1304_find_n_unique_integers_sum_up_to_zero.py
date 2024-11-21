class Solution:
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