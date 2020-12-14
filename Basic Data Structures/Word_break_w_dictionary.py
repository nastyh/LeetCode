def word_break(word, map):
    if len(word) == 0:  # base case
        return True
    i = 1
    while i <= len(word):
        #  we divide the current word in 2: from 0...i and i...end. Check that the first half is in the map AND it has frequency available
        if word[:i] in map and map[word[:i]] > 0:
            map[word[:i]] -= 1  # reduce the frequency and try again with the second half of the word (word break)
            if word_break(word[i:], map):
                return True
            map[word[:i]] += 1  # if it wasn't possible, update frequency and keep with the loop, trying with a different word break
        i += 1
    return False