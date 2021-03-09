from collections import Counter
import math
def minWindow(s, t):  # O(S + t) both where S and T are respective lengths
    d = {}
    for c in t:
        d[c] = d.get(c, 0) + 1
    ToFind, ind = len(t), []
    L, R, head = -len(s)-1, -1, 0
    for i, c in enumerate(s):
        if c in d:
            ind.append(i)
            d[c] -= 1
            if d[c] >=0:
                ToFind -= 1
            if ToFind == 0:
                while d[s[ind[head]]] < 0: # s[ind[head]] is the character
                    d[s[ind[head]]] += 1
                    head += 1
                if i - ind[head] < R - L:
                    L, R = ind[head], i

                d[s[ind[head]]] += 1
                ToFind += 1
                head += 1
    return s[L:R + 1]

    """
go through the string, record the positions of the characters we want to find.
Whenever we find all the characters, keep updating the start position to find a substring with local minimum length. After this, update the start position to next one and then keep looking for the missing character.
Implentation:
use a dictionary d to store the number of each character we need to find. (negative values mean we have some extra!) 
ToFind is the total number of characters we still need to find. ind is a list of indices of the characters in d. head is a pointer in ind so ind[head] is the start position of the substring and s[ind[head]] is that character).
    """

def minWindow_alt(s,  t): # easier to follow
    l, r, curr_l, glob_ans, glob_l = 0, 0, 0, '', math.inf
    d = Counter(t)
    l_d = 0
    while r < len(s):
        d[s[r]] -= 1
        if d[s[r]] >= 0:
            l_d += 1         
        while l_d == len(t):
            curr_l = r - l + 1
            if curr_l < glob_l:
                glob_l = curr_l
                glob_ans = s[l: r + 1]
            d[s[l]] += 1
            if d[s[l]] > 0:
                l_d -= 1
            l += 1
        r += 1   
    return glob_ans


def minWindow_another(s, t):
    if not t or not s:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)
        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1
        if window_counts[character] == dict_t[character]:
            formed += 1
        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]
            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1    

        r += 1    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == '__main__':
    print(minWindow_alt("ADOBECODEBANC", "ABC"))
    print(minWindow_alt("ab", "a"))
    print(minWindow_another("ADOBECODEBANC", "ABC"))
    print(minWindow_another("ab", "a"))
    print(minWindow_alt("dcbefebce", "fd"))