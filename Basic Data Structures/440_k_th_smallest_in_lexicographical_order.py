class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        O(logn * logn)
        O(1) -- nothing else to save
        
        Imagine the numbers 1 to n organized in a prefix tree (trie).
        You want to walk this tree in lexicographical order, starting from 1, and find the kth number.

        Instead of generating the full list, we count how many numbers are under a
        given prefix (curr) and use this count to skip entire subtrees if needed.

        If k = 2, you start from 1 and ask: how many numbers under 1 in [1, 13]? → 5 (1, 10, 11, 12, 13)
        Since 5 ≥ 2, you move deeper (i.e., curr *= 10 → 10), decrementing k by 1 (k = 1). Now curr = 10.
        From 10, there is only one valid number (10), and k = 1, so answer is 10.
        """
        def get_count(prefix, n):
            """
            to compute how many numbers with given prefix are ≤ n.
            """
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # start from the 1st number
        while k > 0:
            count = get_count(curr, n)
            if k >= count:
                # skip the whole subtree
                k -= count
                curr += 1
            else:
                # go deeper in the subtree
                curr *= 10
                k -= 1
        return curr

    def findKthNumber(self, n: int, k: int) -> int:
        """
        Times out
        O(n) to pass 
        O(1) since the output list res doesn't count
        
        We start from 1 and try to go deeper by multiplying by 10 (i.e., 1 → 10 → 100, etc.).
        If going deeper is not possible (exceeds n), we go to the next sibling (i.e., 1 → 2 → 3, ..., → 9).

        Start from curr = 1.
        If curr * 10 <= n, go deeper: e.g., 1 → 10.
        If we can’t go deeper, try curr + 1 (next sibling).
        If curr + 1 > n or curr % 10 == 9, we go up the tree (backtrack) until we find a valid next sibling.
        """
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res[k-1]
    