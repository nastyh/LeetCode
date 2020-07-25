import math

def longestOnes_simple(A, K):
    if len(A) == 0:
            return 0

    l, r = 0, 0
    curr, glob = 0, -math.inf
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


def test(A, K):
    left = right = 0
    
    for right in range(len(A)):
    # if we encounter a 0 the we decrement K
        if A[right] == 0:
            K -= 1
        # else no impact to K
        
        # if K < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if K < 0:
            # if the left one was zero then we adjust K
            if A[left] == 0:
                K += 1
            # regardless of whether we had a 1 or a 0 we can move left side by 1
            # if we keep seeing 1's the window still keeps moving as-is
            left += 1
    return right - left + 1




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
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    # print(test2([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
    print(longestOnes_simple([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(longestOnes_simple([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

