class NumArray:  # works but TLE  O(N) both 
    """
    Initialize a list with the running sum as usual
    The new thing is update()
    When we change a number in nums, we need to propagate this change to running.
    Let's say, nums = [1, 3, 5], thus, running is [1, 4, 9]
    We get update(1, 2) -- change the number at index 1 to 2
    then nums = [1, 2, 5] and running should become [1, 3, 8]
    How to get from [1, 4, 9] to [1, 3, 8]?
    Starting from index 1, we need to subtract from every element in nums the difference between
    original nums[index] and the value passed in update().
    So it will be nums[1] - 2 --> 3 - 2 = 1
    Go to running and from the first index subtract 1 everywhere to the right 
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.running = [0] * len(self.nums)
        self.running[0] = self.nums[0]
        for i in range(1, len(self.running)):
            self.running[i] = self.running[i - 1] + self.nums[i]
        

    def update(self, index: int, val: int) -> None:
        diff = self.nums[index] - val 
        for i in range(index, len(self.running)):
            self.running[i] -= diff
        self.nums[index] = val
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.running[right] - self.running[left] + self.nums[left]


class NumArray_segment_tree:  # O(n) to calculate the sum of one node during each iteration of the for loop. Space is O(n): O(2n) to store the segment tree
    """
    The segment tree for array a[o..n] is a binary tree in which each node contains aggregate information (min, max, sum, etc.)
    for a subrange [i...j] of the array, as its left and right child hold information for range [i...(i + j) / 2] and [(i + j) / 2 + 1, j]
    if the element at index i is not a leaf, its left and right child are stored at index 2i and 2i + 1 respectively.
    """
    
    def __init__(self, nums: List[int]):  # O(n) and O(n) we use 2n extra space to be exact
        self.nums = nums
        self.segment_tree = [0] * 4*len(self.nums)
        if self.nums:
            self.build_segment_tree(0, len(self.nums)-1, 0)

    def update(self, i: int, val: int) -> None:  # O(logn) and O(1)
        diff = val - self.nums[i]
        self.nums[i] = val
        self.perform_update(0, len(self.nums)-1, diff, i, 0)

    def perform_update(self,seg_start, seg_end, diff, i, seg_i):
        if i < seg_start or i > seg_end:
            return 
        self.segment_tree[seg_i] += diff
        if seg_start < seg_end:  
            mid = (seg_start+seg_end)//2
            self.perform_update(seg_start, mid, diff, i, 2 * seg_i + 1)
            self.perform_update(mid + 1, seg_end, diff, i, 2 * seg_i + 2)

    def sumRange(self, i: int, j: int) -> int:  # O(logn) both
        return self.get_sum_range(i, j, 0, len(self.nums) - 1, 0)

    def build_segment_tree(self, start, end, i):
        if start == end:
            self.segment_tree[i] = self.nums[start]
        else:
            mid = (start + end)//2
            self.segment_tree[i] = (
                self.build_segment_tree(start, mid, 2 * i + 1) +
                self.build_segment_tree(mid + 1, end, 2 * i + 2)
            )
        return self.segment_tree[i]

    def get_sum_range(self,q_start, q_end, sg_start, sg_end, i):
        if sg_start > q_end or sg_end < q_start:
            return 0
        elif sg_start >= q_start and sg_end <= q_end:
            return self.segment_tree[i]
        else:
            mid = (sg_start+sg_end) // 2
            return (
                self.get_sum_range(q_start, q_end, sg_start, mid, 2 * i + 1)+
                self.get_sum_range(q_start, q_end, mid + 1, sg_end, 2 * i + 2)
            )