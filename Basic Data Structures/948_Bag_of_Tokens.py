def bagOfTokensScore(tokens, P):
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