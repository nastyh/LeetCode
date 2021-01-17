def numTilePossibilities(tiles):  # O(n!) both
    seqs = set()
    visits = [False] * len(tiles)
    def dfs(seq, depth):
        if seq:
            seqs.add(seq)
        if depth == len(tiles) - 1:
            return
        for i in range(len(tiles)):
            if not visits[i]:
                visits[i] = True
                dfs(seq + tiles[i], depth + 1)
                visits[i] = False
    dfs('', -1)
    return len(seqs)