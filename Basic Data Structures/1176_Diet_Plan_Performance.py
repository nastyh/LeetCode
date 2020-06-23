def dietPlanPerformance(calories, k, lower, upper):
    if len(calories) == 0: return
    l = 0
    r = l + k - 1
    res = 0
    while r < len(calories):
        # curr_w = 0
        curr_w = sum(calories[l: r + 1])
        if curr_w < lower: res -= 1
        if curr_w > upper: res += 1
        l += 1
        r = r + 1
        # curr_w = 0
    return res

if __name__ == '__main__':
    print(dietPlanPerformance([1,2,3,4,5], 1, 3, 3))
    print(dietPlanPerformance([3,2], 2,0,1))
    print(dietPlanPerformance([6,5,0,0], 2, 1, 5))
    print(dietPlanPerformance([6,13,8,7,10,1,12,11], 6, 5, 37))

