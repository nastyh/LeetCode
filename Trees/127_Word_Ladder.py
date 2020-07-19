from string import ascii_lowercase
from collections import defaultdict, deque
def ladderLength(beginWord, endWord, wordList):
    if beginWord in wordList and endWord in wordList: return 0
    if endWord not in wordList: return 0
    if len(wordList) == 0: return 0
        # d = defaultdict(list)
        # for i in range(len(beginWord)):
        #     element = beginWord[:i] + '_' + beginWord[i + 1:]
        #     for c in ascii_lowercase:
        #         d[element].append(beginWord[:i] + c + beginWord[i + 1:])
        # return d
    wordList.append(beginWord)
    graph = defaultdict(list)
    for w in wordList:  # for every word
        for i in range(len(beginWord)):  # for every position in this word
            for c in ascii_lowercase:  # take every letter from a to z
                if w[i] != c:  # sanity check to exclude duplicates
                    newWord = w[:i] + c + w[i + 1:]  # remove a letter at a given index, insert a letter from a-z instead
                    if newWord in wordList:  # if this word is in wordList, add it to the graph
                        graph[w].append(newWord)
                        graph[newWord].append(w)
    q, visited = deque([beginWord]), set()
    visited.add(beginWord)
    path = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node == endWord:
                return path
        for neighbor in graph[node]: # going through the values of a given node in a dictionary
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
        path += 1
    return 0

if __name__ == '__main__':
    print(ladderLength('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"]))
    print(ladderLength('hot','dog',["hot", "dog"]))
    print(ladderLength('a','c',['a', 'b', 'c']))
