"""
You are given two strings s and t. You can select any substring of string s and rearrange the
characters of the selected substring. Determine the minimum length of the substring of s
such that string t is a substring of the selected substring.

Signature
int minLengthSubstring(String s, String t)

Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1

Example
s = "dcbefebce"
t = "fd"'
output = 5

Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.
"""
from collections import Counter
import math

def minLengthSubstring(s: str, t: str) -> int:
    """
    O(st), to go over both strings
    O(t) to store the frequency of chars from t and the current window
    """
    if not s or not t:
        return -1
    # Step 1: Character requirements from t
    target_count = Counter(t)
    current_count = Counter()
    # Step 2: Initialize pointers and variables
    left = 0
    min_length = math.inf
    required_chars = len(target_count)  # Unique chars needed
    formed_chars = 0  # Unique chars satisfying frequency
    # Step 3: Expand with right pointer
    for right in range(len(s)):
        char_right = s[right]
        current_count[char_right] += 1
        
        # Check if this char satisfies a target requirement
        if char_right in target_count and current_count[char_right] == target_count[char_right]:
            formed_chars += 1
        # Step 4: Contract with left pointer when all characters are covered
        while formed_chars == required_chars:
            # Update minimum length if needed
            min_length = min(min_length, right - left + 1)
            # Contract from the left
            char_left = s[left]
            current_count[char_left] -= 1
            if char_left in target_count and current_count[char_left] < target_count[char_left]:
                formed_chars -= 1
            left += 1
    
    # Return the minimum length or -1 if no valid substring found
    return min_length if min_length != math.inf else -1

# Test case
s = "dcbefebce"
t = "fd"
print(minLengthSubstring(s, t))  # Output: 5
