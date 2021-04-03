def compress(chars):  # O(n) and O(1)
    if len(chars) == 0 : return 0
    c, i = 1, 0
    chars.append(" ")
    while chars[i] != " ":
        if chars[i] == chars[i + 1]:
            c += 1
            i += 1
        else:
            if c > 1:
                chars[i + 2 - c:i + 1] = list(str(c))
                i += 2 - c + len(list(str(c)))
                c = 1
            else:
                i += 1
    del chars[-1]


def compress(chars):
    if not chars: return 0
    curr, count, ind = chars[0], 1, 1
    while ind < len(chars):
        if chars[ind] == curr:
            count += 1
            chars.pop(ind)
        elif chars[ind] != curr:
            if count != 1:
                for i in str(count):
                    chars.insert(ind, i)
                    ind += 1
            curr,count = chars[ind], 1
            ind += 1
    if count > 1:
        for i in str(count):
            chars.append(i)
    return len(chars)