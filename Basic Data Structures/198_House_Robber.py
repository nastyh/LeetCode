def rob(nums):
    prev = curr = 0
    for n in nums:
        temp = curr
        curr = max(prev + n, curr)
        prev = temp
    return curr


def rob_linear(nums):
    """
    no need for the whole dp list. Need to keep track of the second house from the left
    and from the first house to the left. Then make updates
    """
    max_from_second_left_house = max_from_first_left_house = 0
    for num in nums:
        max_from_second_left_house, max_from_first_left_house = max_from_first_left_house, max(max_from_first_left_house, max_from_second_left_house + num)
    return max_from_first_left_house


def rob_dp(nums):
    # if nothing is given, return 0. If only one element, return it. If two -- return max
    # Inititate a list dp with None. Every element contains a max number that you can get if you rob all houses up to this point including this house
    # dp[0] = nums[0]. The best you can do with one house, is just rob it
    # dp[1] = max(nums[0], nums[1]). If you can rob only one house of two, rob that with more money
    # after that make a decision: rob the current house and add this number to what you've robbed tho houses ago or don't rob this house and stay with the previous max (hoping that the next house will be good, probably)
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)
    dp = [None] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i -1], nums[i] + dp[i - 2])
    return dp[-1]
    

if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob_dp([1, 2, 3, 1]))
    print(rob_linear([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob_dp([2, 7, 9, 3, 1]))
    print(rob_linear([2, 7, 9, 3, 1]))
