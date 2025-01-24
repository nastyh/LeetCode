class Solution:
    def waysToBuyPensPencils_optimal(self, total: int, cost1: int, cost2: int) -> int:
        """
        O(m), m = total/cost1
        O(1)
        For each possible number of pens, the remaining money determines how many pencils can be purchased
        The maximum number of pens is total/cost1
        calculate the pencils directly for every valid range of money spent
        """
        res = 0 
        for pens_cost in range(0, total + 1, cost1):
            remaining_money = total - pens_cost
            res += (remaining_money // cost2) + 1
        return res 
    def waysToBuyPensPencils_brute_force(self, total: int, cost1: int, cost2: int) -> int:
        """
        Brute force
        O(n), n = total/cost1
        O(1)
        iterate over the number of pens that can be purchased (pens) to max possible (total // cost1)
        for each value of pens, remaining money after buying the pens  = total - pens * cost1
        use remaining money, to calc how many pencils can be purchased
        rem_money // cost2 + 1 and add to res
        return res
        """
        res = 0
        for pens in range(total // cost1 + 1): # +1 b/c of the option to buy zero items
            remaining = total - pens * cost1
            res += (remaining // cost2) + 1
        return res