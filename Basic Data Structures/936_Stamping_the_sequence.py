from collections import deque
def movesToStamp(stamp, target):
    def _check(substr, stamp):
        res = False
        for c1, c2 in zip(substr, stamp): 
            if c1 == c2:
                res = True
            elif c1 == '?': 
                continue #tricky part, we shouldn't put res = True here, because all "?" case will happen, they shouldn't be considered again
            else:
                return False
        return res
    res = deque()
    move, maxmove = 0, 10 * len(target)
    premove = 0
    while move < maxmove: #O(N), maximum check all element in target one by one
        premove = move
        for i in range(len(target) - len(stamp) + 1): #O(N-S)
            substr = target[i:i + len(stamp)]
            if _check(substr, stamp): #O(S) 
                move += 1
                res.appendleft(i)
                target = target[:i] + '?' * len(stamp) + target[i + len(stamp):]  #update the target string when there is a match #O(N)
                if target == "?" * len(target):
                    return res
        if premove == move:
            return []
    return res


def movesToStamp_another(stamp, target):  # O(N(target - stamp)) both
    def equal(a, b): # b-> can have '?'
        c = 0
        for i in range(len(a)):
            if a[i] != b[i] and b[i] != '?':
                return False
            if b[i] == '?':
                c += 1
        return c < len(b)   # if b has only ?'s, return false, 
            # because there is no need to replace it will just increase
                        # the output array length and runtime.
    ans = []
    n = len(target)
    tar = '?' * n
    m = len(stamp)
    f = True
    while len(ans) < 10 * n and f and target != tar:
        start = 0
        f = False
        while start + m <= n:
            if equal(stamp, target[start:start + m]):
                ans.append(start)
                target = target[:start] + '?' * m + target[start + m:]
                f = True
            start += 1
    if target == tar:
        return ans[::-1]
    return []