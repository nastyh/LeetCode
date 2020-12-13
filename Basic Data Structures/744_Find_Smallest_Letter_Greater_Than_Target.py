def nextGreatestLetter(letters, target):
    return next((letter for letter in letters if target < letter), letters[0])


def nextGreatestLetter_binary_search(letters, target):
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