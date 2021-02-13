def reverseVowels(s):  # O(n) both 
    vowels = ['e','u','i','o','a', 'E', 'U', 'I', 'O','A']
    l = list(s)
    i, j = 0, len(l) - 1
    while i < j:
        if l[i] in vowels and l[j] in vowels:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        if l[i] not in vowels:
            i += 1
        if l[j] not in vowels:
            j -= 1
    return ''.join(q for q in l)
    


def reverseVowels_alt(s):
    """
    Two pointers to swap the vowels
    Then need to place consonants back
    Return the result as a string
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l, r = 0, len(s) - 1
    res = [None] * len(s)
    while l <= r:
        if s[l] in vowels and s[r] in vowels:
            res[l], res[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] not in vowels and s[r] in vowels:
            l += 1
        elif s[l] in vowels and s[r] not in vowels:
            r -= 1
        else:
            l += 1
            r -= 1
    for consonant_ix in range(len(s)):
        if s[consonant_ix] not in vowels:
            res[consonant_ix] = s[consonant_ix]
    return ''.join(res)


def reverseVowels_stack(s):
    stack = [i for i in s if i in "aeiouAEIOU"]
    res = []
    for i in s:
        if(i in "aeiouAEIOU"):
            res.append(stack.pop())
        else:
            res.append(i)
    return("".join(res))

