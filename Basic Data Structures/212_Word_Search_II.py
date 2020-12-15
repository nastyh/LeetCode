def findWords(board, words):
    rows, cols = len(board), len(board[0])
    trie = {}
    for word in words:
        node = trie
        for letter in word:
            node = node.setdefault(letter, {})
        node['$'] = True
    result = []
    def backtrack(i: int, j: int, node = trie, prefix: str = ''):
        letter = board[i][j]
        if letter in node:
            board[i][j] = '#'
            node = node[letter]
            if '$' in node:
                result.append(prefix + letter)
                del node['$']
            for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= r < rows and 0 <= c < cols:
                    backtrack(r, c, node, prefix + letter)
            board[i][j] = letter
    for i in range(rows):
        for j in range(cols):
            backtrack(i, j)
    return result


def findWords_backtracking(board, words):  # O(N * 3^L), N is the number of letters, L length of the longest word
    foundList = list()
    def foundWordAtPos(w, pos):
        j,i = pos
        if board[j][i] == "0" or w[0] != board[j][i]:
            return False
        if len(w) == 1:
            return True
        result = False
        temp = board[j][i]
        board[j][i] = "0" # place a marking
        if j < len(board) - 1 and foundWordAtPos(w[1:],(j + 1,i)):
            result = True
        elif i < len(board[0]) - 1 and foundWordAtPos(w[1:],(j,i + 1)):
            result = True
        elif j > 0 and foundWordAtPos(w[1:],(j - 1,i)):
            result = True
        elif i > 0 and foundWordAtPos(w[1:],(j, i - 1)):
            result = True
        board[j][i] = temp  # remove a marking
        return result
    for a in range(len(board)):
        for b in range(len(board[0])):
            for w in words:
                if foundWordAtPos(w, (a, b)) == True:
                    foundList.append(w)
    return list(set(foundList))