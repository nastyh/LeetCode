def partition(s):  # O(N * 2^N) and O(N)
    def isPar(s):
        return s == s[::-1]
    def dfs(s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if isPar(s[:i]):
                dfs(s[i:], path + [s[:i]], res)
    res = []
    dfs(s, [], res)
    return res


def partition_another(s):
    res, len_s = [], len(s)
    def _isPal(s):
        return s == s[::-1]
    def _helper(s, ix, path):
        if ix == len(s):
            res.append(path)
            return
        for i in range(ix + 1, len_s + 1):
            if _isPal(s[ix + 1:]):
                _helper(s, i, path + [s[ix + 1:]])
    _helper(s, 0, [])
    return res
        

def partition_alt(s):
     ans = []
    def dfs(currList, k):
        if k == len(s):
            ans.append(currList)
            return
        for i in range(k, len(s)):
            tmpStr = s[k:i + 1]
            if tmpStr == tmpStr[::-1]:
                dfs(currList + [tmpStr], i + 1)
    dfs([], 0)
    return ans


def partition_memo(s):
    if len(s) == 0:
        return []
    
    def isPalindrome(string):
        li, ri = 0, len(string) - 1
        while li < ri:
            if string[li] != string[ri]:
                return False
            li += 1
            ri -= 1
        return True
    cache = {}  
    def helper(string):
        if string in cache:
            return cache[string]
        res = []
        for i in range(len(string)):
            if isPalindrome(string[:i + 1]):
                if i == len(string) - 1:
                    res.append([string[:i + 1]])
                else:
                    subs = helper(string[i + 1:])
                    for sub in subs:
                        res.append([string[:i + 1]] + sub)
        cache[string] = res
        return res
    res = helper(s)
    return res