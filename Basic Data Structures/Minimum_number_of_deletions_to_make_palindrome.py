"""
Find minimum number of deletions required to convert a string into a palindrome.
Example 1:
Input: "ababa"
Output: 0

Input: "abcdba"
Output: 1
Explanation: remove 'c' or 'd'

Input: "aebcbda"
Output: 2
Explanation: remove 'e' and 'd'
"""

def min_number_for_palindrome(s):  # O(N^2) and O(N^2)
    """
    Calculate the length of the largest palindrome subsequence and subtract it from len(s)
    """
    def _helper(st):
        dp = [[0] * len(st) for _ in range(len(st))]
        for i in range(len(st)):
            dp[i][i] = 1
        for start in range(len(st) - 2, -1, -1):
            for end in range(start + 1, len(st)):
                if st[start] != st[end]:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
                else:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
        return dp[0][-1]
    return len(s) - _helper(s)


def min_number_for_palindrome_efficient(s):  # O(n^2) and O(1)
    def _helper(st):
        pre = [0] * len(st)  
        for i in reversed(range(len(st))):
            cur = [0] * len(st)  
            for j in range(i, len(st)):
                if i == j:
                    cur[j] = 1
                    continue
                if st[i] == st[j]:
                    cur[j] = pre[j - 1] + 2
                else:    
                    cur[j] = max(pre[j], cur[j - 1])
            pre = cur        
        return pre[-1] 
    return len(s) - _helper(s)


if __name__ == '__main__':
    print(min_number_for_palindrome('ababa'))
    print(min_number_for_palindrome('abcdba'))
    print(min_number_for_palindrome('aebcbda'))
    print(min_number_for_palindrome_efficient('ababa'))
    print(min_number_for_palindrome_efficient('abcdba'))
    print(min_number_for_palindrome_efficient('aebcbda'))

