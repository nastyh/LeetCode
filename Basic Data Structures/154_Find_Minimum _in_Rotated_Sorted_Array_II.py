def findMin(nums):  # optimal 
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
    

def findMin_recur(nums):
    l, h = 0, len(nums)-1
    while h > l + 1 and nums[h] <= nums[l]:
        mid = (l + h) // 2
        if nums[mid] == nums[h] == nums[l]:
            return min(findMin_recur(nums[l:mid]), findMin_recur(nums[mid:h + 1]))
        elif nums[mid] > nums[h]:
            l = mid
        elif nums[mid] < nums[l]:
            h = mid
    return min(nums[l], nums[h])