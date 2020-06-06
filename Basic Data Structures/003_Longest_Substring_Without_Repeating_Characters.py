def lengthOfLongestSubstring(s):
    m = set()
    res, l, i = 0, 0, 0

    while i < len(s):
        if s[i] not in m:
            m.add(s[i])
            res = max(res, len(m))
            i += 1
        else:
            m.remove(s[l])
            l += 1
    return res

def lengthOfLongestSubstring_dict(s):
    dic = {}
    res = 0
    left = -1
    for i, ch in enumerate(s):
        if ch in dic:
            left = max(left, dic[ch])
        dic[ch] = i
        res = max(res, i-left)
    return res

def lengthOfLongestSubstring_dict_alt(s):
    d, l, res = {}, 0, 0
    for k, v in enumerate(s):
        if v in d and d[v] >= l:
            l = d[v] + 1
        else:
            res = max(res, k - l + 1)
        d[v] = k
    return res

def lengthOfLongestSubstring_set(s):
    storage, curr, glob, l = set(), 0, 0, 0
    for char in s:
        if char not in storage:
            storage.add(char)
            curr = len(storage)
            glob = max(glob, curr)

        else:

            storage.remove(s[l])
            l += 1
    return glob

def lengthOfLongestSubstring_stack(self, s: str) -> int:
        stack=[]
        res=0
        for i in range(len(s)):
            if s[i] not in stack:
                stack.append(s[i])
                res=max(res,len(stack))
            elif s[i] in stack:
                stack=stack[stack.index(s[i])+1:]+[s[i]]
        return res

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring_dict('abcabcbb'))
    print(lengthOfLongestSubstring_dict_alt('au')) #pwwkew
    print(lengthOfLongestSubstring_set('pwwkew'))
