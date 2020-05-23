class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                modified = True
        return True


#         if len(nums) == 0 or len(nums) == 1:
#             return True
#         res = []
#         for i in range(len(nums) - 1):
#             res.append(nums[i+1] - nums[i])
#         neg = sum([1 for j in res if j < 0])
#         return True if neg <= 1 else False
