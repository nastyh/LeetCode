class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  # O(s) and O(26) or O(1)
        """
        Scan the array with 2 pointers: left and right
        Store the frequency of each character
        Compute the replacement cost: cells count between left and right pointers - the highest frequency
        if the replacement cost <= k: update longest string size
        if the replacement cost > k: decrease frequency of character at left pointer; increase left pointer and repeat
        """
        l, d, res = 0, {}, 0
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 0
            d[s[r]] += 1
            cell_count = r - l + 1
            if cell_count - max(d.values()) <= k:
                res = max(res, cell_count)
            else:
                d[s[l]] -= 1
                if not d[s[l]]:
                    d.pop(s[l])
                l += 1
        return res