import math
def maxArea(height):
    l, r = 0, len(height) - 1
    curr_sq, glob_sq = 0, -math.inf
    while l < r:
        curr_sq = min(height[l], height[r]) * (r - l)
        glob_sq = max(glob_sq, curr_sq)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        # if height[l + 1] > height[l]:
        #     l += 1
        # elif height[r - 1] > height[r]:
        #     r -= 1
        # else:
        #     l += 1
        #     r -= 1
    return glob_sq


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(maxArea([[1, 3, 2, 5, 25, 24, 5]]))
    