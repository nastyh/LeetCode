 def restoreIpAddresses(s):  # O(1) as there is no more than 27 combinations to check
    res = []
    def backtrack(s, current, start):
        if len(current) == 4:
            if start == len(s):
                res.append(".".join(current))
            return
        for i in range(start, min(start+3, len(s))):
            if s[start] == '0' and i > start:
                continue
            if 0 <= int(s[start:i+1]) <= 255:
                backtrack(s, current + [s[start:i+1]], i + 1)
    
    backtrack(s, [], 0)
    return res
