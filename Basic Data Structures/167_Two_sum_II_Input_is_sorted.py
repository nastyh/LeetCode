def twoSum(numbers, target): # numbers are in the ascending order
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -=1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l + 1, r + 1]

