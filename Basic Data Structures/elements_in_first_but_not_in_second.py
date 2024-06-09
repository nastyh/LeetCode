from collections import Counter 
def in_first_not_in_second(s1, s2):
    """
    Return the strings having characters that are not present in another string
    string a - "abcd"
    string b - "ab"
    ans - "cd"
    """
    if len(s1) <= len(s2):
        shorter = s1
        longer = s2
    else:
        shorter = s2
        longer = s1
    d_short, d_long = Counter(shorter), Counter(longer)
    res = ""
    for k in d_long.keys():
        if k not in d_short:
            res += k 
    return res

def in_first_not_in_second_sets(s1, s2):
    if len(s1) <= len(s2):
        shorter = s1
        longer = s2
    else:
        shorter = s2
        longer = s1
    s_short, s_long = set(shorter), set(longer)
    return "".join([ch for ch in s_long if ch not in s_short])


if __name__ == '__main__':
    print(in_first_not_in_second("abcd", "ab"))
    print(in_first_not_in_second_sets("abcd", "ab"))