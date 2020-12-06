from collections import defaultdict
def matching_pairs(s, t):
    m = sum([s[i] == t[i] for i in range(len(s))])
    cache = set()
    set_s, set_t = {}, {}
    max_match = m
    c = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            if (s[i], t[i]) in cache or s[i] in set_s or s[i] in set_t:
                max_match = max(max_match, m)            
            else:
                max_match = max(max_match, m-1)          
        else:
            if (t[i], s[i]) in cache:
                max_match = max(max_match, m+2)
                
            elif s[i] in set_t and (len(set_t[s[i]]) > 1 or s[i] not in set_t[s[i]]):
                max_match = max(max_match, m+1)
                
            elif t[i] in set_s and (len(set_s[t[i]]) > 1 or t[i] not in set_s[t[i]]):
                max_match = max(max_match, m+1)
                
            elif (s[i], t[i]) in cache or s[i] in set_s or t[i] in set_t:
                max_match = max(max_match, m)
                
            else:
                max_match = max(max_match, m-2)
        
        cache.add((s[i], t[i]))
        
        if s[i] not in set_s:
            set_s[s[i]] = set()
            
        set_s[s[i]].add(t[i])
        
        if t[i] not in set_t:
            set_t[t[i]] = set()
            
        set_t[t[i]].add(s[i])
    return max_match

def matching_pairs_alt(s1, s2):
    base = 0 # matched count
    matched = defaultdict(int) # matched char set
    mismatched = [] # mismatched indicies
    for i, (c1, c2) in enumerate(zip(s1,s2)):
        if c1 == c2: 
            base += 1
            matched[c1] += 1
        else: mismatched.append(i)
    
    # if all matched and all chars are unique, any swap will result in -2
    if not mismatched and len(matched) == base: return base - 2

    # perfect swap for (c1, c2) if (c2, c1) is also a mismatch
    paired = set()
    for i in mismatched:
        if (s1[i], s2[i]) in paired: return base + 2
        paired.add((s2[i], s1[i]))

    # swapping at least one char into place
    seen = defaultdict(lambda: set())
    for i in mismatched: seen[s2[i]].add(i)
    if any((s1[i] in seen and i not in seen[s1[i]]) for i in mismatched): return base + 1
    
    # check if neutral swaps exists
    if len(mismatched) >= 2 or \
        any(s1[i] in matched for i in mismatched) or \
        any(count >= 2 for count in matched.values()):
        return base
    
    return base - 1


if __name__ == '__main__':
    print(matching_pairs('abcd', 'adcb'))
    print(matching_pairs('mno', 'mno'))
    print(matching_pairs('abcd', 'adcb'))
    print(matching_pairs_alt('mno', 'mno'))