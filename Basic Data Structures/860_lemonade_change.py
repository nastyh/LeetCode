class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        O(n) and O(1)
        If a customer brings a ＄5 bill, then we take it.
        If a customer brings a ＄10 bill, we must return a five dollar bill. If we don't have a five dollar bill, the answer is False, since we can't make correct change.
        If a customer brings a ＄20 bill, we must return ＄15.
        If we have a ＄10 and a ＄5, then we always prefer giving change in that, because it is strictly worse for making change than three ＄5 bills.
        Otherwise, if we have three ＄5 bills, then we'll give that.
        Otherwise, we won't be able to give ＄15 in change, and the answer is False
        """
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
        def lemonadeChange_with_list(self, bills: List[int]) -> bool:
            """
            O(n) and O(1) since it's only three elements in dp
            first element is for 5s, second for 10s, third for 20s
            Same idea: first give out bigger denominations 
            """
            dp = [0, 0, 0]
            for b in bills:
                if b == 5:
                    dp[0] += 1
                elif b == 10:
                    if dp[0] == 0:
                        return False
                    else:
                        dp[0] -= 1
                        dp[1] += 1
                elif b == 20:
                    if dp[1] == 0:
                        if dp[0] < 3:
                            return False
                        else:
                            dp[0] -= 3
                            dp[2] += 1
                    else:
                        if dp[0] < 1: 
                            return False
                        else: 
                            dp[0] -= 1
                            dp[1] -= 1
                            dp[2] += 2
            return True
