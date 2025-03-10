import bisect
from collections import defaultdict


class Solution:

    def countOfSubstrings_optimal(self, word: str, k: int) -> int:
        """
        O(N) - N operations for the sliding window
        O(1) - nothing extra to store
        two helpers
        to check if it's a vowel
        second uses two pointers (start and end) to maintain 
        a window of the current substring being considered 
        As end moves from 0 to the end of word, new characters are added to the window.
        The vowel or consonant count is updated accordingly.
        When the window contains all 5 vowels (checked by len(vowel_count) == 5) and the number of consonants is at least k
        (consonant_count >= k), the window is considered valid.
        After counting, the window is shrunk by moving start right, and updating the counts. This allows the algorithm to find the next potential window.
        By computing the diff b/w two helpers, we remove the substrings that have more than k
        consonants, leaving us with those that have exactly k consonants 
        """
        def _isVowel(c: str) -> bool:
            return c in ["a", "e", "i", "o", "u"]

        def _atLeastK(word: str, k: int) -> int:
            num_valid_substrings = 0
            start = 0
            end = 0
            # keep track of counts of vowels and consonants
            vowel_count = {}
            consonant_count = 0

            # start sliding window
            while end < len(word):
                # insert new letter
                new_letter = word[end]

                # update counts
                if _isVowel(new_letter):
                    vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
                else:
                    consonant_count += 1

                # shrink window while we have a valid substring
                while len(vowel_count) == 5 and consonant_count >= k:
                    num_valid_substrings += len(word) - end
                    start_letter = word[start]
                    if _isVowel(start_letter):
                        vowel_count[start_letter] = (
                            vowel_count.get(start_letter) - 1
                        )
                        if vowel_count.get(start_letter) == 0:
                            vowel_count.pop(start_letter)
                    else:
                        consonant_count -= 1
                    start += 1

                end += 1

            return num_valid_substrings
        
        return _atLeastK(word, k) - _atLeastK(word, k + 1)
    
    def countOfSubstrings_bin_search(self, word: str, k: int) -> int:
        """
        times out too
        """
        n = len(word)
        vowels = "aeiou"
        
        # Build prefix sums (using an extra element at index 0)
        prefix_cons = [0] * (n + 1)
        prefix_vowel = {v: [0] * (n + 1) for v in vowels}
        
        for i in range(1, n + 1):
            ch = word[i - 1]
            prefix_cons[i] = prefix_cons[i - 1] + (0 if ch in vowels else 1)
            for v in vowels:
                prefix_vowel[v][i] = prefix_vowel[v][i - 1] + (1 if ch == v else 0)
        
        # Precompute a dictionary: for each consonant count value, store the indices (prefix indices)
        indices_by_cons = defaultdict(list)
        for i, count in enumerate(prefix_cons):
            indices_by_cons[count].append(i)
        
        total = 0
        # For each possible ending index r (using prefix index r, corresponding to word[0:r])
        for r in range(1, n + 1):
            target = prefix_cons[r] - k  # We need prefix_cons[l] == target for a valid substring [l, r)
            if target not in indices_by_cons:
                continue
            candidates = indices_by_cons[target]
            # We only want candidate l's that come before r (i.e. l < r)
            pos = bisect.bisect_left(candidates, r)
            if pos == 0:
                continue
            
            # Now among candidates[0:pos], we need those l that satisfy:
            # for every vowel v: prefix_vowel[v][l] <= prefix_vowel[v][r] - 1.
            # We can use binary search on the sorted candidate list to find the rightmost index l that satisfies this.
            lo, hi = 0, pos - 1
            valid_boundary = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                l = candidates[mid]
                if all(prefix_vowel[v][l] <= prefix_vowel[v][r] - 1 for v in vowels):
                    valid_boundary = mid  # candidate at position mid is valid
                    lo = mid + 1  # try to push the boundary to a larger l (later in the string)
                else:
                    hi = mid - 1
            
            if valid_boundary != -1:
                # All candidates from indices 0 to valid_boundary in the list yield valid substrings ending at r.
                total += (valid_boundary + 1)
        
        return total
    def countOfSubstrings(self, word: str, k: int) -> int:
        """
        Times out
        O(n^2)
        O(26) for the dict and the set of vowels 
        """
        vowels = set("aeiou")
        n = len(word)
        total = 0
        # Iterate over all starting indices
        for i in range(n):
            cons_count = 0
            # Initialize a counter for vowels
            vowel_freq = {v: 0 for v in vowels}
            # Extend the substring from index i to j
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    vowel_freq[ch] += 1
                else:
                    cons_count += 1
                
                # If too many consonants, no need to check further for this starting index.
                if cons_count > k:
                    break
                
                # If exactly k consonants and every vowel appears at least once, count this substring.
                if cons_count == k and all(vowel_freq[v] > 0 for v in vowels):
                    total += 1
        return total
