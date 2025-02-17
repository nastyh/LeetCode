from collections import defaultdict
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        """
        O(n) both
        Dict that is event_index: [all the times associated with this ix]
        Add the first element manually
        Process the rest
        Need to return the index that has the largest value in all the lists 
        If a tie, smallest ix 
        """
        d = defaultdict(list)
        d[events[0][0]].append(events[0][1])
        for i in range(1, len(events)):
            incoming_time = events[i][1] - events[i-1][1]
            d[events[i][0]].append(incoming_time)
        res = max(d, key=lambda k: (max(d[k]), -k))
        return res
    
    def buttonWithLongestTime_another(self, events: List[List[int]]) -> int:
        """
        Same but instead of dragging a list, we only keep
        the largest values for each index
        Slight change in the formula for res
        """
        d = defaultdict(int)
        d[events[0][0]] = events[0][1] # add first one manually
        for i in range(1, len(events)): # process the rest 
            incoming_time = events[i][1] - events[i-1][1]
            d[events[i][0]] = max(d[events[i][0]], incoming_time)
        res = max(d, key=lambda k: (d[k], -k)) 
        return res