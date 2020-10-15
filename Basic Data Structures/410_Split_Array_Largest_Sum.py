def splitArray(nums, k):
    l, r = max(nums), sum(nums) # lowest and highest value imaginable
    while l < r: 
        mid = (l + r) // 2 
        num_cont, curr_val = 1, 0 
        for num in nums:
            curr_val += num
            if curr_val > mid:
                now  = num # Start new container
                num_cont += 1
        if num_cont <= k:
            r = mid 
        else:
            l = mid + 1 # "mid" was too small and produced too many containers, our answer is higher
    return l


if __name__ == '__main__':
    print(splitArray([6, 3, 2, 8, 7, 5], 3))
    print(splitArray([7, 2, 5, 10, 8], 2))