class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.cum_sum = [0]
        for num in self.nums:
            self.cum_sum.append(self.cum_sum[-1] + num)
        
    def sumRange(self, i, j):
        return self.cum_sum[j + 1] - self.cum_sum[i]





# normal implementation
def sumRange(nums, i, j):
    orig_sum = sum(nums[i:j + 1])

    def test_cum_sum(nums):
        cum_sum = [0] * (len(nums) + 1)
        # cum_sum[1] = nums[0]
        for i in range(1, len(nums)):
            cum_sum[i] = cum_sum[i - 1] + nums[i]
        return cum_sum
    
    cum_sum_list = test_cum_sum(nums)
    return orig_sum == cum_sum_list[j] - cum_sum_list[i] + nums[i]


if __name__ == '__main__':
    # print(test_cum_sum([-2, 0, 3, -5, 2, -1]))
    print(sumRange([-2, 0, 3, -5, 2, -1], 0, 2))
    print(sumRange([-2, 0, 3, -5, 2, -1], 2, 5))
    print(sumRange([-2, 0, 3, -5, 2, -1], 0, 5))