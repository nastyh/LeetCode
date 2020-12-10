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

    if not nums or int(sum(nums)/k) != sum(nums)/k:
        return False
    nums.sort(reverse = True)
    parts = [sum(nums)/k]*k
    return dfs(parts, nums, 0)


def canPartitionKSubsets_alt(nums, k):
    def dfs(nums, idx, targets):
        if idx == len(nums):
            return True
         for i, v in enumerate(targets):
            if nums[idx] <= v:
                targets[i] -= nums[idx]
                if self.dfs(nums, idx + 1, targets):
                    return True
                targets[i] += nums[idx]

    target = sum(nums)
    if target % k:
        return False
    targets = [target//k for _ in range(k)]
    nums.sort(reverse = True)
    return dfs(nums, 0, targets)