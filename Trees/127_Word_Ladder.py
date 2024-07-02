from string import ascii_lowercase
from collections import defaultdict, deque
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord
        Given two words, beginWord and endWord, and a dictionary wordList,
        return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

        BFS
        Need pre-processing: in a word, let's sub every letter with a symbol
        So "dog" can be "*og", "d*g", "do*"
        This way, we know that the words "dog" and "dig" are different by one letter,
        thus, they can be in an adjacency list. 
        Do the pre-processing on the given wordList and find all the possible generic/intermediate states. Save these intermediate states in a dictionary with key as the intermediate word and value as the list of words which have the same intermediate word.
        Push a tuple containing the beginWord and 1 in a queue. The 1 represents the level number of a node. We have to return the level of the endNode as that would represent the shortest sequence/distance from the beginWord.

        To prevent cycles, use a visited dictionary.

        While the queue has elements, get the front element of the queue. Let's call this word as current_word.

        Find all the generic transformations of the current_word and find out if any of these transformations is also a transformation of other words in the word list. This is achieved by checking the all_combo_dict.

        The list of words we get from all_combo_dict are all the words which have a common intermediate state with the current_word. These new set of words will be the adjacent nodes/words to current_word and hence added to the queue.

        Hence, for each word in this list of intermediate words, append (word, level + 1) into the queue where level is the level for the current_word.

        Eventually if you reach the desired word, its level would represent the shortest transformation sequence length.
        O(M^2 * N) where M is the length of each word, and N is the total number of word in the input word list
        Space O(M^2 * N)
        Each word in the list has M intermediate combinations. For each, we need to save the original word M times.
        Visited is O(MN), as well, as the queue
        Overall, M^2 * N takes over
        """
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                # example: '*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'],
                all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )
                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


    def ladderLength_another(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        O(M^2 * N) both 
        """
        # Create a set of words for faster lookup
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # Initialize queue with the beginWord and set of visited words
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
        # Dequeue the word and its level
        word, level = queue.popleft()
        
        # Iterate over each character in the word
        for i in range(len(word)):
            # Iterate over all possible lowercase letters
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # Skip if the character is the same as in the original word
                if c == word[i]:
                    continue
                # Create the new word by replacing the character at index i
                newWord = word[:i] + c + word[i+1:]
                # Check if the new word is in the wordSet and has not been visited before
                if newWord in wordSet and newWord not in visited:
                    # Check if the new word is the endWord
                    if newWord == endWord:
                        return level + 1
                    # Enqueue the new word and its level
                    queue.append((newWord, level + 1))
                    # Add the new word to the set of visited words
                    visited.add(newWord)
    # No transformation sequence exists
    return 0



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
