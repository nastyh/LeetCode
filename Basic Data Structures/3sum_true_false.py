def find_sum_of_three(nums, target):
    """
    True if the sum of three diff elements == target
    False otherwise
    O(nlogn) due to sorting
    O(1)
    for each number at index i, we will solve a 2sum for other two numbers to the right
    """
    nums.sort()
    for i in range(0, len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            candidate = nums[i] + nums[l] + nums[r]
            if candidate == target: return True
            elif candidate < target:
                l+= 1
            else:
                r -=1
    return False