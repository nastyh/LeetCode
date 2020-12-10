from math import pow

def numSubseq_alt(nums, target):
    res = 0
    end = len(nums)-1
    nums.sort()
    for i in range(len(nums)):
        while nums[i] + nums[end] > target:
            if end > i:
                end = end - 1
            else:
                return res % (10**(9) + 7)
        res += pow(2, end - i)
    return res % (10**(9) + 7)

if __name__ == '__main__':
    print(numSubseq_alt([3, 5, 6, 7], 9))