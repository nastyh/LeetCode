class Solution:

    def __init__(self, nums: List[int]):
        """
        O(N^2) due to remove/pop, which run in linear time. And it happens around n times
        so we have squared
        O(n) to store the original array
        brute force
        If we put each number in a "hat" and draw them out at random, the order in
        which we draw them will define a random ordering.
        # The brute force algorithm essentially puts each number in the aforementioned
        # "hat", and draws them at random (without replacement) until there are none
        # left. Mechanically, this is performed by copying the contents of array into
        # a second helper array named helper before overwriting each element of
        # array with a randomly selected one from helper. After selecting each random
        # element, it is removed from helper to prevent duplicate draws. The
        # implementation of reset is simple, as we just store the original state of nums on
        construction

        """
        self.array = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self) -> List[int]:
        helper = list(self.array)
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(helper))
            self.array[idx] = helper.pop(remove_idx)
        return self.array

    def __init__(self, nums: List[int]):
        """
        O(n) for both 
        Fisher-Yates Algorithm
        On each iteration of the algorithm, we generate a random integer between the
        current index and the last index of the array. Then, we swap the elements at
        the current index and the chosen index - this simulates drawing (and
        removing) the element from the hat, as the next range from which we select a
        random index will not include the most recently processed one. One small, yet important
        detail is that it is possible to swap an element with itself - otherwise, some
        array permutations would be more likely than others. 
        """
        self.array = nums
        self.original = list(nums)
    
    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()