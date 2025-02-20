from collections import Counter
def canConstruct(ransomNote, magazine):  # O(m) where m is the length of magazine.  Space O(k) or O(1). k is the number of chars in the dict
    """
    At worst, the time complexity is O(n) + O(n) + O(m). m >> n, thus, O(m)
    Iterate over ransomNote and check if we 
    have this letter in the magazine dictionary
    If no, return False
    If yes: if the value is zero, return False. If > 0, decrement
    At the end, check that all values in the dictionary are non-negative
    """
    d_magazine = Counter(magazine)
    for ch in ransomNote:
        if ch not in d_magazine:
            return False
        else:
            if d_magazine[ch] == 0:
                return False
            else:
                d_magazine[ch] -= 1
    # return all(v for v in d_magazine.values()) >= 0
    return sum([v for v in d_magazine.values()]) >= 0


def canConstruct_two_dicts(ransomNote, magazine):
    """
    Just compare dictionaries' values
    """
     d_mag, d_note = Counter(magazine), Counter(ransomNote)
        for k, v in d_note.items():
            if k not in d_mag: return False
            if d_mag[k] < d_note[k]: return False
        return True


def canConstruct_sorting(ransomNote, magazine):  # O(mlogm) and O(m)
    if len(ransomNote) > len(magazine): return False
    # Reverse sort the note and magazine. In Python, we simply 
    # treat a list as a stack.
    ransomNote = sorted(ransomNote, reverse = True) 
    magazine = sorted(magazine, reverse = True)
    # While there are letters left on both stacks:
    while ransomNote and magazine:
        # If the tops are the same, pop both because we have found a match.
        if ransomNote[-1] == magazine[-1]:
            ransomNote.pop()
            magazine.pop()
        # If magazine's top is earlier in the alphabet, we should remove that 
        # character of magazine as we definitely won't need that letter.
        elif magazine[-1] < ransomNote[-1]:
            magazine.pop()
        # Otherwise, it's impossible for top of ransomNote to be in magazine.
        else:
            return False   
    # Return true iff the entire ransomNote was built.
    return not ransomNote
