from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Worst case is all permutations
        P(n, i) = n! / (n - i)!, i -- num of tiles considered at this moment
        O(n) for the recursive stack
        """
        d, res = Counter(tiles), 0
        def _helper():
            nonlocal res
            for letter in d:
                if d[letter] > 0:
                    res += 1
                    d[letter] -= 1
                    _helper()
                    d[letter] += 1
        _helper()
        return res
    
    def numTilePossibilities_like_permutations(self, tiles: str) -> int:
        """
        Same as above
        Sort to tackle the same letters 
        used to keep track which titles have been included in the current sequence 
        In recursive calls:
        add non-empty seq into res
        iterate over all tiles, if not used, use it and continue the recursion
        backtrack by removing the last tile and marking it as unused 
        """
        tiles = sorted(tiles)
        res = set()
        used = [False] * len(tiles)

        def _helper(path):
            if path:
                res.add("".join(path))
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i-1] and not used[i-1]:
                    continue
                used[i] = True 
                path.append(tiles[i])
                _helper(path)
                path.pop()
                used[i] = False 
        _helper([])
        return len(res)