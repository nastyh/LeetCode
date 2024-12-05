class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        O(n^2) due to to two loops and O(1)
        sort by the x coordinate in a non-decreasing order; break a tie by sorting the y axis
        look at the upper left corner and the lower right corner 
        so i < j and points[i][0] <= points[j][0] and points[i][1] >= points[j][1]
        save the largest y-coordinate that is no larger than points[i][1] when
        looping on j, say the value is m. And if m < points[j][1], the upper-left 
        and lower-right corner pair is valid.
        Track the max y seen so far so we know no previous y will interfere with our current rectangle forming.
        """
        points.sort(key = lambda x: (-x[1], x[0]))
        res = 0
        for i in range(len(points)):
            x = math.inf 
            for j in range(i+1, len(points)):
                if points[j][0] < points[i][0] or x < points[i][0]:
                    continue
                if points[j][0] < x:
                    res += 1
                x = min(points[j][0],x)
        return res