def subarraySum(nums, k):
        res, curr_sum, start = 0, 0, nums[0]
        for i in range(1, len(nums)):
            curr_sum = start + nums[i]
            if curr_sum == k:
                res += 1
                start = nums[i]
        return res

if __name__ == '__main__':
    print(subarraySum([1,1,1], 2))
