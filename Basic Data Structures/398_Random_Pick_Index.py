from collections import defaultdict
import random
class Solution:  # O(n) both: to build the dictionary and to store the dictionary
    """
    Create a defauldict in a form num: [indices of the num from nums]
    Then apply random.choice(list) to the appopriate value from the dictionary 
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.d = defaultdict(list)
        for k, v in enumerate(self.nums):
            self.d[v].append(k)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])


class Solution_another:  # O(n) and O(1): iterate once over nums but store only one record
    """
    Same as above but we will build the dictionary inside pick() once we know the value of target.
    This way we avoid storing the whole dictionary 
    """
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.d = defaultdict(list)

    def pick(self, target: int) -> int:
        for k, v in enumerate(self.nums):
            if v == target:
                self.d[v].append(k)
        return random.choice(self.d[target])


class Solution_reservoir_sampling:  # O(N) both 
    """
    maintain previous occurance count, say for [1,2,3,3,3] and target = 3, for i=2:
    random int in the range 0 to 0, (prob = 1)
    when count = 2, random can in[0,1], prob =1/2, count = 3, random range = [0,2], prob = 1/3.
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(0, count - 1)
                # chance of getting 0 is 1/count, then we pick that number. So when we have 3 nums, chance of picking it is 1/3,
                # (if chance is not 0, i value may be previous value or even previous before that. so prob remains 1/count)
                if chance == 0:
                    res = i
        return res