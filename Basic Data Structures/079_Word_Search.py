from collections import deque
def exist(board, word):  # o(N * 3^L), N - num of cells, L, length of the word; O(L)
    def dfs(word, i, j, match_idx, directions, board, visited):
        if match_idx == len(word) - 1:
            return True
        # try all four directions
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            # if within the board, never visited, and matches the current char, keep matching the next char
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] == False and board[x][y] == word[match_idx + 1]:
                visited[x][y] = True
                if dfs(word, x, y, match_idx + 1, directions, board, visited):
                    return True
                visited[x][y] = False
    m = len(board)
    n = len(board[0])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    visited = [[False for _ in range(n)] for _ in range(m)]
    # find the starting char
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited[i][j] = True
                match_idx = 0
                if dfs(word, i, j, match_idx, directions, board, visited):
                    return True
                visited[i][j] = False
    return False

def exist_another(self, board: List[List[str]], word: str) -> bool:
    seen = set()
    # if word is longer than the whole board, it's a no
    if len(word) > len(board)*len(board[0]): return False
    # if there are more specific letters in word than in board, it's a no
    d_word = {} # counts of letters from word
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] not in d_word:
                d_word[board[r][c]] = 1
            else:
                d_word[board[r][c]] += 1
    # go over board, make sure we have enough letters to meet the requirements of word
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] not in d_word: continue # ch in board but not in word, it's ok to pass 
            if d_word[board[r][c]] < 0: 
                return False  
            d_word[board[r][c]] -= 1
    def _helper(word_position, i, j):
        """
        first, check the borders
        """
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[word_position] or (i, j) in seen:
            return False 
        # arrived to the solution
        if word_position == len(word) - 1:
            return True 
        found = False
        seen.add((i, j)) # so that we don't process the same cells 
        # Search upward
        found = found or _helper(word_position + 1, i-1, j)
        # Search rightward
        found = found or _helper(word_position + 1, i, j+1)
        # Search downward
        found = found or _helper(word_position + 1, i+1, j)
        # Search Leftward
        found = found or _helper(word_position + 1, i, j-1)
        seen.remove((i, j)) # nothing found, return the cell to the current state
        return found
    # go cell by cell 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if _helper(0, i, j):
                    return True
    return False

def exist_clean(self, board: List[List[str]], word: str) -> bool:
        """
        O(rows * cols * 4^length of word)
        Space is O(rows * cols)
        """
        seen, rows, cols = set(), len(board), len(board[0])
        # edge cases 
        if len(word) > rows * cols: return False
        # False if the count of any letter in the word > the frequency of this letter on the board
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        # # Start the search from lower frequency of characters     
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        def _helper(word_position, i, j):
            # don't fall out the bounds:
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_position] or (i, j) in seen:
                    return False
            if word_position == len(word) - 1:
                    return True
            found = False
            seen.add((i, j))
            # Search upward
            found = found or _helper(word_position + 1, i-1, j)
            # Search rightward
            found = found or _helper(word_position + 1, i, j+1)
            # Search downward
            found = found or _helper(word_position + 1, i+1, j)
            # Search Leftward
            found = found or _helper(word_position + 1, i, j-1)
            seen.remove((i, j))
            return found
        # call the helper on each cell 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if _helper(0, i, j):
                        return True
        return False

def exist_dfs(board, word):
    if not board:
        return False
    h, w = len(board), len(board[0])
    def dfs_search(idx, x, y):
        if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
            # Reject if out of boundary, or current grid cannot match the character word[idx]
            return False
        if idx == len(word) - 1: 
            # Accept when we match all characters of word during DFS
            return True
        cur = board[y][x]
        # mark as '#' to avoid repeated traversal
        board[y][x] = '#'
        # visit next four neighbor grids
        found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
        # recover original grid character after DFS is completed
        board[y][x] = cur
        return found
    return any(dfs_search(0, x, y) for y in range(h) for x in range(w))      


if __name__ == '__main__':  
    print(exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'ABCCED'))
    print(exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'SEE'))
    print(exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'ABCB'))
    print(exist([['a', 'b'], ['c', 'd']], 'abcd'))
