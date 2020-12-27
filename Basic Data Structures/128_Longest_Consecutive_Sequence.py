def longestConsecutive_brute_force(nums):  # O(n^3) and O(1)
    longest_streak = 0
    for num in nums:
        current_num = num
        current_streak = 1
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longestConsecutive_sorting(nums):  # O(nlogn) and O(1)
    if not nums:
        return 0
    nums.sort()
    longest_streak = 1
    current_streak = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1]+1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

    return max(longest_streak, current_streak)


def longestConsecutive__optimized(nums):  # O(n) and O(n)
    """
    numbers are stored in a set to allow O(1) lookups, and we only attempt to build sequences from numbers that are not already part of a longer sequence.
    This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present,
    as that number would necessarily be part of a longer sequence.
    """
    longest_streak = 0
    num_set = set(nums)
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak