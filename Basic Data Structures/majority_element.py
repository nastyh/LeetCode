from collections import defaultdict
def major_element(nums): # Pythonic
    if len(nums) == 0: return []
    if len(nums) == 1: return [0]
    thr = len(nums) // 2
    d = defaultdict(list)
    for n_ix in range(len(nums)):
        if nums[n_ix] not in d:
            d[nums[n_ix]].append(1)
            d[nums[n_ix]].append([n_ix])
        else:
            d[nums[n_ix]][0] += 1
            d[nums[n_ix]][1].extend([n_ix])
    return [v[1] if v[0] > thr else [] for k,v in d.items()][0]

def major_element_simple(nums): # straightforward
    if len(nums) == 0: return []
    if len(nums) == 1: return [0]
    thr = len(nums) // 2
    res = []
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    elements = [k for k, v in d.items() if v > thr]
    return [k for k, v in enumerate(nums) if v in elements]

if __name__ == '__main__':
    print(major_element([1, 1, 2]))
    print(major_element([0, 1]))
    print(major_element([]))
    print(major_element([6, 8, 1, 1, 2, 3, 8, 5, 5, 8, 8, 8, 8, 8, 8, 8]))
    # print(major_element_simple([1, 1, 2]))
    # print(major_element_simple([0, 1]))
    # print(major_element_simple([]))
