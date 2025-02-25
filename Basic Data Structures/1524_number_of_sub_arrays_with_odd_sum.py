from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        O(n) to iterate
        O(1) only counterrs and a runing prefix parity
        even_count = 1 (since a prefix sum of 0 is even)
        odd_count = 0
        Iterate through the array, computing the running prefix sum modulo 2 (i.e. its parity)
        Save it in prefix_parity
        for each element:
        If the current prefix_parity is odd,
        it means that any previous prefix with even parity (stored in even_count)
        will form a subarray with an odd sum when subtracted from the current prefix.
        So, add even_count to the result.
        If the prefix_parity is even, then subtracting any previous odd prefix
        (stored in odd_count) will yield an odd sum. So, add odd_count to the result.
        Update the counters (even_count or odd_count) based on the current prefix_parity
        """
        mod = 10**9 + 7
        even_count = 1  # We start with a prefix sum of 0, which is even.
        odd_count = 0
        prefix_parity = 0
        res = 0

        for num in arr:
        # Update prefix parity
            prefix_parity = (prefix_parity + num) % 2

            if prefix_parity == 1:
                res = (res + even_count) % mod
                odd_count += 1
            else:
                res = (res + odd_count) % mod
                even_count += 1
        return res
    
    def numOfSubarrays_another_optimal(self, arr: List[int]) -> int:
        """
        O(n) to go through
        O(1) nothing to store
        odd+odd=even
        even+odd=odd
        odd+even=odd
        even+even=even
        If arr[i] is even
        All previous odd subarrays remain odd.
        All previous even subarrays remain even.
        Add +1 to even subarrays, since we have one more to start at i
        If arr[i] is odd
        All prev odd become even
        All prev even become odd
        Add +1 to add subarrays, since we have one more to start at i
        res builds up as a number of odd subarrays 
        """
        odd_subarrays = 0
        even_subarrays = 0
        res = 0
        for num in arr:
            if num % 2 == 0:  # Even number
                even_subarrays += 1
            else:  # Odd number
                even_subarrays, odd_subarrays = odd_subarrays, even_subarrays
                odd_subarrays += 1
            res += odd_subarrays
        return res % (10**9 + 7)
    
    def numOfSubarrays_brute_force(self, arr: List[int]) -> int:
        """
        Times out but clean
        O(n^2) since two loops
        O(1) nothing special to store 
        Two pointers
        look how and where we build subarr_sum
        it's coming from the right pointer 
        """
        res = 0
        mod = 10**9 + 7
        if len(arr) == 1:
            if arr[0] % 2 == 0:
                return 0
            else:
                return 1 % mod 
        for l in range(len(arr)):
            subarr_sum = 0 
            for r in range(l, len(arr)):
                subarr_sum += arr[r]
                if subarr_sum % 2 == 1:
                    res = (res + 1) % mod 
        return res