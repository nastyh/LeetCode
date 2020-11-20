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
