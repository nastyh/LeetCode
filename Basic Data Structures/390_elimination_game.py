class Solution:
    def lastRemaining(self, n: int) -> int:  # O(logn) and O(1)
        # keep tracking the first element
        # if from_left is True or the number of elements in the list is odd,
        # we need to update the first element
        # gap is the space between the first and the second elements 
        # n is the number of elements in the list 
        from_left = True
        res, gap = 1, 1
        while n > 1:
            if from_left or n % 2:
                res += gap
            gap *= 2
            n //= 2
            from_left = not from_left
        return res