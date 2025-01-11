"""
Given a number n. Return true if the digit sum(or sum of digits) of n is a Palindrome number otherwise false.

A Palindrome number is a number that stays the same when reversed
Examples:
Input: n = 56
Output: true
Explanation: The digit sum of 56 is 5+6 = 11. Since, 11 is a palindrome number.Thus, answer is true.
Input: n = 98
Output: false
Explanation: The digit sum of 98 is 9+8 = 17. Since 17 is not a palindrome,thus, answer is false.
"""
def sum_of_digits_is_palindrome(num):
    """
    O(log10n) to convert
    Same to store
    """
    if num < 10: return True 
    new_val = 0
    for ch in str(num):
        new_val += int(ch) 
    new_val_ch = str(new_val)
    def _helper(s):
        l, r = 0, len(s) - 1
        while l <= r: 
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True   
    return _helper(new_val_ch)


def sum_of_digits_is_palindrome_short(num):
    str_num = str(num)
    return str_num == str_num[::-1]