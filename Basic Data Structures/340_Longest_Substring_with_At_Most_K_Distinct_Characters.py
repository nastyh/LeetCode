def lengthLongestSubstring(s, k):
    if len(s) == 0 or not s:
        return 0
    count = [0] * 256
    i, numDistinct, maxLen = 0, 0, 0
    for j in range(len(s)):
            # udpate j
        if count[ord(s[j])] == 0:
            numDistinct += 1
        count[ord(s[j])] += 1
            # udpate i
        while numDistinct > k:
            count[ord(s[i])] -= 1
            if count[ord(s[i])] == 0:
                numDistinct -= 1
            i += 1
        maxLen =  max(j - i + 1, maxLen)
    return maxLen


def lengthLongestSubstring_another(s, k):
    """
    Bunch of edge cases for strings with length of 1 and 0
    Then the same thing as below:
    start building a dictionary. If it has more than k elements, start shrinking it by moving the left pointer and removing keys once the values become 0
    """
    if len(s) == 0:
        if k == 0:
            return 0
    if len(s) == 1:
        if k == 0:
            return 0
        else:
            return 1
    res = 0
    l, r, d = 0, 0, {}
    while r < len(s):
        if s[r] not in d:
            d[s[r]] = 1
        else:
            d[s[r]] += 1
        while len(d) > k:
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1
        res = max(res, r  - l + 1)  # important to do it here not above the while loop
        r += 1
    return res
                     

def lengthLongestSubstring_alt(s, k):
    charMapping, start = {}, 0
    result = 0

    for end, s in enumerate(s):
        if s in charMapping:
            charMapping[s] += 1
        else:
            charMapping[s] = 1

        if len(charMapping) <= k:
                result = max(result, end - start + 1)
        else:
            while len(charMapping) > k:
                character = s[start]
                freq = charMapping[character]
                if freq == 1:
                    del charMapping[character]
                else:
                    charMapping[character] -= 1
                start += 1
    return result


def lengthLongestSubstring_set(s, k):
    if k == 0:
        return 0
    if len(s) == 0:
        if k == 0:
            return 0
    if len(s) == 1:
        if k == 0:
            return 0
        else:
            return 1
    res = 0
    l, r, unique = 0, 0, set()
    while r < len(s):
        unique.add(s[r])
        r += 1
        res = max(res, r - l + 1)
        if len(unique) >= k:
            unique.remove(s[l])
            l += 1
    return res

if __name__ == '__main__':
    print(lengthLongestSubstring_alt("abcadcacacaca", 3))
    print(lengthLongestSubstring_set("abcadcacacaca", 3))
