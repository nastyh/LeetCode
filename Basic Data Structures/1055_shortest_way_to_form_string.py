class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        O(mn), m len of target, n len of source
        O(1)
        i iterates over target
        j iterates over source
        start going over both
        if the curr chars match, move both pointers
        if don't, move the j in source
        when source is done, increment a counter for subsequences and reset j to 0
        If a character in target doesn't exist in source, forming target is impossible, so return -1.
        """
        subsequences = 0
        i = 0  # Pointer for target
        while i < len(target):
            j = 0  # Pointer for source
            matched = False  # Track if we match any character in this pass
            while j < len(source) and i < len(target):
                if source[j] == target[i]:
                    i += 1
                    matched = True
                j += 1
            if not matched:  # If no match was found in this pass
                return -1
            subsequences += 1
        return subsequences

    def shortestWay_binary_search(self, source: str, target: str) -> int:
        """
        O(n+m×k), where m is the length of target, n is len of source, 
        k num of occurences of a character in source
        """
        def find_next_index(indices, current):
            """
            iterate thru the list of indices to find the smallest
            ix that is >= that the current one
            """
            for idx in indices:
                if idx >= current:
                    return idx
            return None
        char_to_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_to_indices[c].append(i)
        source_iterator = 0
        # Number of times we need to iterate through source
        count = 1
        # Find all characters of target in source
        for char in target:
            # If character is not in source, return -1
            if char not in char_to_indices:
                return -1
            # Find the next valid index using the helper function
            index = find_next_index(char_to_indices[char], source_iterator)
            # If no valid index is found, restart iteration
            if index is None:
                count += 1
                source_iterator = char_to_indices[char][0] + 1
            else:
                source_iterator = index + 1
        # Return the number of times we need to iterate through source
        return count

    def shortestWay_dp(self, source: str, target: str) -> int:
        """
        O(n*26 +m) = O(n+m)
        O(n)
        Create a 2D DP table next_position, where next_position[i][ch] gives the index of
        the next occurrence of the character ch in source starting from position i.
        If a character does not exist after position i, store -1 for that character.
        Use the next_position table to track the current position in source while iterating through target.
        If the current character in target cannot be matched starting from the current position in source,
        restart from the beginning of source and increment the count of subsequences.
        """
        n = len(source)
        m = len(target)

        # Step 1: Precompute next_position table
        next_position = [[-1] * 26 for _ in range(n)]
        last_seen = [-1] * 26  # Tracks last seen position for each character

        for i in range(n - 1, -1, -1):
            last_seen[ord(source[i]) - ord('a')] = i
            for ch in range(26):
                next_position[i][ch] = last_seen[ch]

        # Step 2: Iterate through the target
        subsequences = 1
        current_position = 0  # Pointer in source

        for char in target:
            char_index = ord(char) - ord('a')

            # If the character is not in source, return -1
            if last_seen[char_index] == -1:
                return -1

            # If the character cannot be matched from the current position
            if current_position == n or next_position[current_position][char_index] == -1:
                subsequences += 1
                current_position = 0

            # Update the current position
            current_position = next_position[current_position][char_index] + 1

        return subsequences