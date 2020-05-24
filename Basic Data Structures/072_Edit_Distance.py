class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) > len(word1):
            return self.minDistance(word2, word1)
        evenRow = [i for i in range(len(word2) + 1)]
        oddRow = [0 for i in range(len(word2) + 1)]
        currentRow = evenRow
        for i in range(1, len(word1) + 1):
            if (i % 2) == 0:
                currentRow = evenRow
                prevRow = oddRow
            else:
                currentRow = oddRow
                prevRow = evenRow
            for j in range(len(word2) + 1):
                if j == 0:
                    currentRow[0] = prevRow[0] + 1
                elif word1[i - 1] == word2[j - 1]:
                    currentRow[j] = prevRow[j - 1]
                else:
                    currentRow[j] = min(currentRow[j - 1], prevRow[j], prevRow[j - 1]) + 1
        return currentRow[-1]
