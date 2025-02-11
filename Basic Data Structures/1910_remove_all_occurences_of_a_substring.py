class Solution:
    def removeOccurrences_kmp(self, s: str, part: str) -> str:
        """
        Build KMP table O(m), len of part
        Searching with KMP: O(n), length of s
        Worst case is O(n^2) to repeat the search and removal process if each removal is O(n)
        Space: O(m) for table, O(n) for string manipulation

        Building the KMP table:
        For each character in part, determine the length of the longest prefix of
        part that matches a proper suffix ending at that position. This helps us backtrack efficiently during a mismatch.
        Search in the table:
        Compare characters from s and part. If a mismatch occurs, use the KMP table to backtrack
        If a full match is found, return the starting index of part in s.
        Remove and repeat:
        Once a match is found, remove the substring part and continue the search until no occurrences are left.
        """
        def build_kmp_table(pattern):
            kmp_table = [0] * len(pattern)
            j = 0  # Length of the previous longest prefix-suffix
            for i in range(1, len(pattern)):
                # Handle mismatch and backtrack
                while j > 0 and pattern[i] != pattern[j]:
                    j = kmp_table[j - 1]
                # If characters match, increase j and update the table
                if pattern[i] == pattern[j]:
                    j += 1
                kmp_table[i] = j
            return kmp_table
        
        def kmp_search(text, pattern, kmp_table):
            n, m = len(text), len(pattern)
            i = j = 0  # Pointers for text and pattern
            
            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    # If we have matched the entire pattern
                    if j == m:
                        return i - m  # Return the start index of the match
                else:
                    # Handle mismatch using the KMP table
                    if j > 0:
                        j = kmp_table[j - 1]
                    else:
                        i += 1  # Move to the next character in text
            
            return -1  # No match found
        
        kmp_table = build_kmp_table(part)
    
    # Perform substring removal using KMP search repeatedly
        while True:
            match_index = kmp_search(s, part, kmp_table)
            if match_index == -1:
                break  # No more occurrences of part found
            s = s[:match_index] + s[match_index + len(part):]  # Remove the substring
        
        return s


    def removeOccurrences_stack(self, s: str, part: str) -> str:
        """
        O(mn), lengths of strings
        O(n), len of s due to the stack
        For each character, add it to the stack.
        After adding a character, check if the top of the stack matches the substring part.
        if yes, pop the last len(part) characters from the stack.
        return remaining stack
        """
        st = []
        for ch in s:
            st.append(ch)
            if len(st) >= len(part) and "".join(st[-len(part):]) == part:
                for _ in range(len(part)):
                    st.pop()
        return "".join(st)