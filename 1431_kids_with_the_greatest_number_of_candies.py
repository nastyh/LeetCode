class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:  # O(n) to run and probably store; or O(1) to store 
        # find the max val in candies
        # if current element + extraCandies >= this max val, this is True
        res = [False] * len(candies)
        max_val = max(candies)
        for ix in range(len(candies)):
            if candies[ix] + extraCandies >= max_val:
                res[ix] = True
        return res