class Solution:
    def isPalindrome(self, x: int) -> bool: # O(n); how much space? Maybe O(1)
        # the easiest way is to turn into a string
        #two pointers and keep comparing
        s = str(x)
        l, r = 0, len(s) - 1 
        while l <= r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True
    
    def isPalindrome_division(self, x: int) -> bool: 
        # construct a reversed number by 
        # takng the reminder and adding it to the existing result
        # that equal existing * 10
        reversed_num = 0
        orig_num = x
        while x > 0: 
            reversed_num = reversed_num * 10 + x%10
            x = x//10
        return orig_num == reversed_num
        # example with 121
        # reversed is 0 * 10 + 1 = 1 
        # then
        # reversed is 1 * 10 + 2 = 12
        # then
        # reversed is 12 * 10 + 1 = 121
        # compare reversed and original 