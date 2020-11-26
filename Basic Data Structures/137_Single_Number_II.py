from collections import Counter
def singleNumber(nums):  # uses extra space
    d = Counter(nums)
    return [k for k, v in d.items() if v != 3][0]


def singleNumber_set(nums):  # also extra space
    return (3 * sum(set(nums)) - sum(nums)) // 2


def singleNumber_bit(nums):
    seen_once = seen_twice = 0
    for num in nums:
        # first appearance: 
        # add num to seen_once 
        # don't add to seen_twice because of presence in seen_once
        
        # second appearance: 
        # remove num from seen_once 
        # add num to seen_twice
        
        # third appearance: 
        # don't add to seen_once because of presence in seen_twice
        # remove num from seen_twice
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~seen_once & (seen_twice ^ num)
    return seen_once