class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # monotonously increasing stack here
        stack = [(0, 0)]
        ans, sum_stack = 0, 0
        for i, num in enumerate(arr, start = 1):
            cnt = 1
            while stack[-1][0] > num:
                n, c = stack.pop()
                cnt += c
                sum_stack -= c * n
            stack.append((num, cnt))
            sum_stack += num * cnt 
            ans = (ans + sum_stack) % (10**9 + 7)
        return ans

    def sumSubarrayMins_another(self, arr: List[int]) -> int:
        stack = [(0, 0, 0)]
        ans = 0
        for i, num in enumerate(arr, start = 1):
            cnt = 1
            while stack[-1][0] > num:
                cnt += stack.pop()[1]
            sum_stack = num * cnt + stack[-1][2]
            stack.append((num, cnt, sum_stack))
            ans = (ans + sum_stack) % (10**9 + 7)
        return ans