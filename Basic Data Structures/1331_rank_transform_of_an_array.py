class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        O(nlogn) sorting
        O(n)
        iterate, if the same number, increment repeated
        Build dict as d[element] = ix - repeated
        Build the res 
        """
        if len(arr) == 0: return []
        arr_sorted = sorted(arr)
        d, res, repeated = {arr_sorted[0]: 0}, [], 0
        for ix in range(1, len(arr_sorted)):
            if arr_sorted[ix-1] == arr_sorted[ix]:
                repeated += 1
            else:
                d[arr_sorted[ix]] = ix - repeated 
        for num in arr:
            res.append(d[num] + 1)
        return res


        