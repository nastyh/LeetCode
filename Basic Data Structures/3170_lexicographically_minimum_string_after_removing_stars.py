import heapq


class Solution:
    def clearStars_heap(self, s: str) -> str:
        """
        O(nlogn) due to the heap
        O(n) space for the heap
        Go over the string.
        If the heap isn't empty and we run into an asterisk
        take out the lexicographically smallest character
        -j because we stored the index as negative to prioritize latest indices on tie.
        Set both the character at position -j and the current '*' to '', effectively removing both.

        If it's not an asterisk, just push the current element and its (negative) index into the heap
        -i is to ensure if two characters are the same, the one closer to the asterisk (rightmost)
        is popped first (lex smallest among those closest to the *).
        """
        res = list(s)
        h = []
        for i, ch in enumerate(s):
            if ch == '*' and h:
                to_delete, j = heapq.heappop(h)
                res[-j] = ''
                res[i] = ''
            else:
                heapq.heappush(h, (ch, -i))
        return ''.join(res)
    def clearStars_stack(self, s: str) -> str:
        """
        TLE
        O(n^2) in the worst case b/c of two loops 
        O(n) to maintain a stack that will grow to the whole string if there are no asterisks

        Go over the string: if the stack is empty or it's a no asterisk,
        throw into the stack
        If it's an asterisk, 
        process the stack from right to left looking for the smallest element 
        min() works on the characters, too 
        if we found such, delete from the stack and stop the loop (we need to remove only 
        one that is most right in the list)
        The stack at the end will contain the answer 
        """
        st = []
        if not any(ch == '*' for ch in s):
            return s
        for ch in s: 
            if not st or ch != '*':
                st.append(ch)
            else:
                min_ch = min(st)
                for i in range(len(st) - 1, -1, -1):
                    if st[i] == min_ch:
                        del st[i]
                        break 
        return ''.join(st)
