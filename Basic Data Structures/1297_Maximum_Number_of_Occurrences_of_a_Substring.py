from collections import Counter
def maxFreq(s, maxLetters, minSize, maxSize):
    count = collections.Counter()
    # Check only for minSize
    for i in range(len(s) - minSize + 1):
        t = s[i:i + minSize]
        if len(set(t)) <= maxLetters:
            count[t] += 1
    return max(count.values()) if count else 0


def maxFreq_another(s, maxLetters, minSize, maxSize):  # O(n * 26) and O(n)
    """
    Every valid substring of length minSize has to occur at least as often as any substring with the same prefix and a higher length. Therefore maxSize can be ignored.
    You just need to count the occurence of every valid substring of length minSize and return the maximum count.
    """
    n = len(s)
    substringCount = collections.defaultdict(int)
    
    for index in range(n - minSize + 1):
        substring = s[index:index + minSize]
        
        if len(set(substring)) <= maxLetters:
            substringCount[substring] += 1
    return max(substringCount.values(), default = 0)


def maxFreq_long(s, maxLetters, minSize, maxSize):  # O(N) both 
    n = len(s)
    modVal = 10**9 + 7
    hashCount = collections.defaultdict(int)
    letterCount = collections.defaultdict(int)
    uniqueLetters = set()
    hashCode = 0    
    for index in range(n):
        addLetter = s[index]
        letterCount[addLetter] += 1
        uniqueLetters.add(addLetter)
        hashCode = (hashCode * 26 + ord(addLetter) - 97) % modVal
        if index + 1 < minSize:
            continue
        if len(uniqueLetters) <= maxLetters:
            hashCount[hashCode] += 1
        removeLetter = s[index - minSize + 1]
        hashCode -= ((ord(removeLetter) - 97) * (26 ** (minSize - 1))) % modVal
        letterCount[removeLetter] -= 1
        if not letterCount[removeLetter]:
            uniqueLetters.remove(removeLetter)
    return max(hashCount.values(), default = 0)
