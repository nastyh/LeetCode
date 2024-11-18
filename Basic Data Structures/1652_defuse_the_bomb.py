class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        O(nk) and O(n)
        If k is positive, we replace each element with the sum of the next k elements,
        using the modulo operator to handle circular bounds.
        If k is negative, we replace each element with the sum of the previous |k| elements,
        again using the modulo operator for circular bounds.
        """
        res = [0] * len(code)
        if k == 0: return res
        for i in range(len(res)):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    res[i] += code[j % len(code)]
            else:
                for j in range(i-abs(k), i):
                    res[i] += code[(j + len(code)) % len(code)]
        return res

    def decrypt_sliding(self, code: List[int], k: int) -> List[int]:
        """
        O(n) both
        As we shift the window to each new index, we update sum by subtracting
        the element that's leaving the window and adding the new element entering it.
        We repeat this process until we cover all indices and store each updated sum in result.
        """
        res = [0 for _ in range(len(code))]
        if k == 0:
            return res
        start, end, window_sum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            window_sum += code[i]
        # Scan through the code array as i moving to the right, update the window sum.
        for i in range(len(code)):
            res[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return res
