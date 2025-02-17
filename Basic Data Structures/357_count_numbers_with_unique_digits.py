class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        O(n)
        O(1)
        For each digit length k from 1 to n
        The first digit (most significant digit) has 9 choices (cannot be 0).
        Each subsequent digit has fewer choices, since we cannot repeat any digit.
        The total for k digits is added to the result.
        The function sums the valid counts including the number 0.
        """
        # For n = 0, only the number 0 is valid.
        if n == 0:
            return 1

        # For n > 10, the count stays the same as for n = 10 because there are only 10 digits.
        n = min(n, 10)
        total = 1  # Count the number 0

        for k in range(1, n + 1):
            # For a k-digit number (k>=1), the first digit has 9 possibilities (1-9)
            # and the remaining digits are chosen from the remaining available digits.
            count_k = 9
            available = 9  # remaining digits available (0 plus other digits except the chosen one)
            for j in range(1, k):
                count_k *= available
                available -= 1
            total += count_k
            
        return total
    def countNumbersWithUniqueDigits_another(self, n: int) -> int:
        ans = 1
        temp = 1
        for i in range(1, n + 1):
            ans = 9 * temp + ans
            temp = temp*(10-i)
            
            return ans