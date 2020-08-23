from collections import Counter
def checkInclusion(s1, s2):  # slow but works
    if len(s2) < len(s1): return False
    def _isPerm(s1, s2):
        return Counter(s1) == Counter(s2)
    l, r = 0, len(s1) - 1
    while r < len(s2):
        if not _isPerm(s1, s2[l:r + 1]):
            l += 1
            r += 1
        else:
            return True
    return False
    

def checkInclusion_alt(s1, s2):
    s, e = 0, len(s1)
    s1 = sorted(s1)
    chars = list(set(s1))
    while s <= len(s2) - e:
        if s2[s] in chars and sorted(s2[s:s + e]) == s1:
            return True
        s += 1
    return False


if __name__ == '__main__':
    print(checkInclusion('ab', 'eidbaooo'))
    print(checkInclusion('ab', 'eidboaoo'))
