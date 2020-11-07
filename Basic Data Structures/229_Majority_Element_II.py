from collections import Counter
def majorityElement(nums):  # O(n) and O(n)
    if len(nums) < 3: return nums
    d = Counter(nums)
    return [k for (k, v) in d.items() if v > len(nums) // 3]


def majorityElement_fast(nums):
    if not nums: return []
    if len(nums) < 3: return nums
    cand1, count1 = None, 0
    cand2, count2 = None, 0
    for num in nums:
        if cand1 == num:
            count1 += 1
        elif cand2 == num:
            count2 += 1
        elif count1 == 0:
            cand1 = num
            count1 += 1
        elif count2 == 0:
            cand2 = num
            count2 += 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [x for x in (cand1, cand2) if nums.count(x) > len(nums) // 3]
    

def majorityElement_generalized(nums):
    candidates = {}
    k = 3
    for num in nums:
        if num in candidates:
            candidates[num] += 1
        elif len(candidates) < k:
            candidates[num] = 1
        else:
            temp={}
            for c in candidates:
                candidates[c]-=1
                if candidates[c] >= 1:
                    temp[c] = candidates[c]
            candidates = temp
    res = [k for k in candidates if nums.count(k) > len(nums) // 3]          
    return res


if __name__ == '__main__':
    print(majorityElement([3, 2, 3]))
    print(majorityElement([1]))
    print(majorityElement([1, 2]))
    print(majorityElement_fast([3, 2, 3]))
    print(majorityElement_fast([1]))
    print(majorityElement_fast([1, 2]))
    print(majorityElement_generalized([3, 2, 3]))
    print(majorityElement_generalized([1]))
    print(majorityElement_generalized([1, 2]))
