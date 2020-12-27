class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """ 
        if number not in self.d:
            self.d[number] = 1
        else:
            self.d[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        If a complement is also in the d, this is True
        Edge case: when value is 10 and you need to cover a possible case with two 5s 
        """
        for num in self.d.keys():
            complement = value - num
            if num != complement:
                if complement in self.d.keys():
                    return True
            elif self.d[num] > 1:
                return True
        return False 
        

class TwoSum_sorting:
    """
    When you call find(), sort everything and do a two pointer approach 
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
       self.nums = []
       self.isSorted = False
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """ 
        self.nums.append(number)
        self.isSorted = False

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if self.isSorted == False:
            self.nums.sort()
            self.isSorted = True
        l, r = 0, len(self.nums) - 1
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] < value:
                l += 1
            else:
                r -= 1
        return False 
        