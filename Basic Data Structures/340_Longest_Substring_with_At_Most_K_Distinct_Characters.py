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

def lengthLongestSubstring_alt(s, k):
    charMapping, start = {}, 0
    result = 0

    for end, s in enumerate(s):
        if s in charMapping:
            charMapping[s] += 1
        else:
            charMapping[s] = 1

        if len(charMapping) <= k:
                result = max(result, end-start+1)
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

if __name__ == '__main__':
    print(lengthLongestSubstring_alt("abcadcacacaca", 3))
