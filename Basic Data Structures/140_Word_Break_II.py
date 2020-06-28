from collections import Counter
def wordBreak(s, wordDict):
    # quick check on the characters,
    #   otherwise it would exceed the time limit for certain test cases.
    if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
        return []

    wordSet = set(wordDict)

    dp = [[]] * (len(s)+1)
    dp[0] = [""]

    for endIndex in range(1, len(s)+1):
        sublist = []
        # fill up the values in the dp array.
        for startIndex in range(0, endIndex):
            word = s[startIndex:endIndex]
            if word in wordSet:
                for subsentence in dp[startIndex]:
                    sublist.append((subsentence + ' ' + word).strip())

        dp[endIndex] = sublist

    return dp[len(s)]

def wordBreak_another(s, wordDict):
    if len(s) <=1:
        return [s] if s in wordDict else []
    
    parents = defaultdict(list)
    mem = [False for i in range(len(s)+1)]
    mem[0] = True
    wordDict = set(wordDict)
    
    for i in range(len(s)):
        if mem[i]:
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict: 
                    mem[j+1] = True
                    parents[j].append(i)
                    
    def build(k=len(s)-1):
        if k < 0: return [""]
        res = []
        for i in parents[k]:
            u = s[i:k+1]
            if k != len(s)-1:
                u+= " "
            a = build(i-1)
            for x in a:
                res.append(x+u)
        return res
    
    ans = build()       
    return [] if ans == [""] else ans