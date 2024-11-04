class Solution:
    def addDigits(self, num: int) -> int:
        """
        O(1) both
        """
        if num < 10:  # one digit
            return num
        if num % 9 == 0:
            return 9
        else:
            return num%9

    def addDigits_another(self, num: int) -> int:
        """
        O(1) both
        """
        return 1 + (num - 1) % 9

        