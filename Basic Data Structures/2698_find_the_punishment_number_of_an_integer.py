class Solution:
    def punishmentNumber_dfs(self, n: int) -> int:
        """
        O(n*2^m), n is the length of a number, m is the num of digits in i^2
        O(logn) due to the recursion stack
        """
        def dfs(s: str, target: int, index: int, curr_sum: int) -> bool:
            """Performs a depth-first search to check valid partitions."""
            if index == len(s):
                return curr_sum == target
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if dfs(s, target, i + 1, curr_sum + num):
                    return True
            return False

        def can_partition(num: int, target: int) -> bool:
            """Checks if the square of a number can be partitioned into contiguous substrings summing to the number."""
            s = str(num)
            return dfs(s, target, 0, 0)

        res = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(str(square), i):
                res += square
        return res