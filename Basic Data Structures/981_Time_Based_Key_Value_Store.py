from collections import defaultdict
import bisect
class TimeMap_bisect:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        sorted_timestamp = self.timemap[key]
        sorted_timestamp.insert( bisect.bisect_right(sorted_timestamp, (timestamp, value)), (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        sorted_timestamp = self.timemap[key]
        index = bisect.bisect_left(sorted_timestamp, (timestamp, ''))
        if index == len(sorted_timestamp):
            return sorted_timestamp[-1][1]
        elif sorted_timestamp[index][0] == timestamp:
            return sorted_timestamp[index][1]
        elif index == 0 and sorted_timestamp[index][0] != timestamp:
            return ''
        else:
            return sorted_timestamp[index - 1][1]

class TimeMap_short:  # O(N) all 
    """
    Store everything in a defaultdict: key: [value, timestamp]
    Then go iterate over d[value] while we haven't arrived to the proper timestamp
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.dic[key]
        ind = len(vals) - 1
        while ind > -1 and vals[ind][0] > timestamp:
            ind -=1
        return "" if ind == -1 else vals[ind][1] 



class TimeMap_short_bin_search:  # TLE 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)   

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def _bin(self, nums, val):
        l, r = 0, len(nums) - 1
        ans = -1
        if r = -1: return r
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == val:
                return m
            elif nums[m] > val:
                r = m - 1
            else:
                l = m + 1
                ans = m
        return ans
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = (l + r + 1) // 2
        #     if nums[m] == val:
        #         return m
        #     elif nums[m] < val:
        #         l = m
        #     else:
        #         r = m - 1
        # return l
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic: return ""
        if len(self.dic[key]) == 0: return self.dic[key][1]
        tuples = self.dic[key]
        vals = []
        for t in tuples:
            vals.append(t[0])
        ix = self._bin(vals, timestamp)
        if timestamp < vals[ix]: return ""
        # if not ix: return ""
        # print(tuples)
        return tuples[ix][1]




class TimeMap:
    def __init__(self):  # O(n) for storarte and then below are time complexities
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:  # O(1)
        if key not in self.hashmap:
            self.hashmap[key] = SortedDict()
        self.hashmap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:  # O(logN)
        if key not in self.hashmap:
            return ''
        sd = self.hashmap[key]
        if timestamp in sd:
            return sd[timestamp]
        if sd.peekitem(0)[0] > timestamp:
            return ''
        return self.binary_search(key, timestamp, sd)
    
    def binary_search(self, key, timestamp, sd):
        left, right = 0, len(sd) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if sd.peekitem(mid)[0] < timestamp:
                left = mid
            else:
                right = mid
        if sd.peekitem(right)[0] < timestamp:
            return sd.peekitem(right)[1]
        return sd.peekitem(left)[1]


if __name__ == '__main__':
    print(_test([10, 20], 5))