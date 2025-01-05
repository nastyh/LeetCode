class Solution:
    def shiftingLetters_prefix_sum(self, s: str, shifts: List[List[int]]) -> str:
        """
        O(n+k), n is the length of string, k is the number of shifts
        O(n) for shift_marks

        We don't want to move the same character back and forth many times
        Better to first calculate all the shifts for each character and apply them once
        shift_marks to record the cumulative shifts for each character:
        Increment the start index of the shift by the shift direction value
        Decrement the end index + 1 to balance out the shift beyond the specified range
        Perform a prefix sum over the auxiliary array to compute the net shift at each character.
        Apply the new shifts only once
        """
        n = len(s)
        res = []
        shift_marks = [0] * (n + 1)  # Extra space to handle end+1 decrement
        # mark the shifts
        for start, end, direction in shifts:
            shift_direction = 1 if direction == 1 else -1
            shift_marks[start] += shift_direction
            if end + 1 < n:
                shift_marks[end + 1] -= shift_direction
        # compute the prefix sum
        for i in range(1, n):
            shift_marks[i] += shift_marks[i - 1]
        # apply the computed shifts to the string 
        for i, char in enumerate(s):
            base = ord('a') 
            net_shift = shift_marks[i] % 26
            new_char = chr((ord(char) - base + net_shift) % 26 + base)
            res.append(new_char)
        return ''.join(res)

    def shiftingLetters_times_out(self, s: str, shifts: List[List[int]]) -> str:
        """
        O(nm), n num of shift operations, m length of s
        O(m)
        Times out!
        Turn the string into a list of characters
        work with ord of each character to move left or right depending on the ask
        build the answer and return as a string
        """
        s_list = list(s)
        for shift in shifts:
            start, end, direction = shift
            shift_multiplier = 1 if direction == 1 else -1
            for i in range(start, end + 1):
                base = ord('a') 
                s_list[i] = chr((ord(s_list[i]) - base + shift_multiplier) % 26 + base)
        return ''.join(s_list)