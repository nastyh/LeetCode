def toGoatLatin(S):  # O(n) both
    """
    Do what it says.
    Set in order to access vowels faster
    Turn the string into a list with words
    Iterate over words, do operations depending on whether a word starts with a vowel. 
    Careful w/ lower() and upper(). Could've added capital vowels to the set alternatively.
    Than do one more pass adding 'a' depending on the index of the word
    Accurately with indices b/c we need to consider that the first word has an index of 1, not 0
    Finally, combine the list into a string.
    We have one extra space in the beginning that we want to avoid
    """
    vowels = set()
    vowels.add('a')
    vowels.add('e')
    vowels.add('i')
    vowels.add('o')
    vowels.add('u')
    s_list = [i for i in S.split()]
    for i in range(len(s_list)):
        if s_list[i][0].lower() in vowels:
            s_list[i] += 'ma'
        else:
            first_ch = s_list[i][0]
            rest_ch = s_list[i][1:]
            s_list[i] = rest_ch + first_ch + 'ma'
    for k, _ in enumerate(s_list, start = 1):
        s_list[k - 1] += 'a' * k
    res = ''
    for word in s_list:
        res += ' '
        res += word
    """
    We can build res a bit differently:
    res = ''
    res += s_list[0]
    for word in s_list[1:]:
        res += ' '
        res += word
    return res
    """
    return res[1:]