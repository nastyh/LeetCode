class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return chr(ord(num1) + ord(num2))


    def addStrings(self, num1: str, num2: str) -> str:
        # Grab the length of longest one
        max_length = max(len(num1), len(num2))

        result = []
        carry = 0
        for index in range (1, max_length + 1):
            # Walk from the end back
            rev_index = index * - 1
            # Place zero if other array is longer
            digit1 = num1[rev_index] if index < len(num1) + 1 else 0
            digit2 = num2[rev_index] if index < len(num2) + 1 else 0
            # Add the current number column
            sum = str(int(digit2) + int(digit1) + carry)
            # Determine if we have a carry
            if len(sum) == 2:
                carry = int(sum[0])
                result.insert(0, sum[1])
            else:
                carry = 0
                result.insert(0, sum[0])
        # Special case of a carry on last addition
        if carry:
            result.insert(0, "1")

        return "".join(result)
