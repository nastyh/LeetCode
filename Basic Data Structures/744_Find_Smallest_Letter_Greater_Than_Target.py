def nextGreatestLetter(letters, target):
    return next((letter for letter in letters if target < letter), letters[0])


def nextGreatestLetter_binary_search(letters, target):  # O(logN) and O(1)
    """
    Essentially we want to find something bigger than target in a sorted array
    """
    left = 0
    right = len(letters) - 1
    res = letters[0]
    while left <= right:
        mid = left + (right - left) // 2  
        if letters[mid] == target:
            left = mid + 1 
        elif letters[mid] < target:
            left = mid + 1
        elif letters[mid] > target:
            res = letters[mid]
            right = mid - 1
    return res


def nextGreatestLetter_brute_force(letters, target):  # O(n) and O(1) b/c set(letters) is only 26
    alphabet = string.ascii_lowercase
    target_ix = alphabet.index(target)
    for ch_ix in range(target_ix + 1, len(alphabet)):
        if alphabet[ch_ix] in set(letters):
            return alphabet[ch_ix]
    return letters[0]