class Solution:
    def maxCount_linear(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        O(n) both prob due to the set 
        Just go one by one and build the current sum
        If the element isn't banned and the potential running sum is still under maxSum,
        we can build the answer 
        """
        s = set()
        res, curr_sum = 0, 0
        for b in banned:
            s.add(b)
        
        for num in range(1, n + 1):
            if num not in s and maxSum >= curr_sum + num:
                res += 1
                curr_sum += num 
        return res

    def maxCount_binary_search(self, banned: List[int], n: int, maxSum: int) -> int:
        """
        O((m+n)logm)
        O(m)
        m elements runs n times 
        Sort banned 
        for each number check if the curr number matches something from the banned list 
        """
        def _helper(target):
            l, r = 0, len(banned) - 1
            while l <= r:
                m = l + (r -l) // 2
                if banned[m] == target:
                    return True 
                elif target < banned[m]:
                    r = m - 1
                else:
                    l = m + 1
            return False
        banned = sorted(banned) 
        res, curr_sum = 0, 0 
        for num in range(1, n + 1):
            if _helper(num):
                continue
            if curr_sum + num <= maxSum:
                curr_sum += num
                res += 1
            else: 
                return res
        return res 
