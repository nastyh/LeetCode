def wordDistance(a: str, b: str) -> int:
    """
    Given two strings, calculate the "distance" between them.
    lenghts don't need to be the same 
    operations: 
      -- insert a char
      -- delete a char 
      -- replace a char 
      O(len(a) * len(b)) -- to go over both strings in two loops
      O(len(a) * len(b)) -- to build dp
    """
    # Your implementation here
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)] # updated b to a and vice versa
    print(f"show me empty dp: {dp}")
    # edge cases 
    for i in range(len(a) + 1):
        dp[i][0] = i # delete all
    for j in range(len(b) + 1):
        dp[0][j] = j # insert all 

    for i in range(1, len(a) + 1): # another fix 
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else: # take the min num of ops we've seen so far
                dp[i][j] = 1 + min(dp[i-1][j], 
                dp[i][j-1],
                dp[i-1][j-1])
    return dp[len(a)][len(b)] # dp[-1][-1]


if __name__ == '__main__':
    # Test cases: (string_a, string_b, expected_distance)
    test_cases = [
        ("helo", "hello", 1),
        ("algorithm", "rhythm", 6),
        ("kitten", "sitting", 3),
        ("gate", "goat", 2),
        ("saturday", "sunday", 3),
        ("", "test", 4),
        ("test", "", 4)
    ]

    for i, (word_a, word_b, expected) in enumerate(test_cases):
        result = wordDistance(word_a, word_b)
        try:
            assert result == expected
            print(f"Test Case {i + 1} PASSED")
        except AssertionError:
            print(f"Test Case {i + 1} FAILED: For ('{word_a}', '{word_b}'), expected {expected}, but got {result}")

    print("\nAll tests run.")