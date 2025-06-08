from typing import List


class Solution:
    def lexicalOrder_optimal(self, n: int) -> List[int]:
        """
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
        return res
    
    def lexicalOrder(self, n: int) -> List[int]:
        """
        The question asks to do in O(1) space, though
        O(nlogn) due to sorting
        O(n) due to all_nums and res

        Generate all the candidates and save in a list as strings
        If you sort a list of strings, it will be sorted in a lexicographical order
        After that just return as a list of integers 
        """
        all_nums = [str(num) for num in range(1, n + 1)]
        res = []
        for num in sorted(all_nums):
            res.append(int(num))
        return res
        """
        or we can do just two lines as 
        all_nums = [str(num) for num in range(1, n + 1)]
        return [int(num) for num in sorted(all_nums)]
        """