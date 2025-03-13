"""
start with a 2sum
expand to n cards
"""

def two_sum(nums, target, start):
    """
    Find all unique pairs in nums[start:] that sum to target using two-pointer approach.
    O(n)
    """
    res = []
    left, right = start, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            res.append([nums[left], nums[right]])
            left += 1
            right -= 1
            # Skip duplicates if needed
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return res

def k_sum(nums, target, k, start):
    """
    Recursively find all unique combinations of k numbers from nums[start:] that sum to target.
    O(n^(k-1)), k the num of cards
    Same for space incl. output
    """
    res = []
    # Base case: if we need to find 2 numbers, use the two_sum function.
    if k == 2:
        return two_sum(nums, target, start)
    
    # For k > 2, recursively reduce the problem.
    for i in range(start, len(nums) - k + 1):
        # Optionally skip duplicates if avoiding repeated combinations
        if i > start and nums[i] == nums[i - 1]:
            continue
        
        # Early termination: if the current number is too big or too small, skip further processing.
        if nums[i] * k > target or nums[-1] * k < target:
            break
        
        # Recursive call for k - 1 sum.
        subsets = k_sum(nums, target - nums[i], k - 1, i + 1)
        for subset in subsets:
            res.append([nums[i]] + subset)
    
    return res

def find_n_sum(credit_cards, total, n):
    """
    Main func
    Given a list of credit card amounts (credit_cards), determine if you can pick exactly n cards
    that sum up to the total.
    Returns all valid combinations.
    """
    # Sort the list to make the two-sum technique and duplicate skipping easier.
    credit_cards.sort()
    return k_sum(credit_cards, total, n, 0)

# Example usage:
credit_cards = [10, 20, 30, 40, 50, 60]
total = 100
n = 3  # Now we want to find if any 3 credit cards add up to 100.
result = find_n_sum(credit_cards, total, n)
print("Combinations of {} cards that sum to {}:".format(n, total), result)

# For classic 2-sum (n=2)
result_two_sum = find_n_sum(credit_cards, total, 2)
print("Combinations of 2 cards that sum to {}:".format(total), result_two_sum)
