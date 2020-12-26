class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.cum_sum = [0]
        for num in self.nums:
            self.cum_sum.append(self.cum_sum[-1] + num)
        
    def sumRange(self, i, j):
        return self.cum_sum[j + 1] - self.cum_sum[i]




class NumArray_another:
    """
    Slightly different
    Need to consider an edge case when a provided list is empty, otherwise running_sum will throw an error
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(self.nums) == 0:
            self.running_sum = [0]
        else:
            self.running_sum = [None] * len(self.nums)
            self.running_sum[0] = self.nums[0]
            for i in range(1, len(self.nums)):
                self.running_sum[i] = self.running_sum[i - 1] + self.nums[i]


    def sumRange(self, i: int, j: int) -> int:
        return self.running_sum[j] - self.running_sum[i] + self.nums[i]




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


def sumRange_alt(nums, i, j):  # doesn't pass weird edge cases 
    orig_sum = sum(nums[i:j + 1])

    def test_cum_sum(nums):
        cum_sum = [0] * len(nums)
        cum_sum[0] = nums[0]
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
    print(sumRange_alt([-2, 0, 3, -5, 2, -1], 0, 2))
    print(sumRange_alt([-2, 0, 3, -5, 2, -1], 2, 5))
    print(sumRange_alt([-2, 0, 3, -5, 2, -1], 0, 5))