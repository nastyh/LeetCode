class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def get_rootNode(self):
        return self.rootNode
    
    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        currNode = self.rootNode
        for idx, ch in enumerate(word):
            if( ch not in currNode.children ):
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]        
        currNode.endOfWord = True

def findWords_trie(board, words):  # (M(4x3^(L-1))) (M is the number of cells in the board and L is the maximum length of words.) and O(N)
    def dfs(i, j, curr, currNode):
        ch = board[i][j]
        if( ch not in currNode.children or (i, j) in visited ):
            return
        if currNode.children[ch].endOfWord:
            res.add(curr)
            # return                            # edge case
        visited.add((i,j))
        for x,y in directions:
            if 0 <= i + x < m and 0 <= j + y < n:
                dfs( i + x, j + y, curr + board[i + x][j + y], currNode.children[ch])
        visited.remove((i,j))   # edge case
    # buid trie data structure
    my_trie = Trie()
    [ my_trie.insert(word) for word in words ]
    rootNode = my_trie.get_rootNode()
    m, n = len(board), len(board[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    res = set()                     
    for i in range(len(board)):
        for j in range(len(board[i])):
            visited = set()
            dfs(i, j, board[i][j], rootNode)
    return res


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