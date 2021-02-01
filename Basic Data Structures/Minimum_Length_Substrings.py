from collections import Counter
import math
def minWindow_alt(s,  t): # easier to follow
    res = math.inf
    l, r = 0, 0
    d = Counter(t)
    l_d = 0
    while r < len(s):
        d[s[r]] -= 1
        if d[s[r]] >= 0:
            l_d += 1         
        while l_d == len(t):
            # curr_l = r - l + 1
            # if curr_l < glob_l:
            #     glob_l = curr_l
                # glob_ans = s[l: r + 1]
            res = min(res, r - l + 1)
            d[s[l]] += 1
            if d[s[l]] > 0:
                l_d -= 1
            l += 1
        r += 1   
    return res if res != math.inf else -1
    

def minWindow_repurpose(s, t):
    """
    Take the exact solution from 076 but return the length of the resulting string instead of the string itself
    """
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
    return len(glob_ans) if len(glob_ans) != 0 else -1


if __name__ == '__main__':
    print(minWindow_alt("dcbefebce", "fd"))
    print(minWindow_alt("bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", "cbccfafebccdccebdd"))
    print(minWindow_repurpose("dcbefebce", "fd"))
    print(minWindow_repurpose("bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", "cbccfafebccdccebdd"))