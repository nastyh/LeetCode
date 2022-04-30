from collections import Counter
def anadrome(string):
    charCounter = Counter(string) # Make a hash map to count chars
    numOfOdds = 0
    for char, count in charCounter.items():
        if count % 2 != 0:
            numOfOdds += 1 # Count odd
    # If chars are all even, just return 0
    # Else, we need to add chars according to # of odds except just one
    # For example, aabbbc has 2 odd chars, b and c. We need to add 2 (# of odd chars) - 1, b or c once to make it palindrome first and remove the remaining odd to make it anagram.
    return numOfOdds - 1 if numOfOdds > 0 else 0