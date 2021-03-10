"""
Input: "abac"
Output: ["a", "b", "c", "aa", "aba"]
"""

def palidromeSubsequences(input):  # O(2^n) both
    def isPalindrome(l):
        return l[::] == l[::-1]]

    def backtracking(input, start, end, temp_list):
    if isPalindrome(temp_list):
        .result.append(temp_list.copy())
    for i in range(start, end):
        temp_list.append(input[i])
        backtracking(input,i + 1, end, temp_list)
        temp_list.pop()

    result = []
    backtracking(input, 0, len(input), [])
    return result
