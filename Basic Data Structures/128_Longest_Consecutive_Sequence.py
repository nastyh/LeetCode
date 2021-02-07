from collections import Counter
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
    """
    Sort and count all numbers that are next to each other and are different by 1 
    """
    if not nums:
        return 0
    nums.sort()
    longest_streak = 1
    current_streak = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    return max(longest_streak, current_streak)

def longestConsecutive_left_right(nums):  # O(n) both
    """
    All numbers to the set to get O(1) access
    For each number check if this number is a potential start of a sequence (means there is no num - 1)
    If it's a case, start incrementing this number by 1 and checking if the newly incremented number is still in the set
    Update the result accordingly 
    """
    s = set()
    res = 0
    for num in nums:
        s.add(num)
    for num in nums:
        if num - 1 not in s:  # nums is a start of the sequence
            step = 0 
            while num + step in s:
                step += 1
            res = max(step, res)
    return res
    

def longestConsecutive_optimized(nums):  # O(n) and O(n)
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


if __name__ == '__main__':
    print(longestConsecutive_optimized([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive_optimized([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longestConsecutive_left_right([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive_left_right([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))