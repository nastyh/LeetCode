from collections import deque
def bagOfTokensScore(tokens, P):  # O(nlogn) both b/c sorting (timsort in Python) also takes space
    tokens.sort()
    res = 0
    l, r = 0, len(tokens) - 1
    while l <= r and (res or P >= tokens[l]):
        if P >= tokens[l]:
            res += 1
            P -= tokens[l]
            l += 1
        elif l != r:
            res -= 1
            P += tokens[r]
            r -= 1 
        else:
            break  
    return res
    

def bagOfTokensScore_deque(tokens, P):  #same as above
    tokens.sort()
    d = deque(tokens)
    ans = score = 0
    while d and (P >= deque[0] or score):
        while d and P >= d[0]:
            P -= d.popleft()
            score += 1
        ans = max(ans, bns)
        if d and score:
            P += d.pop()
            score -= 1
    return ans