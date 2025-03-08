class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        O(n) to go over blocks
        O(1) nothing to store
        Sliding window
        We need to move the window across blocks and count the number of white 
        the lowest number across all the candidates will be the answer. 
        Means that if we recolor those, we will have all blacks 
        The fact that it should be consecutive doesn't do anything special here 

        Create the initial window of size k
        count whites in it, update res
        process in a loop starting from the right of the end of the window
        if an incoming letter is W, increment the count
        if a letter that is leaving is W, decrement the count 
        keep updating res
        """
        curr_w = sum(1 for b in blocks[:k] if b == 'W')
        res = curr_w
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                curr_w += 1
            if blocks[i-k] == 'W': # accurate with indices, it's the left side of the window 
                curr_w -= 1
            res = min(res, curr_w)
        return res