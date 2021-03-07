def canPartitionKSubsets(nums, k):  # O(4^n)
    def dfs(parts, nums, idx):
    if idx == len(nums):
        return not sum(parts)
    for i in range(len(parts)):
        if parts[i] >= nums[idx]:
            parts[i] -= nums[idx]
            if dfs(parts, nums, idx+1):
                return True
            parts[i] += nums[idx]

    if not nums or int(sum(nums)/k) != sum(nums) / k:
        return False
    nums.sort(reverse = True)
    parts = [sum(nums) / k] * k
    return dfs(parts, nums, 0)


def canPartitionKSubsets_alt(nums, k):
    def dfs(nums, idx, targets):
        if idx == len(nums):
            return True
         for i, v in enumerate(targets):
            if nums[idx] <= v:
                targets[i] -= nums[idx]
                if dfs(nums, idx + 1, targets):
                    return True
                targets[i] += nums[idx]
    target = sum(nums)
    if target % k:
        return False
    targets = [target // k for _ in range(k)]
    nums.sort(reverse = True)
    return dfs(nums, 0, targets)


def canPartitionKSubsets_recur(nums, k):  #  O(k * 2^n) since we do 2^n(worst case) for k subsets
   def recur(nums, curr_sum, curr_ind, t_sum, k):
        if curr_sum == t_sum:
            # resetting the variables for the new subset
            k -= 1
            curr_sum = 0
            curr_ind = 0
        if not k:
            # terminal condition
            ans = True
            return 
        # check if no answer is found yet
        if not ans and curr_ind < len(nums):
            # select only indexes which have not been selected for other indices
            if nums[curr_ind] != -1:
                if curr_sum + nums[curr_ind] <= t_sum:
                    val = nums[curr_ind]
                    nums[curr_ind] = -1
                    recur(nums, curr_sum + val, curr_ind + 1, t_sum, k)
                    nums[curr_ind] = val
            # choice to leave the element out of the current subset 
            recur(nums, curr_sum, curr_ind + 1, t_sum, k)
    t_sum = sum(nums)
    if t_sum % k:
        return False
    ans = False
    recur(nums, 0, 0, t_sum // k, k)
    return ans


def canPartitionKSubsets_bitmask(nums, k): # O(N * 2^N)
    """
    Edge case if sum cannot be divided evenly in 4 parts
    Sort to improve the running time
    If mask == 0, all elements have been used, check if cur == 0.
    If cur is 0 while mask isn't zero, we found an equal subset. But we need to keep going till k subsets are found
    """
    if not nums or int(sum(nums)/k) != sum(nums)/k: return False 
    N = len(nums)
    nums.sort(reverse = True) 
    
    def dp(mask, cur, memo): # Top-down DP with memoization
        if mask == 0:
            return cur == 0 #[3]
        elif cur == 0:
            return dp(mask, sum(nums)/k, memo) 
        if (mask, cur) not in memo:
            res = False
            for bit in range(N): 
                if mask & (1 << bit):  # check whether the number is unused 
                    if nums[bit] > cur: continue # Writing this to be more explicit, for easy-understanding
                    if dp(mask ^ (1 << bit), cur - nums[bit], memo): # turning from unused to used 
                        res = True
                        break
            memo[(mask, cur)] = res
        return memo[(mask, cur)] 
    return dp(2**N - 1, sum(nums) / k, dict()) 