"""
Given a String S consisting only lowercase alphabets and an integer K.
Find the count of all substrings of length K which have exactly K-1 distinct characters.

Input:
S = "abcc"
K = 2
Output:
1
Explanation:
Possible substrings of length K = 2 are
ab : 2 distinct characters
bc : 2 distinct characters
cc : 1 distinct character
Only one valid substring exists {"cc"}. 
"""
from collections import defaultdict

def countOfSubstrings_effiient(S, K):
    """
    O(S)
    O(1) due to 26 elements
    """
    n = len(S)
    if K > n:
        return 0
    # Array to track the frequency of characters in the current window
    freq = [0] * 26
    distinct_count = 0  # Number of distinct characters in the current window
    result = 0
    # Initialize the first window of size K
    for i in range(K):
        index = ord(S[i]) - ord('a')
        if freq[index] == 0:
            distinct_count += 1
        freq[index] += 1
    # Check if the initial window has exactly K-1 distinct characters
    if distinct_count == K - 1:
        result += 1
    # Now slide the window over the rest of the string
    for i in range(K, n):
        # Remove the character going out of the window
        left_index = ord(S[i - K]) - ord('a')
        freq[left_index] -= 1
        if freq[left_index] == 0:
            distinct_count -= 1
        # Add the new character coming into the window
        right_index = ord(S[i]) - ord('a')
        if freq[right_index] == 0:
            distinct_count += 1
        freq[right_index] += 1
        
        # If the current window has exactly K-1 distinct characters, increment result
        if distinct_count == K - 1:
            result += 1
    
    return result

def countOfSubstrings(S, K):
    """
    O(n) 
    O(1) maybe b/c only 26 keys?
    start by counting the distinct characters in the first window of size K and store this count.
    slide the window by one position
    decrease the count of the character that goes out of the window
    increase the count of the character that comes into the window
    adjust the distinct character count accordingly
    After each window update, if the number of distinct characters is K-1, we increment the result
    """
    n = len(S)
    if K > n:
        return 0
    # Frequency map to count occurrences of characters in the window
    freq_map = defaultdict(int)
    distinct_count = 0  # Tracks the number of distinct characters in the current window
    result = 0
    # Initialize the first window of size K
    for i in range(K):
        if freq_map[S[i]] == 0:
            distinct_count += 1
        freq_map[S[i]] += 1
    
    # If the initial window has exactly K-1 distinct characters, increment result
    if distinct_count == K - 1:
        result += 1
    
    # Now slide the window over the rest of the string
    for i in range(K, n):
        # Remove the character going out of the window
        freq_map[S[i - K]] -= 1
        if freq_map[S[i - K]] == 0:
            distinct_count -= 1
        
        # Add the new character coming into the window
        if freq_map[S[i]] == 0:
            distinct_count += 1
        freq_map[S[i]] += 1
        
        # If the current window has exactly K-1 distinct characters, increment result
        if distinct_count == K - 1:
            result += 1
    
    return result

