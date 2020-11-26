from collections import Counter
def longestSubstring(s, k):
    if not s: return 0
    d = Counter(s)
    segments = []
    start = 0
    for i in range(len(s)):
        if d[s[i]] < k:
            if start < i:
                segments.append(s[start:i])
            start = i + 1
    if start != len(s):
        segments.append(s[start:])
    if len(segments) == 1:
        return len(segments[0])
    max_len = 0
    for segm in segments:
        curr_len = longestSubstring(segm, k)
        max_len = max(max_len, curr_len)
    return max_len


if __name__ == '__main__':
    print(longestSubstring('aaabb', 3))
    print(longestSubstring('ababbc', 3))