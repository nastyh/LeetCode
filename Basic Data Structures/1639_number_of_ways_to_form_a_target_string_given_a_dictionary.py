class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        O(word_length * targret_length + word_length * total_words)
        O(word_length * target_length)
        two variables that change as we progress through the matrix: the current word index (currWord)
        and the current target string index (currTarget).
        two loops to iterate over all the combinations
        if currTarget is 0, then dp[currWord][0] = 1,
        meaning there is exactly one way to form an empty target string, regardless of the number of columns in words.

        Skip the current column of words:
        Carry over the value from the previous row: dp[currWord][currTarget]=dp[currWord−1][currTarget] 

        Include the current character if it matches:
        If target[currTarget - 1] matches a character in the current column of words,
        add its contribution: dp[currWord][currTarget]+=charFrequency[currWord−1][target[currTarget−1]− ′a′]⋅dp[currWord−1][currTarget−1]
        take the result modulo 10^9+7 at every step to prevent overflow.
        total number of ways to form the target string is stored in dp[wordLength][targetLength].
        """
        word_length = len(words[0])
        target_length = len(target)
        mod = 1000000007
        # Step 1: Calculate frequency of each character at every index in
        # "words".
        char_frequency = [[0] * 26 for _ in range(word_length)]
        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1
        # Step 2: Initialize a DP table.
        dp = [[0] * (target_length + 1) for _ in range(word_length + 1)]
        # Base case: There is one way to form an empty target string.
        for curr_word in range(word_length + 1):
            dp[curr_word][0] = 1
        # Step 3: Fill the DP table.
        for curr_word in range(1, word_length + 1):
            for curr_target in range(1, target_length + 1):
                # Carry over the previous value (not using this index of
                # "words").
                dp[curr_word][curr_target] = dp[curr_word - 1][curr_target]
                # Add ways using the current index of "words" if the characters
                # match.
                cur_pos = ord(target[curr_target - 1]) - ord("a")
                dp[curr_word][curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * dp[curr_word - 1][curr_target - 1]
                ) % mod
                dp[curr_word][curr_target] %= mod
        # Step 4: The result is in dp[word_length][target_length].
        return dp[word_length][target_length]
    
    def numWays_another(self, words: List[str], target: str) -> int:
        """
        (O(m \times (k + n))) m -- col length (length of each word), k is the num of words
        O(m \times (n + 26))): freq table takes (O(m \times 26)) (for 26 letters), dp table takes (O(m \times n)).
        Each column acts as a source of potential characters for the respective positions in the target
        calculate the frequency of each character for every column of the words list.
        dp[i][j]:
        i is the number of columns considered so far.
        j is the number of characters matched so far in the target.
        dp[i][j] represents the number of ways to form the first j characters of the target using the first i columns.
        For each column i, we can:
        Skip the column: Carry forward the previous value (dp[i][j] = dp[i-1][j]).
        Use the column to match the current character in target (if possible). Update based on the frequency of the character in the current column.
        value at dp[m][n] gives the total number of ways to form the target string.
        """
        MOD = 1000000007
        m, n = len(words[0]), len(target)
        # Step 1: Precompute character frequencies in each column
        freq = [[0] * 26 for _ in range(m)]
        for word in words:
            for i in range(m):
                freq[i][ord(word[i]) - ord('a')] += 1
        # Step 2: Dynamic Programming
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            for j in range(n + 1):
                # Case 1: Skip the current column
                dp[i][j] = dp[i - 1][j]
                # Case 2: Use the current column (only if j > 0)
                if j > 0:
                    char_index = ord(target[j - 1]) - ord('a')
                    dp[i][j] += dp[i - 1][j - 1] * freq[i - 1][char_index]
                    dp[i][j] %= MOD
        return dp[m][n]

