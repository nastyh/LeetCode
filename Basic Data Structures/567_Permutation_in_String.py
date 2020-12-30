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


def checkInclusion_another(s1, s2):  # another slow but works
    """
    Can live with one pointer
    Start the loop from pointing to the element with the index == length of s1 and going to the end of s2
    Using this pointer, need to build the line of the length s1 but counting back 
    Then pass it to the helper function to compare with s1 and make a decision
    """
    if len(s2) < len(s1): return False
    def _helper(first, second):
        return Counter(first) == Counter(second)
    for i in range(len(s1) - 1, len(s2)):
        if _helper(s2[i - len(s1) + 1:i + 1], s1):
            return True
        else:
            continue
    return False


def checkInclusion_dict(s1, s2):  # O(l1 + (l2 - l1)) and O(l2)
    if len(s2) < len(s1): return False
    charCounts = Counter(s1)
    m, n, nChars = len(s1), len(s2), len(charCounts)
    #Only consider window of length m and only check chars in s1
    for i in range(m):
        if s2[i] in charCounts:
            charCounts[s2[i]] -= 1
            if charCounts[s2[i]] == 0:
                nChars -= 1
        if nChars == 0:
            return True
        
    for i in range(m, n):
        if s2[i - m] in charCounts:
            charCounts[s2[i - m]] += 1
            if charCounts[s2[i - m]] == 1: nChars += 1
        if s2[i] in charCounts:
            charCounts[s2[i]] -= 1
            if charCounts[s2[i]] == 0: nChars -= 1
        if nChars == 0:
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


def checkInclusion_more(s1, s2):
    """
    Initialize the right pointer. The left pointer is right minus the length of s1
    Accurate with the indicess
    """
    if len(s2) < len(s1): return False
    def _isPal(st1, st2):
        return Counter(st1) == Counter(st2)
    r = len(s1) - 1
    while r < len(s2):
        if _isPal(s1, s2[r - len(s1) + 1:r + 1]):
           return True
        r += 1
    return False



if __name__ == '__main__':
    # print(checkInclusion('ab', 'eidbaooo'))
    # print(checkInclusion('ab', 'eidboaoo'))
    print(checkInclusion_more('ab', 'eidboaoo'))
    print(checkInclusion_more('ab', 'eidbaooo'))
