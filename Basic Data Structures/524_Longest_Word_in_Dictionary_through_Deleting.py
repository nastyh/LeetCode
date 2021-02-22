from collections import defaultdict
def findLongestWord(s, d):  # O(nk) and O(n) where n is the words, nk total number of characters in d
    buckets = defaultdict(list)
    for eachWord in d:
        wordIterator = iter(eachWord)
        nextCharToConsume = next(wordIterator)
        buckets[nextCharToConsume].append((wordIterator, eachWord))
    maxLengthStringConsumed = ""
    for eachChar in s:
        charBucket = buckets[eachChar]
        buckets[eachChar] = []
        while charBucket:
            eachWordIterator, eachWord = charBucket.pop()
            nextCharToConsume = next(eachWordIterator, None)
            if nextCharToConsume is not None:
                buckets[nextCharToConsume].append((eachWordIterator, eachWord))
            else:
                if len(eachWord) > len(maxLengthStringConsumed):
                    maxLengthStringConsumed = eachWord
                elif len(eachWord) == len(maxLengthStringConsumed) and eachWord < maxLengthStringConsumed:
                    maxLengthStringConsumed = eachWord
    return maxLengthStringConsumed
 


if __name__ == '__main__':
    print(findLongestWord('abpcplea', ["ale","apple","monkey","plea"]))
    print(findLongestWord('abpcplea', ['a', 'b', 'c']))