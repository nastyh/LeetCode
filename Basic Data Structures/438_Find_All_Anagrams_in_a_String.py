from collections import Counter
def findAnagrams(s, p): # s -- long, p -- short
    l, r, res = 0, 0, []
    if len(s) == 0: return res
    if len(p) > len(s): return None

    d_p = Counter(p)
    p_len = len(d_p)

    for r in range(len(s)):
        if s[r] in d_p:
            d_p[s[r]] -= 1
        if d_p[s[r]] == 0: # if a given value in the dictionary == 0:
            p_len -= 1 # subtract 1 from p_len
        if p_len == 0: # when p_len is all zero, it means we've met all characters from p in s
            res.append(r - len(p) + 1) # we need to append the index from which we started seeing our characters. It's where we are at now minus the length of p plus 1.
            # res.append(l)
            # for the first instance, we're done once we hit 'a' at index 2. So we do 2 minus len(p) + 1. It gives us zero, or the index of 'c,' the first characted that contributed to the anagram we're looking for
        for i in range(len(p), len(s)):
            if s[i-len(p)] in d_p:
                d_p[s[i-len(p)]] += 1
                if d_p[s[i-len(p)]] > 0 and d_p[s[i-len(p)]] < 2:
                    p_len += 1

            if s[i] in d_p:
                d_p[s[i]] -= 1
                if d_p[s[i]] == 0:
                    p_len -= 1
            if p_len == 0:
                res.append(i - len(p) + 1)





        # if r - l == len(p) - 1:
        #     d_p[s[l]] += 1
        #     if d_p[s[l]] > 0:
        #         p_len += 1
        #     l += 1

    return res




if __name__ == '__main__':
    print(findAnagrams('cbaebabacd', 'abc'))
