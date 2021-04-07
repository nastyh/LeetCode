def halvesAreAlike(s):  # O(n) and O(1)
    """
    Increment res when traversing the left half
    Decrement res when traversting the right half
    """
    res = 0
    for ch in s[:len(s) // 2]:
        if ch in 'aeiouAEIOU':
            res += 1
    for ch in s[len(s) // 2:]:
        if ch in 'aeiouAEIOU':
            res -= 1
    return res == 0


def halvesAreAlike_set(s):  # O(n) both but faster because of the set
    res = 0
    vowels = set()
    for ch in 'aeiouAEIOU':
        vowels.add(ch)
     for ch in s[:len(s) // 2]:
        if ch in vowels:
            res += 1
    for ch in s[len(s) // 2:]:
        if ch in vowels:
            res -= 1
    return res == 0