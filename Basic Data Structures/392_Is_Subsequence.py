def isSubsequence(s, t):
    s_ix = 0
    if len(s) == 0:
        return True
    for el in t:
        if el == s[s_ix]:
            s_ix += 1
        if s_ix >= len(s):
            return True
    return False

def isSubsequence_index(s, t):
    if len(s) > len(t):
        return False
    i = 0
    for ch in s:
        if ch in t[i:]:    
            i = t.index(ch, i) + 1  
        else:
            return False 
    return True 


def isSubsequence_dict_another(s, t):  # fails edge case
    ds, dt = {}, {}
    for k, v in enumerate(s):
        if v not in ds:
            ds[v] = k
    for k, v in enumerate(t):
        if v not in dt:
            dt[v] = k
    if any(w not in dt for w in ds.keys()): return False
    for k, v in ds.items():
        if v > dt[k]:
            return False
    return True

def isSubsequence_dict(s, t):
    if len(s) == 0: return True
    for k, v in enumerate(s):
        if t.index(v) >= k:
            continue
        else:
            return False
    return True
    # d_s, d_t = {}, {}
    # for k, v in enumerate(s):
    #     d_s[v] = k
    # for k, v in enumerate(t):
    #     d_t[v] = k
    # if len(d_s) > len(d_t):
    #     return False
    # # if any(k not in d_t.keys() for k in d_s.keys()): return False
    # for k, v in enumerate(d_s):
    #     if d_s[]




    # for k, v in d_s.items():
    #     if v > d_t[k]:
    #         return False
    #     else:
    #         continue
    # return True

if __name__ == '__main__':
    # print(isSubsequence('abc','anbgdc'))
    # print(isSubsequence('axc','ahbgdc'))
    # print(isSubsequence_dict('axc','ahbgdc'))
    print(isSubsequence_dict('abc','ahbgdc'))
    print(isSubsequence_dict('acb','ahbgdc'))

