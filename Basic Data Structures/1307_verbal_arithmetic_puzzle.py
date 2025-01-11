import math
from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        O(m + klogk + 10^k)
        O(m) to process words and result, m the total length of everything
        10^k is the worst case for all permutations (bit better since leading 0 aren't considered)
        klogk is for sorting
        O(k+m), k for the set and m for the recursion stack
        """
        head = set()
        num = dict()
        for word in words:
            for i in range(len(word)):
                if i == 0 and len(word) > 1:
                    head.add(word[i])
                if word[i] not in num:
                    num[word[i]] = 10 ** (len(word) - i - 1)
                else:
                    num[word[i]] += 10 ** (len(word) - i - 1)
        num2 = dict()
        for i in range(len(result)):
            if i == 0 and len(result ) > 1:
                head.add(result[i])
            if result[i] not in num2:
                num2[result[i]] = 10 ** (len(result) - i - 1)
            else:
                num2[result[i]] += 10 ** (len(result) - i - 1)
        arr = list(set([i for i in num] + [i for i in num2]))
        arr.sort(key = lambda x: -(num[x] if x in num else 0) -(num2[x] if x in num2 else 0))
        suml, sumr = sum([num[i] for i in num]), sum([num2[i] for i in num2])
        s = [suml, sumr]
        left, right = 0, 0
        check = set()

        def backTrack(x, left, right):
            if len(check) == len(arr):
                if left == right:
                    return True
                else:
                    return False
            a = arr[x]
            if abs(left - right) > 9 * (max(s[0], s[1])):
                return False
            for i in range(10):
                if i in check:
                    continue
                if i == 0 and a in head:
                    continue
                s[0] = s[0] - num[a] if a in num else s[0]
                s[1] = s[1] - num2[a] if a in num2 else s[1]
                check.add(i)
                if backTrack(x + 1, left + num[a] * i if a in num else left, right + num2[a] * i if a in num2 else right):
                    return True
                s[0] = s[0] + num[a] if a in num else s[0]
                s[1] = s[1] + num2[a] if a in num2 else s[1]
                check.remove(i)
            return False

        return backTrack(0, 0, 0)