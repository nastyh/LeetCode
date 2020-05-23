def first_non_repeating_string(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    if len(set(s)) == 1:
        return ''

    d = {}

    for el in s.lower():
        if el not in d:
            d[el] = 1
        else:
            d[el] += 1

    nonrep = [k for k,v in d.items() if v == 1]
    if len(nonrep) == 0:
        return ''

    for j in s.lower():
        if j in nonrep:
            return j

if __name__ == '__main__':
    print(first_non_repeating_string('sTreSS'))


# alternative, handles edge cases
string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
    return ""
