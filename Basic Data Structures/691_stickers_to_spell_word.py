class Solution:
    def minStickers_dp(self, stickers: List[str], target: str) -> int:
        """
        Suppose we need dp[state] stickers to satisfy all target[i]'s for which the i-th bit of state is set. 
        We would like to know dp[(1 << len(target)) - 1].
        For each state, let's work with it as now and look at what happens to it after applying a sticker.
        For each letter in the sticker that can satisfy an unset bit of state, we set the bit (now |= 1 << i).
        In the end, we know now is the result of applying that sticker to state, and we update our dp appropriately.
        O(2^T * S * T), S total num of letters in all stickers, T is the num of letters in the target word
        O(2^T), the space for dp
        """
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)
        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target)) # 
        dp[0] = 0
        for state in xrange(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]
    
    def minStickers_anothe(self, stickers: List[str], target: str) -> int:
        arr = []
        for i, ele in enumerate(stickers):
            arr.append({})
            for s in ele:
                arr[i][s] = 1 + arr[i].get(s, 0)
        dp = {}

        def dfs(target, strr):
            if target in dp:
                return dp[target]
            if not target: return 0
            res = 1 if strr else 0
            targetT = ""
            for i,c in enumerate(target):
                if c in strr and strr[c] > 0:
                    strr[c] -=1
                else: targetT += c
            used = float("inf")
            if targetT:
                for s in arr:
                    if targetT[0] in s:
                        used = min(used, dfs(targetT,s.copy()))
                dp[targetT] = used
                res+=used
            return res
            
        res = dfs(target, {})
        return res if res != float("inf") else -1