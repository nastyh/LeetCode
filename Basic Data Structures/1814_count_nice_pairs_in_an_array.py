class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        """
        O(n) both 
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        if diff(x) = x - rev(x)
        then a pair (i, j) is nice if diff(nums[i]) equals diff(nums[j]). 
        count the frequency of each diff value and then add up the number of pairs within each group (using the formula n*(n-1)/2).
        """
        mod = 10**9 + 7
        freq = {}
        count = 0
        
        for num in nums:
            # Compute the reverse of num.
            rev_num = int(str(num)[::-1])
            # Calculate the difference.
            diff = num - rev_num
            
            # If diff has been seen before, each occurrence forms a nice pair with the current number.
            if diff in freq:
                count = (count + freq[diff]) % mod
                freq[diff] += 1
            else:
                freq[diff] = 1
                
        return count

# Example usage:
sol = Solution()
print(sol.countNicePairs([42,11,1,97]))  # Expected output: 2
print(sol.countNicePairs([13,10,35,24,76]))  # Expected output: 4
