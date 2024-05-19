class Solution:
    def findMin(self, nums: List[int]) -> int: # O(n) so won't do 
        # we need to find a pivot index: 
        # elements are growing, then they stop they go down. We need an index of the last 
        # growing element.
        # If no such element, then the list isn't actually rotated 
        # so the first element is the min
        # if there is such an element and it's the last one,
        # the min is still the first element in the list (we came to the end of the list and the largest is the last one)
        # otherwise return the element after this one
        # don't mess up the indices
        def _helper(nums):
            piv_ix = None
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    piv_ix = i
                    break
            return piv_ix
        last_growing = _helper(nums)
        if last_growing is None:
            return nums[0]
        else: return nums[last_growing + 1] 
    
    def findMin_binary_search(self, nums: List[int]) -> int:
        # the list is growing then there is an element when
        # it goes down and starts growing again
        # we need to find this element and check that everything to the
        # left are smaller than the first element of the list and 
        # everything to the right is smaller than the first element of the list
        # Why so? Because if we take the pivot element and everything to the right and move them to the beginning
        # of the list, then we'll get a normal sorted list (like nothing was ever turned)
        if len(nums) == 1:  # edge cases
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        l , r = 0, len(nums) - 1  # usual binary search
        while l < r:
            mid = l + ( r - l) // 2
            if nums[mid] > nums[mid + 1]: # we found the top of the left half at index mid
                return nums[mid + 1] # since we know it's going to be smaller
            if nums[mid - 1] > nums[mid]: # we were growing and at mid we went down 
                return nums[mid] # it means this is the result we need (min)
            if nums[mid] > nums[0]: # it means that we're in the growing section
                l = mid + 1 # let's move to the right half
            else: # means we're moving to the left half
                r = mid - 1 # example [7, 8, 9, 0, 1, 2, 3, 4, 5, 6] nums[mid] == 1; 1 < 7, go search in the left half


