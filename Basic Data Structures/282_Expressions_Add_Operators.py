class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        O(4^n): at each digit, there are three alternative choices plus a choice to continue using the
        current operand
        O(n)
        For each recursive call, choose a substring of num (as the next operand).
        If it's the first operand, add it to the path and update current_value and last_operand.
        otherwise, try adding the other signs: +, -, or *
        edge cases: input w/ leading zeroes, like 105
        Large inputs where no valid expression matches the target.
        """
        result = []
        def backtrack(index, path, current_value, last_operand):
            # Base case: If we've used all digits, check if the expression evaluates to target
            if index == len(num):
                if current_value == target:
                    result.append(path)
                return

            # Iterate over the remaining digits
            for i in range(index, len(num)):
                # Get the current operand as a substring
                operand_str = num[index:i + 1]
                operand = int(operand_str)

                # Skip operands with leading zeros
                if len(operand_str) > 1 and operand_str[0] == '0':
                    continue

                if index == 0:
                    # First operand, just add it to the path
                    backtrack(i + 1, operand_str, operand, operand)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + operand_str, current_value + operand, operand)
                    # Subtraction
                    backtrack(i + 1, path + "-" + operand_str, current_value - operand, -operand)
                    # Multiplication
                    backtrack(i + 1, path + "*" + operand_str, current_value - last_operand + last_operand * operand, last_operand * operand)

        # Start backtracking
        backtrack(0, "", 0, 0)
        return result
        
    def addOperators(self, num, target):  # O(4^N * N) b/c of 4 recursive paths and need to build a string every time. Space O(N)
        L = len(num)
        ans = set()
        
        def backtrack(i, total, last, expr):
            if i == L:
                if total == target:
                    ans.add(expr)
                return
            
            for j in range(i, L):
                n = int(num[i:j+1])
                if i == 0:
                    backtrack(j+1, n, n, str(n))
                else:
                    backtrack(j + 1, total + n, n, expr + '+' + str(n))
                    backtrack(j + 1, total - n, -n, expr + '-' + str(n))
                    backtrack(j + 1, total - last + last * n, last * n, expr + '*' + str(n))
                if n == 0:
                    break
                    
        backtrack(0, 0, 0, '')
        return list(ans)
