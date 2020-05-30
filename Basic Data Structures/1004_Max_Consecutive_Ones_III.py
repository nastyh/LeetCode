import math
def longestOnes(A, K):
    if len(A) == 0:
        return 0

    l, r = 0, 0
    # curr, glob = 0, -math.inf
    num_of_zeroes = K

    while r < len(A):
        if A[r] == 0:
            num_of_zeroes -= 1
        if num_of_zeroes < 0:
            if A[l] == 0:
                num_of_zeroes += 1
                l += 1
            else:
                l += 1
        r += 1
    return r - l

    # while r < len(A):
    #     while num_of_zeroes > 0:
    #         if A[r] == 0:
    #             num_of_zeroes -= 1
    #         curr = r - l + 1
    #         glob = max(glob, curr)
    #         r += 1
    #     if A[l] == 0:
    #         l += 1
    #         num_of_zeroes += 1
    #     else:
    #         l += 1
    # return glob

if __name__ == '__main__':
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    # print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))




