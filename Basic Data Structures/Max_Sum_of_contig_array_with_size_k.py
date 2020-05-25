def maxSubArray(nums, k):
    l= 0
    curr, gl = 0, 0

    for r in range(len(nums)):
        curr += nums[r]

        if r >= k - 1:
            gl = max(gl, curr)
            curr -= nums[l]
            l += 1
    return gl



    # l , r = 0, 1
    # curr = nums[l]
    # gl = 0
    # counter = k
    # while counter > 0:
    #     curr += nums[r]
    #     r +=1
    #     counter -= 1
    # l += 1
    # gl = max(gl, curr)
    # return gl

if __name__ == '__main__':
    print(maxSubArray([2,1,5,1,3,2], 3))
    print(maxSubArray([1, 9, -1, -2, 7, 3, -1, 2], 4))

