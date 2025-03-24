from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        O(nlogn) for sorting
        O(n) for merged 
        Sort by the start time
        First create a merged list 
        two intervals overlap, take min start and max end
        Count gaps
        First gap (if before the first meeting): this gap is merged[0][0] - 1
        Between the meetings: for two consecutive intervals, the gap is merged[i][0] - merged[i-1][1] - 1
        After the last meeting: the gap is days - merged[-1][1]
        """
        meetings.sort(key = lambda x: x[0])
        res = 0
        merged = [meetings[0]]
        for ix in range(1, len(meetings)):
            if merged[-1][1] >= meetings[ix][0]:
                merged[-1][1] = max(merged[-1][1], meetings[ix][1])
            else:
                merged.append(meetings[ix])

        res += merged[0][0] - 1
        for ix in range(1, len(merged)):
            res += merged[ix][0] - merged[ix-1][1] - 1
        res += days - merged[-1][1]
        return res