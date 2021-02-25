def palindromePairs(words):  # O(k^2 * n) building hashtables O(nk) and each word is O(k) to insert and there are n words. Space: O((k + n)^2) 
    def all_valid_prefixes(word):
        valid_prefixes = []
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                valid_prefixes.append(word[:i])
        return valid_prefixes

    def all_valid_suffixes(word):
        valid_suffixes = []
        for i in range(len(word)):
            if word[:i+1] == word[:i+1][::-1]:
                valid_suffixes.append(word[i + 1:])
        return valid_suffixes
    word_lookup = {word: i for i, word in enumerate(words)}
    solutions = []
    for word_index, word in enumerate(words):
        reversed_word = word[::-1]
        # Build solutions of case #1. This word will be word 1.
        if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
            solutions.append([word_index, word_lookup[reversed_word]])
        # Build solutions of case #2. This word will be word 2.
        for suffix in all_valid_suffixes(word):
            reversed_suffix = suffix[::-1]
            if reversed_suffix in word_lookup:
                solutions.append([word_lookup[reversed_suffix], word_index])
        # Build solutions of case #3. This word will be word 1.
        for prefix in all_valid_prefixes(word):
            reversed_prefix = prefix[::-1]
            if reversed_prefix in word_lookup:
                solutions.append([word_index, word_lookup[reversed_prefix]])
    return solutions


class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []

def palindromePairs_trie(words):  # O(k^2 * n) and O((k + n)^2)
     trie = TrieNode()
    for i, word in enumerate(words):
        word = word[::-1] # We want to insert the reverse.
        current_level = trie
        for j, c in enumerate(word):
            # Check if remainder of word is a palindrome.
            if word[j:] == word[j:][::-1]:# Is the word the same as its reverse?
                current_level.palindrome_suffixes.append(i)
            # Move down the trie.
            current_level = current_level.next[c]
        current_level.ending_word = i

    # Look up each word in the Trie and find palindrome pairs.
    solutions = []
    for i, word in enumerate(words):
        current_level = trie
        for j, c in enumerate(word):
            # Check for case 3.
            if current_level.ending_word != -1:
                if word[j:] == word[j:][::-1]: # Is the word the same as its reverse?
                    solutions.append([i, current_level.ending_word])
            if c not in current_level.next:
                break
            current_level = current_level.next[c]
        else: # Case 1 and 2 only come up if whole word was iterated.
            # Check for case 1.
            if current_level.ending_word != -1 and current_level.ending_word != i:
                solutions.append([i, current_level.ending_word])
            # Check for case 2.
            for j in current_level.palindrome_suffixes:
                solutions.append([i, j])
    return solutions


def palindromePairs_greedy(words):  # O(k^2 * n), k is prefix and O((k + n)^2)
     def isPalindrome(s):
        start = 0
        end = len(s) - 1
        while( start < end ):
            if( s[ start ] != s[ end ] ):
                return False
            start += 1
            end -= 1
        return True
    results = set()
    reversedWords = {word[::-1]: index for index, word in enumerate(words)}
 i, word in enumerate(words):
        for j in range(0,len(word) + 1):
            prefix = word[:j]
            pfremain = word[j:]
            if prefix in reversedWords and isPalindrome(pfremain) and reversedWords[prefix] != i:
                results.add((i,reversedWords[prefix]))
        for j in range(len(word), -1, -1):
            suffix = word[j:]
            sfremain = word[:j]
            if suffix in reversedWords and isPalindrome(sfremain) and reversedWords[suffix] != i:
                results.add((reversedWords[suffix], i))
    return results