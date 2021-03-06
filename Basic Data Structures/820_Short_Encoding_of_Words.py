 from collections import defaultdict
 def minimumLengthEncoding(words):  # O(w^2) and O(w), where w is the lengths of all words
    good = set(words)
    for word in words:
        for k in range(1, len(word)):
            good.discard(word[k:])
    return sum(len(word) + 1 for word in good)


def minimumLengthEncoding_trie(words):  # O(w) both
    words = list(set(words)) #remove duplicates
    #Trie is a nested dictionary with nodes created
    # when fetched entries are missing
    Trie = lambda: defaultdict(Trie)
    trie = Trie()
    #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
    nodes = [reduce(dict.__getitem__, word[::-1], trie)
                for word in words]
    #Add word to the answer if it's node has no neighbors
    return sum(len(word) + 1
                for i, word in enumerate(words)
                if len(nodes[i]) == 0)



def minimumLengthEncoding_sort(words): # O(wlogw) both
    words = sorted([ word[::-1] for word in words])[::-1]
    length = 0
    wordsNum = len(words)
    wordsIdx = 0
    while(wordsIdx < wordsNum):
        word = words[wordsIdx]
        while(wordsIdx + 1 < wordsNum):
            if not word.startswith(words[wordsIdx + 1]):
                break
            wordsIdx += 1
        length += len(word) + 1
        wordsIdx += 1
    return length