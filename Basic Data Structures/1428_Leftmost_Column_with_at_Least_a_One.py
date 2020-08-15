# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rowscols = binaryMatrix.dimensions()
        ans = rowscols[1]
        for row in range(rowscols[0]):
            l, r = 0, rowscols[1] - 1 
            while l < r:
                m = (r - l) // 2 + l
                if binaryMatrix.get(row, m) == 0:
                    l = m + 1 
                else:
                    r = m 
                if binaryMatrix.get(row, l) == 1:
                    ans = min(ans, l)
        return -1 if ans == rowscols[1] else ans 
