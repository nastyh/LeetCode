from collections import deque
def wordBreak(s, wordDict):  # O(n^3) b/c of two loops and checking if elements in a dictionary. O(n)
    """
    The DP part of the problem can be like this: the substring up to but not including index i satisfies the question. To solve this, we can further divide
    the substring (up to i) into two parts, s[0:j] and s[j:i]. dp[j] provides the answer for s[0:j] and we only need to verify s[j:i] is in wordDict or not.
    If there exists a j that satisfies both requirements, then dp[i] is True.
    """
    wordDict = set(wordDict)
    # a substring [0:i] satisfies the requirement
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in wordDict:
                dp[i] = True
                break
    return dp[-1]


def wordBreak_dp_another(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for ix in range(1, len(s) + 1):
        for word in wordDict:
            if dp[ix - len(word)] and s[:ix].endswith(word):
                dp[ix] = True
    return dp[-1]

def wordBreak_explained(self, s: str, wordDict: List[str]) -> bool:
        """
        O(n^2 * m) and O(n)
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
        """
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        # fill out from the back
        for i in range(len(s) -1, -1, -1):
            # assess each word
            for w in wordDict:
                # if there are enough elements to work with and everything before has already matched
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:  # means the word w from wordDict is found
                    break
        return dp[0]


def wordBreak_bfs(s, wordDict):
    word_set = set(wordDict)
    q = deque()
    visited = set()
    q.append(0)
    while q:
        start = q.popleft()
        if start in visited:
            continue
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set:
                q.append(end)
                if end == len(s):
                    return True
            visited.add(start)
    return False


def wordBreak_alt(s, wordDict):  #w/ recursion
    words = set(wordDict)
    memo = {} 
    def recurse(idx):
        if idx in memo: return memo[idx]
        
        if idx == len(s):
            return True 
        ret = False 
        for i in range(idx, len(s) + 1): 
            if s[idx:i] in words: 
                ret |= recurse(i)  # inplace operation: combination of operation and assignment (think, +=)
        memo[idx] = ret 
        return ret 
    return recurse(0)
    

if __name__ == '__main__':
    print(wordBreak("leetcode",["leet", "code"]))
    print(wordBreak("applepenapple",["apple", "pen"]))
    print(wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))
    print(wordBreak_alt("leetcode",["leet", "code"]))
    print(wordBreak_alt("applepenapple",["apple", "pen"]))
    print(wordBreak_alt("catsandog",["cats", "dog", "sand", "and", "cat"]))
