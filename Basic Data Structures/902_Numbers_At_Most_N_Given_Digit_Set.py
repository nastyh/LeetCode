def atMostNGivenDigitSet(digits, n):
    if len(digits) == 1:
        if int(digits[0]) <= n:
            return 1
        else:
            return 0
    res = []
    digits_new = [int(i) for i in digits]
    len_digits = len(digits_new)
    def _helper(nums, curr_ix, curr_res):
        res.append(curr_res[:])
        for i in range(curr_ix, len(nums)):
            curr_res.append(nums[i])
            _helper(nums, curr_ix + 1, curr_res)
            curr_res.pop()
    _helper(digits_new, 0, [])
    ans = []   
    for elem in res:
        curr_digit = 0
        for m in elem:
            curr_digit = curr_digit * 10 + m
        ans.append(curr_digit)
    # return len([i for i in ans if i <= n])
    count_ans = 0
    for num in ans:
        if num <= n:
            count_ans += 1
    return count_ans


if __name__ == '__main__':
    print(atMostNGivenDigitSet(["1","3","5","7"], 100))