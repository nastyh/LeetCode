def longestWordWithPath(words):
    """
    O(nlong) + O(L) --> O(L), L is the sum of lenghts of all words
    O(n), word_set contains all the words that are buildable 
    allowing character insertions at any position to construct the longest word.
    It also returns the construction path of the longest word, showing the sequence of words used.
    """
    words.sort()  # Sort words lexicographically
    word_set = set()  # To keep track of buildable words
    path = []  # To store the construction path

    for word in words:
        # A word is buildable if any of its prefixes exist in word_set or if it has length 1
        if len(word) == 1 or any(word[:i] in word_set for i in range(1, len(word))):
            word_set.add(word)
            path.append(word)

    return path
