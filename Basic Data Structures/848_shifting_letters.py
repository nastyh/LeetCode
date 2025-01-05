class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        O(n) 
        O(n) due to an in-place update of shifts
        accumulate the shift values backward
        Each character at position i will inherit the total shifts from shifts[i] and the subsequent positions
        For each character in the string, compute the total shift and update the character
        accordingly using modular arithmetic for wrapping.
        """
        n = len(shifts)
        total_shifts = 0  # Track cumulative shifts
        result = []
        # Reverse iterate through shifts to calculate cumulative shifts
        for i in range(n - 1, -1, -1):
            total_shifts += shifts[i]
            shifts[i] = total_shifts  # Update shifts[i] to include cumulative shifts
        # Apply shifts to each character
        for i, char in enumerate(s):
            new_char = chr((ord(char) - ord('a') + shifts[i]) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)
