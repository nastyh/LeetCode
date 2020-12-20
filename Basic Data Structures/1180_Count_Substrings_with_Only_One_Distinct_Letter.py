def countLetters(S):  # O(n) and O(1)
    """
    Initialize an integer variable total to count the number of substrings along with the iteration
    initialize two pointers left and right which mark the beginning and the end of the substring that contains only one distinct letter.
    Iterate through S:
    If we do not reach the end and the new character S[right] is the same as the beginning one S[left], increment right by 1 to keep exploring S;
    otherwise, calculate the length of the substring as right - left and apply the Sum Equation of Arithmetic Sequence; remember to set right as left to start exploring the new substring.
    """
    total = left = 0
    for right in range(len(S) + 1):
        if right == len(S) or S[left] != S[right]:
            len_substring = right - left

            total += (1 + len_substring) * len_substring // 2
            left = right
    return total


def countLetters_dp(S):  # O(n) and O(n)
    """
    if the previous letter is the same, increment the counter
    If it's different, put counter to one
    """
    total = 1
    substrings = [0] * len(S)
    substrings[0] = 1
    for i in range(1, len(S)):
        if S[i - 1] == S[i]:
            substrings[i] = substrings[i-1] + 1
        else:
            substrings[i] = 1
        total += substrings[i]
    return total


def countLetters_dp_optimized(S):  # O(n) and O(1)
    """
    Improvement over the previous one, as we only need to know the value of the last one
    don't need to maintain the whole array
    """
    res, curr = 1, 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            curr += 1
            res += curr
        else:
            curr = 1
            res += curr
    return res