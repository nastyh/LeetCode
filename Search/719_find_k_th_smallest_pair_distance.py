class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        O(nlogn) and O(1)
        After sorting the array, we perform a binary search to find the kth smallest distance.
        The binary search is conducted on the range of possible distances between elements in the array.
        We initialize left to 0 (minimum possible distance) and right to the maximum possible difference
        between any two elements in the sorted array (nums[-1] - nums[0]).
        In each iteration of the binary search, we calculate the midpoint mid between left and right.
        We then use the helper function to count the number of pairs with distances less than or equal to mid.
        This function performs a linear scan through the array and counts such pairs.
        If the count is less than k, we know that the kth smallest distance must be larger than mid, so we update left to mid + 1.
        If the count is greater than or equal to k, we update right to mid because we need to find a smaller distance.
        The binary search continues until left is no longer less than right, at which point left will be equal to the kth smallest distance.
        The helper function performs a linear scan through the sorted array to count the number
        of pairs with distances less than or equal to mid. This count is achieved by maintaining two pointers,
        left and right, which point to the start and end of the sliding window of elements.
        We start with left at index 0 and iterate through the array with right increasing from 0 to the end of the array.
        While the difference between nums[right] and nums[left] is greater than mid, we increment left to shrink the window.
        For each right, the number of valid pairs with distances less than or equal to mid is the difference between right
        and left. This is because the array is sorted, and as long as the difference condition is met, all elements between left and right are valid pairs.
        The function returns the total count of such pairs.
        """
        def _helper(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = _helper(nums, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def smallestDistancePair_another(self, nums: List[int], k: int) -> int:
        """
        O(nlog(n) + nlog(max pair distance) + n)
        O(1)
        """
        nums.sort()
        def _helper(guess):
            left = count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        low, high = 0, nums[-1] - nums[0]
        while low <= high:
            mid = (low + high) // 2
            
            if _helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
    def smallestDistancePair_two_pointers(self, nums: List[int], k: int) -> int:
        """
        The minimum possible distance is 0 (if there are duplicates),
        and the maximum possible distance is the difference between the largest and smallest element in the sorted array.
        For any given middle distance mid, we need to count how many pairs of elements in the sorted array have
        a distance less than or equal to mid. This counting can be done efficiently using the two-pointer technique.
        """
        nums.sort()
        l, r = 0, nums[-1] - nums[0] # smallest possible diff and largest possible diff
        def _helper(m):
            """
            counts how many pairs of elements have a distance less than or equal to m.
            The right pointer moves forward through the array, while the left pointer is
            adjusted to ensure that the difference between nums[right] and nums[left] is within m.
            The number of valid pairs for each right is given by right - left, as all elements
            between left and right have a distance less than or equal to mid.
            """
            count, left = 0, 0 
            for right in range(len(nums)):
                while nums[right] - nums[left] > m: # we want to decrease the diff as much as possible
                    left += 1
                count = count + right - left # getting rid of the pairs 
            return count
        while l < r:
            """
            O(nlogn+nlogD)
            O(1)
            The goal of the binary search is to find the smallest distance
            such that there are at least k pairs with a distance less than or equal to that distance.
            mid is calculated as the middle of the current range [left, right].
            _helper(mid) function determines how many pairs have a distance ≤ mid
            If the count is less than k, it means the target distance is larger than mid, so we adjust the left boundary.
            Otherwise, the right boundary is adjusted to search for smaller distances.
            After the binary search converges, left will point to the k-th smallest distance. This value is returned as the result.
            """
            mid = l + (r - l) // 2
            if _helper(mid) < k: 
                l = mid + 1 
            else:
                r = mid 
        return l 

    def smallestDistancePair_dp(self, nums: List[int], k: int) -> int:
        """
        O(nlogn+nlogM+M) where n is the num of elements and M the max poss distance
        O(n+M+S) S is for sorting overhead, in Python it's O(n)
        The minimum distance is 0, and the maximum is the difference between the largest
        and smallest elements in the array. This bounded range allows us to use binary search
        to efficiently find the k-th smallest distance.
        for any given distance d, we can count the number of pairs in the array with a
        distance less than or equal to d. If this count is less than k, the k-th smallest distance
        must be greater than d. Conversely, if the count is at least k, the k-th smallest distance must be
        less than or equal to d. This forms the basis of our binary search approach.
        The lower bound of our search range is 0, and the upper bound is the difference between the maximum and minimum elements in the sorted array.
        In each iteration, we calculate the midpoint of the current range and count the number of pairs
        with distances less than or equal to this midpoint.
        prefixCount: This array maintains the cumulative count of elements up to each value in the sorted array.
        For any index i, prefixCount[i] represents the number of elements less than or equal to i.
        valueCount: Implemented as a hash map, valueCount[i] stores the count of occurrences of the value i in the array.

        """
        def _helper(nums, prefix_count, value_count, max_distance):
            count = 0
            array_size = len(nums)
            index = 0

            while index < array_size:
                current_value = nums[index]
                value_count_for_current = value_count[current_value]

                # Calculate pairs involving current value with distance <= max_distance
                pairs_with_larger_values = (
                    prefix_count[
                        min(current_value + max_distance, len(prefix_count) - 1)
                    ]
                    - prefix_count[current_value]
                )
                pairs_with_same_values = (
                    value_count_for_current * (value_count_for_current - 1) // 2
                )
                count += (
                    pairs_with_larger_values * value_count_for_current
                    + pairs_with_same_values
                )

                # Skip duplicate values
                while index + 1 < array_size and nums[index] == nums[index + 1]:
                    index += 1
                index += 1

            return count


        nums.sort()
        nums_size = len(nums)
        max_el = nums[-1] # since it's sorted
        max_dist = max_el * 2 
        # prefix counts and value counts
        prefix_count = [0] * max_dist
        value_count = [0] * (max_el + 1)

        index = 0
        for value in range(max_dist):
            while index < nums_size and nums[index] <= value:
                index += 1
            prefix_count[value] = index
        for i in range(nums_size):
            value_count[nums[i]] += 1
        
        left, right = 0, max_el
        while left < right:
            mid = (left + right) // 2
            # Count pairs with distance <= mid
            count = _helper(nums, prefix_count, value_count, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
