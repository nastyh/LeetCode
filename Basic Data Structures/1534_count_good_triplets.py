class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        O(n^3) and O(1)
        Given the question constraints, just a brute force will do
        three loops: the left pointer, the pointer to the right, another pointer to the right
        check the requirement, update res 
        """
        res = 0
        for f in range(len(arr) - 2):
            for s in range(f+1, len(arr) - 1):
                for th in range(s+1, len(arr)):
                    if (abs(arr[f]-arr[s]) <= a and abs(arr[s]-arr[th]) <= b and abs(arr[f]-arr[th]) <= c):
                        res += 1
        return res