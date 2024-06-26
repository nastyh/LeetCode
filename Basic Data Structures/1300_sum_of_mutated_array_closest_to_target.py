class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int: # (nlogn(n)) and O(1)
        arr.sort()
        length = len(arr)
        for x in range(length):
            sol = round(target / length)
            if arr[x] >= sol:
                return sol
            target -= arr[x]
            length -= 1
        return arr[-1]