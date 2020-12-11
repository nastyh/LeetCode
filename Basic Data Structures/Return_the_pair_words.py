def return_pairs(l):
    l.sort()
    i = 1
    index=0
    result = []
    while i < len(l):
        if l[i][:len(l[i - 1])] != l[i - 1]:
            result.append(l[index:i])
            index = i
        i += 1
    result.append(l[index:])
    return result