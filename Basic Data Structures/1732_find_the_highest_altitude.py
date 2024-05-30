class Solution:
    def largestAltitude_window(self, gain: List[int]) -> int:
        res, curr_res = 0, 0 
        l= 1
        # process the first one separately
        # 0 + whatever the first element is
        curr_res = 0 + gain[0]
        res = max(res, curr_res) # usual check
        while l < len(gain): # moveing through the list
            # starting with the second element
            curr_res += gain[l] # add it and see what it does
            res = max(res, curr_res)
            l += 1 # move to the right 
        return 
        
    def largestAltitude_another(self, gain: List[int]) -> int:
        curr_res, glob_res = 0, -math.inf
        for g in gain:
            curr_res = curr_res + g
            glob_res = max(curr_res, glob_res)
        return glob_res if glob_res > 0 else 0 # because initialized at -math.inf