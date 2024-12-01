class Solution:
    def checkIfExist_set(self, arr: List[int]) -> bool:
        """
        O(N) both
        if a double number has already been seen or
        the current number is even, then it might be a double of something 
        that we've already seen, then True
        Else, False 
        """
        s = set()
        for num in arr:
            if 2*num in s or (num % 2 == 0 and num // 2 in s):
                return True
            s.add(num)
        return False
    
    def checkIfExist_binary_search(self, arr: List[int]) -> bool:
        """
        O(nlogn) and O(n): both due to binary search 
        sort and use the helper func
        it takes the list and the target (double of each number)
        if it can find it, it will return its ix. 
        Make sure its index != to the current number's index and return True 
        """
        arr.sort()
        def _helper(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r: 
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        for ix in range(len(arr)):
            curr_target = 2 * arr[ix]
            curr_ix = _helper(arr, curr_target)
            if curr_ix >= 0 and ix != curr_ix:
                return True 
        return False 
        

    
    
    def checkIfExist_brute_force(self, arr: List[int]) -> bool:
        """
        O(n^2) and O(1)
        just brute force with two pointers
        """
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False 