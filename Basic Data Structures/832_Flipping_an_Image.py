def flipAndInvertImage(A):
    """
    Intuitive:
    first flip b appending the row in an opposite order
    Then go through every element and if it's 1, write 0 and vice versa
    """
    if len(A) == 0: return []
    flipped = []
    for row in A:
        flipped.append(row[::-1])
    invert = []
    for row in flipped:
        curr = []
        for element in row:
            if element == 1:
                curr.append(0)
            else:
                curr.append(1)
        invert.append(curr)
    return invert


def flipAndInvertImage_alt(A):
    result = []
    for row in A:
        result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
    return result