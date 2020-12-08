def longestWord(words):  # brute force
    ans = ""
    wordset = set(words)
    for word in words:
        if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            if all(word[:k] in wordset for k in range(1, len(word))):
                ans = word
    return ans


def longestWord_another(words):  # another brute force  O(w^2) where w is the number of words
    wordset = set(words)
    words.sort(key = lambda c: (-len(c), c))
    for word in words:
        if all(word[:k] in wordset for k in xrange(1, len(word))):
            return word
    return ""


def longestWord_dfs(words):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        reduce(dict.__getitem__, word, trie)[END] = i

    stack = trie.values()
    ans = ""
    while stack:
        cur = stack.pop()
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans