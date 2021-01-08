def arrayStringsAreEqual(word1, word2):  # O(n) both
    s1, s2 = '', ''
    s1 = ''.join(w for w in word1)
    s2 = ''.join(w for w in word2)
    return s1 == s2


def arrayStringsAreEqual_splitting(word1, word2):  # O(n) both
    l1, l2 = [], []
    for element in word1:
        for ch in element:
            l1.append(ch)
    for element in word2:
        for ch in element:
            l2.append(ch)
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True 


def arrayStringsAreEqual_connecting(word1, word2):  # O(n) both
    string_index = 0
    character_Index = 0
    word2_len = len(word2)
    words2_len_list = [len(s) for s in word2]
    for s in word1:
        for c in s:
            if string_index >= word2_len or c != word2[string_index][character_Index]:
                return False
            character_Index += 1
            if character_Index == words2_len_list[string_index]:
                string_index += 1
                character_Index = 0
    if string_index < word2_len:
        return False
    return True


def arrayStringsAreEqual_no_extra_space(word1, word2):  # O(n) and O(1)
    n1, n2 = len(word1), len(word2)
    str_inx_1, char_inx_1, str_inx_2, char_inx_2 = 0, 0, 0, 0
    while str_inx_1 < n1 and str_inx_2 < n2:
        if word1[str_inx_1][char_inx_1] != word2[str_inx_2][char_inx_2]:
            return False
        char_inx_1, char_inx_2 = char_inx_1+1, char_inx_2+1
        if char_inx_1 >= len(word1[str_inx_1]):
            char_inx_1, str_inx_1 = 0, str_inx_1+1
        if char_inx_2 >= len(word2[str_inx_2]):
            char_inx_2, str_inx_2 = 0, str_inx_2+1
    if str_inx_1 < n1 or str_inx_2 < n2:
        return False
    return True