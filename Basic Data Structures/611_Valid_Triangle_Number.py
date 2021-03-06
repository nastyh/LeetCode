def triangleNumber_brute_force(nums):  # O(n^3) and O(1) TLE
    """
    Just a triple loop to generate the triplets and check the values for each of them 
    """
    res = 0
    for f_ix in range(len(nums) - 2):
        for s_ix in range(f_ix + 1, len(nums) - 1):
            for t_ix in range(s_ix + 1, len(nums)):
                first_side = nums[f_ix]
                second_side = nums[s_ix]
                third_side = nums[t_ix]
                if first_side + second_side > third_side and first_side + third_side > second_side and second_side + third_side > first_side:
                    res += 1
    return res


def triangleNumber_linear(nums):  # O(n^2)  and O(1)
    """
    we need to find the right limit of the index k for a pair of indices (i, j) chosen to find the countcount of elements
    satisfying nums[i] + nums[j] > nums[k] for the triplet (nums[i], nums[j], nums[k]) to form a valid triangle.
    """
    res = 0
    nums.sort()
    for i in range(len(nums) - 2):
        k = i + 2
        for j in range(i + 1, len(nums) - 1):
            temp = nums[i] + nums[j] - 1
            if temp < nums[j]:
                continue
            while k < len(nums) and nums[k] <= temp:
                k += 1
            res += min(k, len(nums)) - (j + 1)
    return res 


def triangleNumber_another(nums):  # O(n^2)  and O(1)
    nums.sort()
    ans = 0
    n = len(nums) - 1
    for i in range(n, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            if nums[r] + nums[l] > nums[i]:
                ans += r - l
                r -= 1
            else:
                l += 1
    return ans



if __name__ == '__main__':
    print(triangleNumber_brute_force([2, 2, 3, 4]))
    print(triangleNumber_linear([2, 2, 3, 4]))