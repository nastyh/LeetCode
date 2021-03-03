from collections import Counter
def wordBreak(s, wordDict):  # O(N^2 + 2^N + W) where N the length of the input string, W is the number of words in the dictionary 
    # quick check on the characters,
    #   otherwise it would exceed the time limit for certain test cases.
    if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
        return []
    wordSet = set(wordDict)
    dp = [[]] * (len(s) + 1)
    dp[0] = [""]
    for endIndex in range(1, len(s) + 1):
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
    if len(s) <= 1:
        return [s] if s in wordDict else []
    
    parents = defaultdict(list)
    mem = [False for i in range(len(s) + 1)]
    mem[0] = True
    wordDict = set(wordDict)
    
    for i in range(len(s)):
        if mem[i]:
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict: 
                    mem[j + 1] = True
                    parents[j].append(i)
                    
    def build(k = len(s) - 1):
        if k < 0: return [""]
        res = []
        for i in parents[k]:
            u = s[i:k + 1]
            if k != len(s) - 1:
                u += " "
            a = build(i - 1)
            for x in a:
                res.append(x + u)
        return res
    ans = build()       
    return [] if ans == [""] else ans


def wordBreak_more(s, wordDict):
    cache = {}
    def wordbr(s):
        if s not in cache: 
            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(s) == len(w):
                        result.append(w)
                    else:
                        for word in wordbr(s[len(w):]):
                            result.append(w + " " + word)
            cache[s] = result
        return cache[s]
    return wordbr(s)


def wordBreak_trie(s, wordDict):
    all_results = []
    trie = {}
    s_letters, words_letters = set(s), set()
    # Build a trie from the words in word dictionary
    for word in wordDict:
        node = trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
            words_letters.add(letter)
        node[None] = word
    # Check if all letters of the S string are in the words' letters
    if s_letters - words_letters:
        return []
    # BFS
    # Each element in the queue is the S-string index (current parsing position) and
    # an array with the found words so far
    queue = collections.deque([(0, [])])
    while queue:
        idx, result = queue.pop()
        # If index has reached the end of the S string, then we have found one of the
        # results
        if idx == len(s):
            all_results.appendleft(" ".join(result))
            continue
        # Go through the trie until a word is found
        node = trie
        while idx < len(s) and s[idx] in node:
            node = node[s[idx]]
            idx = idx + 1
            if None in node:
                queue.append((idx, result + [node[None]]))
    return all_results
