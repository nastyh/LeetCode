class Solution:
    def compress(self, chars: List[str]) -> int:
        # it doesn't count, they want to modify chars
        # and do it inplace
        d = {}
        res = []
        if len(chars) == 1:
            return chars[0]
        for c in chars:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for k, v in d.items():
            res.append(k)
            res.append(str(v))
        return res 
    def compress_pointers(self, chars: List[str]) -> int:
        # We initiate both left and right pointer at the beginning. We iterate the right pointer
        # from left either to end or till we have similar character as the left pointer is pointing.
        # Once we get the count, remove all the characters from the next character of left pointer to
        # the the right pointer and insert the count (splitting the digits if there are more than one digit).
        l, r = 0, 0
        s = len(chars)
        while l < s:
            n = 0
            r = l
            while r < s and chars[l] == chars[r]: # while we're processing letters
                if chars[l] == chars[r]:
                    n += 1
                r += 1

            if n > 1: # doing insertions 
                for k in range(l + 1, r):
                    chars.pop(l + 1)
                    s -= 1
                for k in range(len(str(n))):
                    l = l + 1
                    chars.insert(l, str(n)[k])
                    s += 1

            l += 1
            r = l

        return len(chars)