def validWordSquare(words):
    vert = []
    for i in range(len(words)):
        curr = ''
        for j in range(len(words[i])):
            try:
                curr += ''.join(words[j][i])
            except IndexError:
                return False
        vert.append(curr)
    return vert == words


if __name__ == '__main__':
    print(validWordSquare(['abcd', 'bnrt', 'crmy', 'dtye']))
    print(validWordSquare(['abcd', 'bnrt', 'crm', 'dt']))
    print(validWordSquare(['ball', 'area', 'read', 'lady']))
    print(validWordSquare(['ball', 'asee', 'let', 'lep']))
        