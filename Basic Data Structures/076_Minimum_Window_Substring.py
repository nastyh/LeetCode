from collections import Counter
import math
def minWindow(self, s, t):
    d = {}
    for c in t:
        d[c] = d.get(c,0) + 1

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

    return s[L:R+1]


    """

go through the string, record the positions of the characters we want to find. Whenever we find all the characters, keep updating the start position to find a substring with local minimum length. After this, update the start position to next one and then keep looking for the missing character.

Implentation:

use a dictionary d to store the number of each character we need to find. (negative values mean we have some extra!) ToFind is the total number of characters we still need to find. ind is a list of indices of the characters in d. head is a pointer in ind so ind[head] is the start position of the substring and s[ind[head]] is that character).


    """

def minWindow_alt(s,  t):
    l, r, curr_ans, curr_l, glob_ans, glob_l = 0, 0, '', 0, '', math.inf
    d = Counter(t)
    l_d = len(t)
    while r < len(s):
        while l_d != 0:
            if s[r] in d:
                d[s[r]] -= 1
            if d[s[r]] == 0:
                l_d -= 1
            r += 1
            curr_ans = s[l: r + 1]
            curr_l = r - l + 1
            if curr_l < glob_l:
                glob_l = curr_l
                glob_ans = curr_ans
            if l_d == 0:
                while l < r and d[s[l]] < 0:
                    d[s[l]] += 1
                    l_d += 1
                    i += 1
    return glob_ans

if __name__ == '__main__':
    print(minWindow_alt("ADOBECODEBANC","ABC"))
                