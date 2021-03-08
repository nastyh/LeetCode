def removePalindromeSub(s):  # O(n) both b/c of reversing
    """
    two edge cases are obvious
    Otherwise, we need to remove as (or bs) and the remove a palindrome.
    So, it's two
    """
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    return 2


def removePalindromeSub_pointers(s):  # O(n) and O(1)
    """
    Same as above but w/o reversing the string but rather checking element by element 
    """
    def _helper(s):  # isPalindrome
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    if not s:
        return 0
    if _helper(s):
        return 1
    return 2